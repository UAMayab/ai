"""YucaExpress: The Fastest Route Challenge — Activity 7 (Session 14).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import json

import streamlit as st
from streamlit_agraph import Config, Edge, Node
from streamlit_agraph import _agraph as _agraph_component

from map_data import ADJACENCY, COORDINATES, DESCRIPTIONS, GOAL, NODE_KIND, START, heuristic, undirected_edges
from search_engine import ASTAR_COST, ASTAR_PATH, ASTAR_TRACE, GREEDY_COST, GREEDY_PATH, GREEDY_TRACE

st.set_page_config(page_title="YucaExpress Route Challenge", page_icon="🚚", layout="wide")

st.title("🚚 YucaExpress: The Fastest Route Challenge")
st.markdown(
    "You dispatch deliveries for **YucaExpress** in Mérida. A courier needs to get from the "
    "**Depot** to the **Client Office** using the *cheapest total distance* — every extra "
    "kilometer costs the company time and fuel. You know the straight-line distance from any "
    "junction to the client's office (easy to compute from a map), but the real roads don't "
    "always go in a straight line. This is exactly the problem **Heuristic Search** solves."
)

NODE_COLORS = {"start": "#4C8BF5", "goal": "#F5A623", "normal": "#7ED321"}
CURRENT_COLOR = "#E94F64"
NEW_COLOR = "#B980F0"


def render_map(nodes_highlight: dict[str, str] | None = None, key: str = "map_main"):
    nodes_highlight = nodes_highlight or {}
    nodes = [
        Node(id=n, label=n, size=22, color=nodes_highlight.get(n, NODE_COLORS[NODE_KIND[n]]))
        for n in ADJACENCY
    ]
    edges = [Edge(source=a, target=b, label=f"{cost} km") for a, b, cost in undirected_edges()]
    config = Config(width=700, height=450, directed=False, physics=True)
    data_json = json.dumps({"nodes": [n.to_dict() for n in nodes], "edges": [e.to_dict() for e in edges]})
    config_json = json.dumps(config.__dict__)
    _agraph_component(data=data_json, config=config_json, key=key)


tab_map, tab_greedy, tab_astar = st.tabs(["🗺️ The Map", "🎯 Greedy Best-First", "⭐ A* Search"])

# --------------------------------------------------------------- Map tab
with tab_map:
    st.header("Defining the Problem (Session 14)")
    st.write(
        "This is a search problem, just like Sessions 12 and 13:\n\n"
        f"- **Initial state** — where the courier starts: `{START}`.\n"
        f"- **Goal state** — the delivery destination: `{GOAL}`.\n"
        "- **Actions** — at each junction, which road to take next.\n"
        "- **Cost** — the real, driven distance of each road (in km).\n\n"
        "What's new this session is the **heuristic**, h(n): an estimate — not a guarantee — of "
        "how far a junction is from the goal. Here, h(n) is simply the **straight-line "
        "distance** from that junction to the Client Office."
    )
    st.info(
        "The full evaluation function used by A\\* is:\n\n"
        "**f(n) = g(n) + h(n)**\n\n"
        "- g(n) = the real distance already driven to reach n\n"
        "- h(n) = the straight-line distance estimate from n to the goal\n"
        "- f(n) = the estimated total cost of a route through n"
    )

    st.subheader("The Map")
    st.caption("Blue = Depot (start), orange = Client Office (goal), green = every other junction. Edge labels are real road distances.")
    render_map(key="map_overview")

    st.subheader("Straight-Line Distances to the Client Office (the heuristic, h)")
    st.table(
        [
            {"Junction": n, "Coordinates (km)": str(COORDINATES[n]), "h(n) — straight-line km to goal": heuristic(n)}
            for n in ADJACENCY
        ]
    )

    with st.expander("Who/what is at each junction?"):
        for name, desc in DESCRIPTIONS.items():
            st.write(f"- **{name}** — {desc}")


def stepper_tab(trace, session_key, priority_label, algorithm_name, map_key):
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    col_step, col_reset = st.columns(2)
    with col_step:
        if st.button(f"▶️ Take one step ({algorithm_name})", key=f"step_btn_{session_key}", disabled=st.session_state[session_key] >= len(trace)):
            st.session_state[session_key] = min(st.session_state[session_key] + 1, len(trace))
    with col_reset:
        if st.button(f"⏮️ Reset ({algorithm_name})", key=f"reset_btn_{session_key}"):
            st.session_state[session_key] = 0

    idx = st.session_state[session_key]
    if idx == 0:
        current_node = None
        new_names: set[str] = set()
        closed_now = {START}
        message = f"The courier starts at **{START}**. Click **Take one step** to begin!"
        finished = False
    else:
        step = trace[idx - 1]
        current_node = step["node"]
        new_names = {c["node"] for c in step["new_frontier"]}
        closed_now = {trace[i]["node"] for i in range(idx) if trace[i]["action"] in ("expand", "goal")} | {START}
        message = step["message"]
        finished = step["action"] == "goal"

    st.progress(min(idx, len(trace)) / len(trace))
    st.markdown(f"**Step {idx} of {len(trace)}:** {message}")

    if finished:
        cost = GREEDY_COST if algorithm_name == "Greedy" else ASTAR_COST
        path = GREEDY_PATH if algorithm_name == "Greedy" else ASTAR_PATH
        st.balloons()
        st.success(f"Arrived! Total distance driven: **{cost} km**, via `{' → '.join(path)}`.")
        if algorithm_name == "A*" and GREEDY_TRACE and GREEDY_TRACE[-1]["action"] == "goal":
            diff = round(GREEDY_COST - ASTAR_COST, 2)
            st.info(
                f"Compare to the Greedy Best-First tab: A\\* found a route **{diff} km shorter** "
                f"by weighing real driven distance (g), not just straight-line closeness (h)."
            )

    col_graph, col_state = st.columns([2, 1])

    with col_state:
        st.subheader(f"📋 Frontier, sorted by {priority_label}")
        if idx == 0:
            st.write(f"{START} ({priority_label}={heuristic(START)})")
        else:
            frontier = trace[idx - 1]["frontier_after"]
            if frontier:
                for p, n in frontier:
                    st.write(f"- {n} ({priority_label}={p})")
            else:
                st.write("*(empty)*")

        st.subheader("✅ Settled junctions")
        st.write(", ".join(sorted(closed_now, key=lambda n: n != START)))

    with col_graph:
        highlight = {}
        for n in closed_now:
            highlight[n] = NODE_COLORS[NODE_KIND[n]]
        for n in new_names:
            highlight[n] = NEW_COLOR
        if current_node:
            highlight[current_node] = CURRENT_COLOR
        render_map(highlight, key=map_key)

    with st.expander("🔍 Show the full step-by-step trace table (once you're done exploring)"):
        st.table(
            [
                {
                    "Step": i + 1,
                    "Junction": s["node"],
                    priority_label: s["priority"],
                    "g (driven so far)": s.get("g", "—"),
                    "New roads discovered": ", ".join(c["node"] for c in s["new_frontier"]) or "(none)",
                    "Already settled, skipped": ", ".join(s["skipped"]) or "(none)",
                }
                for i, s in enumerate(trace)
            ]
        )


with tab_greedy:
    st.header("Step Through Greedy Best-First Search")
    st.write(
        "Greedy Best-First always drives toward whichever junction **looks closest to the "
        "goal in a straight line** — it never looks at how far it has already driven."
    )
    stepper_tab(GREEDY_TRACE, "greedy_step", "h", "Greedy", "map_greedy")

with tab_astar:
    st.header("Step Through A* Search")
    st.write(
        "A\\* balances two things at once: the real distance already driven (g), plus the "
        "straight-line estimate of what's left (h). It only commits to a junction once "
        "**f = g + h** says it's the most promising option overall."
    )
    stepper_tab(ASTAR_TRACE, "astar_step", "f", "A*", "map_astar")

st.divider()
st.info("When you're done exploring all three tabs, fill out **A7_ReflectionQuestions.md** with your results.")
