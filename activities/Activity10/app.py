"""SmartWash: A Fuzzy Logic Laundry Controller — Activity 10 (Session 17).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import pandas as pd
import streamlit as st

from fuzzy_data import DIRT_TERMS, LOAD_TERMS, OUTPUT_CENTERS, PROFILES, RULES
from fuzzy_engine import run

st.set_page_config(page_title="SmartWash Fuzzy Controller", page_icon="🧺", layout="wide")

st.title("🧺 SmartWash: A Fuzzy Logic Laundry Controller")
st.markdown(
    "Real washing machines don't ask 'is the load big or small?' as a strict Yes/No question — "
    "a load can be *kind of* small and *kind of* medium at the same time. **Fuzzy Logic** lets a "
    "controller reason with exactly that kind of in-between, real-world ambiguity, then still "
    "produce one precise decision: how many minutes to wash for."
)

curve_x = list(range(0, 11))


def curve_dataframe(terms: dict) -> pd.DataFrame:
    return pd.DataFrame({name: [fn(x) for x in curve_x] for name, fn in terms.items()}, index=curve_x)


tab_controller, tab_test = st.tabs(["🧺 The Fuzzy Controller", "🔬 Test the Controller"])

# --------------------------------------------------------------- Controller tab
with tab_controller:
    st.header("How SmartWash Reasons (Session 17)")
    st.write(
        "SmartWash reads two crisp sensor values — **Load Size** (0-10 kg) and **Dirtiness** "
        "(a 0-10 sensor reading) — and decides a **Wash Time** (0-90 minutes), following the same "
        "four steps as any fuzzy controller:"
    )
    st.table(
        [
            {"Step": "1. Fuzzification", "What happens": "Turn the crisp Load and Dirt numbers into a degree of membership (0 to 1) in linguistic terms like 'Small' or 'Heavy'."},
            {"Step": "2. Inference (rule base)", "What happens": "Check every IF-THEN rule; each rule's strength is the smaller of its two membership degrees."},
            {"Step": "3. Aggregation", "What happens": "For each possible Wash Time term (Short/Medium/Long), take the strongest rule that concluded it."},
            {"Step": "4. Defuzzification", "What happens": "Combine the three Wash Time terms into one precise number of minutes (weighted-average method)."},
        ]
    )

    st.subheader("Membership Functions")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Load Size (kg)**")
        st.line_chart(curve_dataframe(LOAD_TERMS))
    with col2:
        st.write("**Dirtiness (sensor reading)**")
        st.line_chart(curve_dataframe(DIRT_TERMS))
    st.caption(
        "The y-axis is degree of membership (0 = not at all, 1 = fully). Notice a value like 4 "
        "can be partly 'Small' AND partly 'Medium' at the same time — that overlap is the whole "
        "point of fuzzy logic."
    )

    st.subheader("The Rule Base (Knowledge Base)")
    st.table(
        [{"Rule": f"R{i+1}", "IF Load is": lt, "AND Dirt is": dt, "THEN Wash Time is": tt} for i, (lt, dt, tt) in enumerate(RULES)]
    )
    st.caption(f"Output term reference values used for defuzzification: {OUTPUT_CENTERS}")

# --------------------------------------------------------------- Test tab
with tab_test:
    st.header("Run the Controller on a Fixed Profile")
    st.write(
        "Pick one of the five fixed profiles below and see the full fuzzy reasoning pipeline, "
        "step by step. Everyone in the class sees the exact same numbers for these profiles."
    )

    profile_name = st.selectbox("Choose a profile", list(PROFILES.keys()))
    load, dirt = PROFILES[profile_name]
    result = run(load, dirt)

    st.markdown(f"**Load Size = {load} kg, Dirtiness = {dirt}**")

    st.subheader("Step 1 — Fuzzification")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Load membership degrees:")
        st.table([{"Term": k, "Degree": round(v, 2)} for k, v in result["load_degrees"].items()])
    with col2:
        st.write("Dirt membership degrees:")
        st.table([{"Term": k, "Degree": round(v, 2)} for k, v in result["dirt_degrees"].items()])

    st.subheader("Step 2 — Inference (rules that fired, strength > 0)")
    fired = [r for r in result["fired_rules"] if r["strength"] > 0]
    st.table(
        [
            {
                "Rule": f"IF Load={r['load_term']} AND Dirt={r['dirt_term']}",
                "THEN Time": r["time_term"],
                "Strength": round(r["strength"], 2),
            }
            for r in fired
        ]
    )

    st.subheader("Step 3 — Aggregation (strongest rule per output term)")
    st.table([{"Wash Time term": k, "Aggregated strength": round(v, 2)} for k, v in result["aggregated"].items()])

    st.subheader("Step 4 — Defuzzification")
    st.success(f"**Final Wash Time: {result['wash_time']} minutes**")

    st.divider()
    with st.expander("🧪 Sandbox: try your own Load/Dirt values (ungraded — for exploration only)"):
        st.caption(
            "This is just for building intuition. Your reflection questions are based on the "
            "five fixed profiles above, not on whatever you try here."
        )
        free_load = st.slider("Load Size (kg)", 0.0, 10.0, 5.0, 0.5)
        free_dirt = st.slider("Dirtiness", 0.0, 10.0, 5.0, 0.5)
        free_result = run(free_load, free_dirt)
        st.write(f"Wash Time: **{free_result['wash_time']} minutes**")

st.divider()
st.info("When you're done exploring both tabs, fill out **A10_ReflectionQuestions.md** with your results.")
