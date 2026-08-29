"""ReelWave: The Recommendation Meltdown — Activity 4 (Sessions 7-9).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph

from knowledge_graph import SIMILAR_TO_EDGES, build_graph, get_top_recommendations
from logic_engine import SUSPECTS, query
from reelwave_data import get_data_quality_report, get_raw_logs

st.set_page_config(page_title="ReelWave: Recommendation Meltdown", page_icon="🕵️", layout="wide")

st.title("🕵️ The ReelWave Recommendation Meltdown")
st.markdown(
    "ReelWave's recommendation engine went haywire overnight — kids' profiles are getting "
    "horror movie recommendations, and horror fans are getting cooking shows. You've been "
    "hired as an **AI Detective** to find out why. Is it bad **Data**, bad **Information**, "
    "or bad **Knowledge**? Work through all four tabs below, then fill out "
    "`A4_ReflectionQuestions.md`."
)

tab_data, tab_info, tab_graph, tab_interrogation = st.tabs(
    ["🗂️ Data", "📊 Information", "🕸️ Knowledge Graph", "🔎 Interrogation Room"]
)

# ---------------------------------------------------------------- Data tab
with tab_data:
    st.header("Raw Interaction Logs")
    st.write(
        "This is the raw, unprocessed **Data** ReelWave collects every time a profile "
        "watches or rates something."
    )
    df = get_raw_logs()

    profile_filter = st.multiselect(
        "Filter by profile type",
        sorted(df["profile_type"].unique()),
        default=list(sorted(df["profile_type"].unique())),
    )
    user_search = st.text_input("Search by user ID (optional)")

    filtered = df[df["profile_type"].isin(profile_filter)]
    if user_search:
        filtered = filtered[filtered["user_id"].str.contains(user_search, case=False)]
    st.dataframe(filtered, use_container_width=True)

    if st.button("🔍 Show data quality report"):
        report = get_data_quality_report(df)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total rows", report["total_rows"])
        c2.metric("Duplicate rows", report["duplicate_rows"])
        c3.metric("Missing ratings", report["missing_ratings"])
        c4.metric("Total corrupted rows", report["total_corrupted"])
        st.info("Raw Data can look fine at a glance — corruption like this hides in plain sight.")

# ----------------------------------------------------------- Information tab
with tab_info:
    st.header("Aggregated Viewing Stats")
    st.write(
        "**Information** is Data that has been organized and summarized so it becomes meaningful."
    )
    df = get_raw_logs()
    profile_choice = st.selectbox("Choose a profile type to inspect", sorted(df["profile_type"].unique()))
    subset = df[df["profile_type"] == profile_choice]
    avg_by_genre = subset.groupby("genre")["genre_match_score"].mean().sort_values(ascending=False)
    st.bar_chart(avg_by_genre)
    st.caption("Average genre-match score by genre, for the selected profile type.")
    st.warning("Notice anything unexpected in one of the bars? Keep it in mind for your report.")

# ------------------------------------------------------- Knowledge Graph tab
with tab_graph:
    st.header("The Content Knowledge Graph")
    st.write(
        "This is what ReelWave's recommender actually **knows**: content nodes connected by "
        "typed relationships (`genre_of`, `appropriate_for`, `similar_to`)."
    )

    if "removed_edges" not in st.session_state:
        st.session_state.removed_edges = set()

    col_graph, col_controls = st.columns([2, 1])

    with col_controls:
        st.subheader("Fix an Edge")
        edge_options = [
            f"{s} → {d} (similar_to, {w})"
            for s, d, w in SIMILAR_TO_EDGES
            if (s, d) not in st.session_state.removed_edges
        ]
        choice = st.selectbox("Select a 'similar_to' edge to remove", edge_options) if edge_options else None
        if st.button("🛠️ Remove this edge") and choice:
            src, rest = choice.split(" → ")
            dst = rest.split(" (")[0]
            st.session_state.removed_edges.add((src, dst))
            st.rerun()
        if st.button("↩️ Reset graph"):
            st.session_state.removed_edges = set()
            st.rerun()

        st.subheader("Top 3 Recommended")
        st.caption("Seed: a kids profile that just watched 'Bunny Buddies'")
        graph = build_graph(st.session_state.removed_edges)
        recs = get_top_recommendations(graph, seed="Bunny Buddies", n=3)
        for title, weight in recs:
            st.write(f"- **{title}** (match: {weight})")

    with col_graph:
        graph = build_graph(st.session_state.removed_edges)
        node_colors = {"content": "#4C8BF5", "genre": "#F5A623", "age_group": "#7ED321"}
        nodes = [
            Node(id=n, label=n, size=20, color=node_colors.get(data.get("node_type"), "#999999"))
            for n, data in graph.nodes(data=True)
        ]
        edges = [
            Edge(source=u, target=v, label=data.get("relation", ""))
            for u, v, data in graph.edges(data=True)
        ]
        config = Config(width=700, height=500, directed=True, physics=True)
        agraph(nodes=nodes, edges=edges, config=config)

# ---------------------------------------------------- Interrogation Room tab
with tab_interrogation:
    st.header("Interrogation Room")
    st.markdown(
        "**Rule:** `suspect(X) :- has_access(X, knowledge_graph), edited_at(X, Time), "
        "overnight(Time).`"
    )

    if "extra_facts" not in st.session_state:
        st.session_state.extra_facts = {}

    suspect_choice = st.selectbox("Pick a suspect to query", SUSPECTS)
    if st.button("⚖️ Run Query"):
        verdict, trace = query(suspect_choice, st.session_state.extra_facts)
        for line in trace:
            st.write("• " + line)
        if verdict:
            st.error(f"VERDICT: {suspect_choice} is GUILTY")
        else:
            st.success(f"VERDICT: {suspect_choice} is NOT GUILTY")

    st.divider()
    st.subheader("Add a New Fact")
    new_suspect = st.selectbox("Suspect", SUSPECTS, key="fact_suspect")
    new_time = st.text_input("Time this suspect edited the knowledge graph (HH:MM, 24h)", key="fact_time")
    col_add, col_clear = st.columns(2)
    with col_add:
        if st.button("➕ Add fact") and new_time:
            st.session_state.extra_facts[new_suspect] = new_time
            st.success(f"New fact added: edited_at({new_suspect}, {new_time})")
    with col_clear:
        if st.button("🧹 Clear added facts"):
            st.session_state.extra_facts = {}

st.divider()
st.info(
    "When you're done investigating, fill out **A4_ReflectionQuestions.md** and submit it "
    "along with your labeled screenshots."
)
