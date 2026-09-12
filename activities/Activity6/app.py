"""Six Degrees to Katún: A Breadth-First Search Networking Challenge —
Activity 6 (Session 13).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph

from bfs_engine import FULL_TRACE, dfs_path, discovery_path, shortest_distance
from network_data import ADJACENCY, DESCRIPTIONS, GOAL, NODE_KIND, START, undirected_edges

st.set_page_config(page_title="Six Degrees to Katún", page_icon="🤝", layout="wide")

st.title("🤝 Six Degrees to Katún: A Breadth-First Search Challenge")
st.markdown(
    "You're a Business Development Associate at **Meridian Consulting Group**, trying to land "
    "a meeting with **Elena Ruiz, CFO of Grupo Katún**. You don't know her directly — but maybe "
    "someone you know, knows someone, who knows her. You want the **fastest possible chain of "
    "introductions**, not just *any* chain. That's exactly the problem **Breadth-First Search "
    "(BFS)** solves."
)

NODE_COLORS = {"start": "#4C8BF5", "goal": "#F5A623", "deadend": "#999999", "normal": "#7ED321"}
CURRENT_COLOR = "#E94F64"
NEW_COLOR = "#B980F0"

tab_network, tab_bfs = st.tabs(["🕸️ The Network", "🔎 BFS Path Finder"])

# --------------------------------------------------------------- Network tab
with tab_network:
    st.header("Defining the Problem (Session 13)")
    st.write(
        "Just like any search problem, this one has:\n\n"
        f"- **Initial state** — where you start: `{START}`.\n"
        f"- **Goal state** — who you're trying to reach: `{GOAL}`.\n"
        "- **Actions** — at each person, asking them who *they* know.\n"
        "- **Search space** — every possible chain of introductions through the network."
    )
    st.info(
        "In business networking, this is often called **'degrees of separation'** — how many "
        "introductions stand between you and someone you want to meet. LinkedIn's \"2nd "
        "connection\" / \"3rd connection\" labels are exactly this idea."
    )

    st.subheader("Your Professional Network")
    st.caption("Blue = you, orange = Elena Ruiz (goal), gray = a dead-end contact, green = everyone else.")
    nodes = [Node(id=n, label=n, size=22, color=NODE_COLORS[NODE_KIND[n]]) for n in ADJACENCY]
    edges = [Edge(source=a, target=b) for a, b in undirected_edges()]
    agraph(nodes=nodes, edges=edges, config=Config(width=750, height=450, directed=False, physics=True))

    with st.expander("Who is who?"):
        for name, desc in DESCRIPTIONS.items():
            st.write(f"- **{name}** — {desc}")

# --------------------------------------------------------------- BFS tab
with tab_bfs:
    st.header("Step Through Breadth-First Search (Session 13)")
    st.write(
        "Click **Process next person in line** to advance one step at a time. BFS keeps a "
        "**line (queue)** of people to ask next — first come, first served (First In, First "
        "Out). Everyone at the same 'distance' from you joins the line before anyone farther "
        "away gets asked. That's what guarantees the *first* chain that reaches Elena is the "
        "*shortest possible* one."
    )

    if "step_index" not in st.session_state:
        st.session_state.step_index = 0

    col_step, col_reset = st.columns(2)
    with col_step:
        if st.button("▶️ Process next person in line", disabled=st.session_state.step_index >= len(FULL_TRACE)):
            st.session_state.step_index = min(st.session_state.step_index + 1, len(FULL_TRACE))
    with col_reset:
        if st.button("⏮️ Reset search"):
            st.session_state.step_index = 0

    idx = st.session_state.step_index
    if idx == 0:
        queue_now = [START]
        discovered_now = [START]
        processed_node = None
        new_this_step: list[tuple[str, int]] = []
        message = "You're the only one in line so far. Click **Process next person in line** to begin!"
        finished = False
    else:
        step = FULL_TRACE[idx - 1]
        queue_now = step["queue_after"]
        discovered_now = step["discovered_so_far"]
        processed_node = step["node"]
        new_this_step = step["new_contacts"]
        message = step["message"]
        finished = any(name == GOAL for name, _ in new_this_step)

    st.progress(min(idx, len(FULL_TRACE)) / len(FULL_TRACE))
    st.markdown(f"**Step {idx} of {len(FULL_TRACE)}:** {message}")

    if finished:
        st.balloons()
        path = discovery_path()
        st.success(
            f"Reached Elena Ruiz in **{shortest_distance()} introductions** — and because this "
            f"is BFS, that is *guaranteed* to be the fewest possible. The chain: "
            f"`{' → '.join(path)}`."
        )
        with st.expander("🔍 What would last session's DFS have done here?"):
            comparison = dfs_path()
            st.write(
                f"Running plain Depth-First Search (Session 12) on this exact same network, in "
                f"the same introduction order, produces this chain instead:\n\n"
                f"`{' → '.join(comparison)}`\n\n"
                f"That's **{len(comparison) - 1} introductions** — longer than BFS's "
                f"**{shortest_distance()}**. DFS still finds *a* path, just not necessarily the "
                f"shortest one — which is exactly why you'd pick BFS for a \"fewest introductions\" "
                f"business question."
            )

    col_graph, col_state = st.columns([2, 1])

    with col_state:
        st.subheader("🧍 Line to be processed (front → back)")
        st.write(", ".join(queue_now) if queue_now else "*(empty)*")

        st.subheader("✅ Reached so far")
        st.write(", ".join(discovered_now))

    with col_graph:
        new_names = {name for name, _ in new_this_step}
        nodes = []
        for n in ADJACENCY:
            if n == processed_node:
                color = CURRENT_COLOR
            elif n in new_names:
                color = NEW_COLOR
            elif n in discovered_now:
                color = NODE_COLORS[NODE_KIND[n]]
            else:
                color = "#D9D9D9"
            size = 28 if n == processed_node else 20
            nodes.append(Node(id=n, label=n, size=size, color=color))
        edges = [Edge(source=a, target=b) for a, b in undirected_edges()]
        agraph(nodes=nodes, edges=edges, config=Config(width=650, height=450, directed=False, physics=True))

    with st.expander("🔍 Show the full step-by-step trace table (once you're done exploring)"):
        st.table(
            [
                {
                    "Step": i + 1,
                    "Person asked": s["node"],
                    "Distance (hops from You)": s["level"],
                    "New contacts discovered": ", ".join(f"{n} ({lvl})" for n, lvl in s["new_contacts"]) or "(none)",
                    "Already known, skipped": ", ".join(s["skipped_contacts"]) or "(none)",
                }
                for i, s in enumerate(FULL_TRACE)
            ]
        )

st.divider()
st.info("When you're done exploring both tabs, fill out **A6_ReflectionQuestions.md** with your results.")
