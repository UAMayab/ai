"""The Whispering Cave: A Depth-First Search Adventure — Activity 5 (Sessions 10-12).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph

from cave_data import ADJACENCY, DESCRIPTIONS, GOAL, NODE_KIND, START, undirected_edges
from dfs_engine import FULL_TRACE, discovery_path, enumerate_all_paths, query_reachable, slug

st.set_page_config(page_title="The Whispering Cave", page_icon="🔦", layout="wide")

st.title("🔦 The Whispering Cave: A Depth-First Search Adventure")
st.markdown(
    "You are a cave explorer standing at the mouth of the **Whispering Cave**. Somewhere "
    "inside, past ten chambers and winding tunnels, sits a chest of treasure. You only have "
    "one flashlight, so you can only look down **one tunnel at a time** — and if it's a dead "
    "end, you have to walk all the way back before you can try a different one. "
    "That's exactly how a computer explores a graph with **Depth-First Search (DFS)**."
)

NODE_COLORS = {"start": "#4C8BF5", "goal": "#F5A623", "deadend": "#999999", "normal": "#7ED321"}
CURRENT_COLOR = "#E94F64"

tab_space, tab_rules, tab_dfs = st.tabs(
    ["🧭 The Search Space", "🔗 Tunnel Rules", "🔦 Depth-First Explorer"]
)

# --------------------------------------------------------------- Search Space tab
with tab_space:
    st.header("What Are We Even Searching For? (Session 11)")
    st.write(
        "Before a computer can search for anything, it needs to know four things:\n\n"
        f"- **Initial state** — where we start: `{START}`.\n"
        f"- **Goal state** — where we're trying to get to: `{GOAL}`.\n"
        "- **Actions** — at any chamber, the tunnels we're allowed to walk down.\n"
        "- **Search space** — *every possible sequence of tunnels* we could ever walk, "
        "laid out like a giant map of maps."
    )
    st.info(
        "A **well-defined problem** has a clear start, a clear goal, and clear rules for "
        "moving between them — exactly like this cave. That's what makes it solvable by search!"
    )

    st.subheader("The Cave Map")
    st.caption("Blue = start, orange = treasure (goal), gray = dead ends, green = every other chamber.")
    nodes = [
        Node(id=n, label=n, size=22, color=NODE_COLORS[NODE_KIND[n]])
        for n in ADJACENCY
    ]
    edges = [Edge(source=a, target=b) for a, b in undirected_edges()]
    agraph(nodes=nodes, edges=edges, config=Config(width=750, height=450, directed=False, physics=True))

    st.subheader("The Entire Search Space, Brute-Force")
    all_paths = enumerate_all_paths()
    st.write(
        f"If we patiently tried every possible route with no repeated chambers, there are "
        f"exactly **{len(all_paths)} possible paths** from `{START}` to `{GOAL}` in this cave:"
    )
    for i, path in enumerate(all_paths, start=1):
        st.write(f"{i}. `{' → '.join(path)}`  ({len(path) - 1} tunnels)")
    st.warning(
        "Real search spaces (chess, route planning, word puzzles) can have *billions* of paths — "
        "far too many to try one by one. That's why we need smart search **algorithms**, not just "
        "brute force."
    )

# --------------------------------------------------------------- Tunnel Rules tab
with tab_rules:
    st.header("Facts, Rules, and Recursion (Session 10)")
    st.write(
        "In logic programming (like Prolog), we describe the world with **facts** (simple true "
        "statements) and **rules** (new facts we can derive from other facts). Here is the "
        "*entire* Whispering Cave, written as facts:"
    )

    facts_code = "\n".join(f"tunnel({slug(a)}, {slug(b)})." for a, b in undirected_edges())
    st.code(facts_code, language="prolog")

    st.write("And here is one **recursive rule** that answers 'can I eventually get from X to Y?':")
    st.code(
        "reachable(X, Y) :- tunnel(X, Y).\n"
        "reachable(X, Y) :- tunnel(X, Z), reachable(Z, Y).",
        language="prolog",
    )
    st.markdown(
        "This rule is recursive because **`reachable` is defined using `reachable` itself** — "
        "just like the `ancestor(X, Y)` rule from your Session 10 guided example. Each recursive "
        "call takes one more step through a tunnel, until either it lands directly on Y (the "
        "**base case**), or it runs out of new tunnels to try."
    )

    st.subheader("Ask the Oracle")
    chambers = list(ADJACENCY.keys())
    col1, col2 = st.columns(2)
    with col1:
        from_chamber = st.selectbox("From chamber", chambers, index=chambers.index(START))
    with col2:
        to_chamber = st.selectbox("To chamber", chambers, index=chambers.index(GOAL))

    if st.button("🔮 Ask the Oracle"):
        verdict, trace = query_reachable(from_chamber, to_chamber)
        for line in trace:
            st.text(line)
        if verdict:
            st.success(f"reachable({slug(from_chamber)}, {slug(to_chamber)}) = TRUE")
        else:
            st.error(f"reachable({slug(from_chamber)}, {slug(to_chamber)}) = FALSE")
        st.caption(
            "Notice: the Oracle just explored tunnel after tunnel, backtracking whenever it hit "
            "a dead end. That's Depth-First Search, hiding inside a recursive rule!"
        )

# --------------------------------------------------------------- DFS Explorer tab
with tab_dfs:
    st.header("Step Through Depth-First Search (Session 12)")
    st.write(
        "Click **Take one step** below to advance the search one move at a time. Watch the "
        "**stack** (a pile of chambers waiting to be explored — Last In, First Out) and the "
        "**visited** list (chambers we've already fully explored)."
    )

    if "step_index" not in st.session_state:
        st.session_state.step_index = 0

    col_step, col_reset = st.columns(2)
    with col_step:
        if st.button("▶️ Take one step", disabled=st.session_state.step_index >= len(FULL_TRACE)):
            st.session_state.step_index = min(st.session_state.step_index + 1, len(FULL_TRACE))
    with col_reset:
        if st.button("⏮️ Reset explorer"):
            st.session_state.step_index = 0

    idx = st.session_state.step_index
    if idx == 0:
        stack_now = [START]
        visited_now: list[str] = []
        current_node = None
        message = "Our explorer stands at the **Entrance**, flashlight ready. Click **Take one step** to begin!"
        finished = False
    else:
        step = FULL_TRACE[idx - 1]
        stack_now = step["stack_after"]
        visited_now = step["visited_after"]
        current_node = step["node"]
        message = step["message"]
        finished = step["action"] == "goal"

    st.progress(min(idx, len(FULL_TRACE)) / len(FULL_TRACE))
    st.markdown(f"**Step {idx} of {len(FULL_TRACE)}:** {message}")
    if finished:
        st.balloons()
        st.success(
            f"Found it in {idx} steps! The path DFS actually walked was: "
            f"`{' → '.join(discovery_path())}`."
        )

    col_graph, col_state = st.columns([2, 1])

    with col_state:
        st.subheader("📚 Stack (top of pile = next chamber)")
        if stack_now:
            for chamber in reversed(stack_now):
                st.write(f"- {chamber}")
        else:
            st.write("*(empty)*")

        st.subheader("✅ Visited, in order")
        st.write(", ".join(visited_now) if visited_now else "*(none yet)*")

    with col_graph:
        nodes = []
        for n in ADJACENCY:
            if n == current_node:
                color = CURRENT_COLOR
            elif n in visited_now:
                color = NODE_COLORS[NODE_KIND[n]]
            else:
                color = "#D9D9D9"
            size = 28 if n == current_node else 20
            nodes.append(Node(id=n, label=n, size=size, color=color))
        edges = [Edge(source=a, target=b) for a, b in undirected_edges()]
        agraph(nodes=nodes, edges=edges, config=Config(width=650, height=450, directed=False, physics=True))

    with st.expander("🔍 Show the full step-by-step trace table (once you're done exploring)"):
        st.table(
            [
                {
                    "Step": i + 1,
                    "Action": s["action"],
                    "Chamber": s["node"],
                    "Stack after (bottom → top)": " | ".join(s["stack_after"]) or "(empty)",
                    "Visited so far": " → ".join(s["visited_after"]),
                }
                for i, s in enumerate(FULL_TRACE)
            ]
        )

st.divider()
st.info(
    "When you're done exploring all three tabs, fill out **A5_ReflectionQuestions.md** and "
    "record your **5-minute explanation video** (see the README for what it must cover)."
)
