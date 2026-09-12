"""ShopSmart Assistant: An Expert System for Customer Decisions —
Activity 8 (Session 15).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import streamlit as st

from expert_engine import evaluate_profile
from rules_data import FACT_LABELS, PROFILES, RULES

st.set_page_config(page_title="ShopSmart Assistant", page_icon="🧠", layout="wide")

st.title("🧠 ShopSmart Assistant: An Expert System for Customer Decisions")
st.markdown(
    "**ShopSmart** is a fictional online store. Instead of a human agent deciding what to do "
    "for every customer or every server alert, ShopSmart uses a small **expert system**: a set "
    "of IF-THEN rules, written down once by a human expert, that a computer can apply "
    "automatically and consistently, forever. This activity explores how that works."
)

tab_kb, tab_engine = st.tabs(["🧠 Knowledge Base & Architecture", "⚙️ Run the Inference Engine"])

# --------------------------------------------------------------- Knowledge Base tab
with tab_kb:
    st.header("The Five Parts of an Expert System (Session 15)")
    st.write(
        "Every expert system is built from the same five components. Here's what each one "
        "is **in this specific app**:"
    )
    st.table(
        [
            {"Component": "Knowledge base", "In this app": "The 4 rules listed below."},
            {"Component": "Inference engine", "In this app": "The rule-checking logic in the 'Run the Inference Engine' tab."},
            {"Component": "User interface", "In this app": "This Streamlit app itself."},
            {"Component": "Knowledge acquisition mechanisms", "In this app": "How the 4 rules below were written (by interviewing a 'business + IT expert' — in this case, your instructor)."},
            {"Component": "Explanation mechanisms", "In this app": "The condition-by-condition trace shown for every rule you check — showing exactly *why* it fired or didn't."},
        ]
    )

    st.subheader("The Rule Base (Knowledge Base)")
    st.caption("Every rule follows the same IF-THEN (production rule) format.")
    for rule in RULES:
        st.markdown(f"**{rule['id']} — {rule['name']}** *({rule['department']})*")
        st.code(rule["text"], language="text")

    st.subheader("The Five Fixed Profiles")
    st.write("These are the exact facts you'll feed into the inference engine in the next tab.")
    rows = []
    for name, facts in PROFILES.items():
        row = {"Profile": name}
        for fact, label in FACT_LABELS.items():
            row[label] = facts[fact]
        rows.append(row)
    st.dataframe(rows, use_container_width=True)

# --------------------------------------------------------------- Inference Engine tab
with tab_engine:
    st.header("Step Through the Inference Engine")
    st.write(
        "Pick a profile, then click **Check next rule** to run the engine's rules against it "
        "one at a time — exactly like a 'direct inference engine' checking rules "
        "'rule à rule' against known facts."
    )

    profile_name = st.selectbox("Choose a profile", list(PROFILES.keys()), key="profile_choice")

    if "rule_step" not in st.session_state or st.session_state.get("last_profile") != profile_name:
        st.session_state.rule_step = 0
        st.session_state.last_profile = profile_name

    results = evaluate_profile(profile_name)

    col_step, col_reset = st.columns(2)
    with col_step:
        if st.button("▶️ Check next rule", disabled=st.session_state.rule_step >= len(results)):
            st.session_state.rule_step = min(st.session_state.rule_step + 1, len(results))
    with col_reset:
        if st.button("⏮️ Reset"):
            st.session_state.rule_step = 0

    idx = st.session_state.rule_step
    st.progress(idx / len(results))

    if idx == 0:
        st.info("No rules checked yet. Click **Check next rule** to begin.")
    else:
        for r in results[:idx]:
            with st.container(border=True):
                fired_badge = "✅ FIRES" if r["fired"] else "❌ does not fire"
                st.markdown(f"**{r['id']} — {r['name']}** *({r['department']})* — {fired_badge}")
                for c in r["condition_results"]:
                    mark = "✓" if c["holds"] else "✗"
                    label = FACT_LABELS[c["fact"]]
                    st.write(f"{mark} `{label}` {c['comparison']} — actual value: `{c['actual_value']}`")
                if r["fired"]:
                    st.success(f"Conclusion: {r['conclusion']}")
                else:
                    st.caption("At least one condition failed, so this rule's conclusion does not apply.")

    if idx == len(results):
        conclusions = [r["conclusion"] for r in results if r["fired"]]
        st.divider()
        st.subheader("Final Summary")
        st.write(f"**{len(conclusions)} of {len(results)} rules fired** for `{profile_name}`.")
        if conclusions:
            for c in conclusions:
                st.write(f"- {c}")
        else:
            st.write("No rules triggered — no action needed for this profile.")

st.divider()
st.info("When you're done exploring both tabs and all five profiles, fill out **A8_ReflectionQuestions.md** with your results.")
