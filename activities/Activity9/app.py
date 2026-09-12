"""Pack for the Trip: A Genetic Algorithm Challenge — Activity 9 (Session 16).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import streamlit as st

from ga_data import CAPACITY_KG, ITEMS, NUM_ITEMS, packed_items, weight_and_value
from ga_engine import GENERATIONS, HISTORY, OPTIMAL_CHROMOSOME, OPTIMAL_VALUE, POPULATION_SIZE

st.set_page_config(page_title="Pack for the Trip", page_icon="🧳", layout="wide")

st.title("🧳 Pack for the Trip: A Genetic Algorithm Challenge")
st.markdown(
    "You're heading out on a business trip with one **8 kg carry-on bag**. You have 8 items you'd "
    "like to bring, each with its own weight and usefulness score — but they don't all fit. "
    "Which combination should you pack to get the **most total usefulness** without going over "
    "the weight limit? This is the classic **Knapsack Problem**, and today you'll solve it the "
    "way nature does: with a **Genetic Algorithm**."
)

tab_problem, tab_ga = st.tabs(["🧳 The Packing Problem", "🧬 Run the Genetic Algorithm"])

# --------------------------------------------------------------- Problem tab
with tab_problem:
    st.header("Defining the Problem (Session 16)")
    st.write(f"Your bag can hold **{CAPACITY_KG} kg**. Here are your 8 candidate items:")
    st.table(
        [
            {"Item": name, "Weight (kg)": w, "Usefulness (value)": v}
            for name, w, v in ITEMS
        ]
    )
    st.info(
        f"There are **2^{NUM_ITEMS} = {2 ** NUM_ITEMS} possible packing combinations** — small "
        "enough to brute-force here, but real-world versions of this problem (scheduling staff, "
        "choosing which projects to fund, loading a delivery truck) can have far too many "
        "combinations to ever check by hand. That's what makes a Genetic Algorithm useful."
    )

    st.subheader("Genetic Algorithm Vocabulary")
    st.table(
        [
            {"Term": "Chromosome", "In this app": "One possible packing plan — a string of 8 yes/no decisions, one per item."},
            {"Term": "Gene", "In this app": "One yes/no decision within a chromosome — 'pack the Laptop or not?'"},
            {"Term": "Population", "In this app": f"A batch of {POPULATION_SIZE} candidate packing plans considered at once."},
            {"Term": "Fitness", "In this app": "Total usefulness of a packing plan — 0 if it's over the weight limit (discarded)."},
            {"Term": "Generation", "In this app": "One full round of selection, crossover, and mutation that produces a new population."},
            {"Term": "Selection", "In this app": "Roulette-wheel selection — fitter packing plans are more likely to be chosen as parents."},
            {"Term": "Crossover", "In this app": "One-point crossover — two parent plans swap part of their item choices to make two children."},
            {"Term": "Mutation", "In this app": "Each yes/no decision has a small chance of flipping, to explore new combinations."},
        ]
    )

# --------------------------------------------------------------- GA tab
with tab_ga:
    st.header("Step Through the Genetic Algorithm")
    st.write(
        "Click **Evolve to next generation** to advance one generation at a time. Watch the "
        "population's fitness values, the best packing plan *in this generation*, and the best "
        "one found *so far across all generations* — because this is a **non-elitist** genetic "
        "algorithm, the best plan can disappear from the population in a later generation, so we "
        "track the best-ever separately, exactly like the algorithm's own bookkeeping."
    )

    if "gen_step" not in st.session_state:
        st.session_state.gen_step = 0

    col_step, col_reset = st.columns(2)
    with col_step:
        if st.button("▶️ Evolve to next generation", disabled=st.session_state.gen_step >= len(HISTORY)):
            st.session_state.gen_step = min(st.session_state.gen_step + 1, len(HISTORY))
    with col_reset:
        if st.button("⏮️ Reset"):
            st.session_state.gen_step = 0

    idx = st.session_state.gen_step
    st.progress(idx / len(HISTORY))

    if idx == 0:
        st.info("No generations run yet. Click **Evolve to next generation** to begin.")
    else:
        h = HISTORY[idx - 1]
        st.markdown(f"### Generation {h['generation']} of {GENERATIONS}")

        rows = []
        for chromosome, fit in zip(h["population"], h["fitnesses"]):
            weight, value = weight_and_value(chromosome)
            rows.append(
                {
                    "Chromosome": "".join(str(b) for b in chromosome),
                    "Items": ", ".join(packed_items(chromosome)) or "(empty bag)",
                    "Weight (kg)": weight,
                    "Fitness": fit,
                    "Feasible?": "✅" if weight <= CAPACITY_KG else "❌ over limit",
                }
            )
        st.table(rows)

        col1, col2 = st.columns(2)
        with col1:
            st.metric(f"Best in Generation {h['generation']}", h["gen_best_fitness"])
            st.caption(", ".join(packed_items(h["gen_best_chromosome"])) or "(empty bag)")
        with col2:
            st.metric("Best-ever (across all generations so far)", h["best_ever_fitness"])
            st.caption(", ".join(packed_items(h["best_ever_chromosome"])) or "(empty bag)")

    if idx == len(HISTORY):
        st.divider()
        final = HISTORY[-1]
        st.subheader("Final Result")
        gap = OPTIMAL_VALUE - final["best_ever_fitness"]
        if gap == 0:
            st.success(
                f"The Genetic Algorithm found the **true optimal packing**: "
                f"`{', '.join(packed_items(final['best_ever_chromosome']))}` — total value "
                f"**{final['best_ever_fitness']}**, confirmed by brute-force search of all "
                f"{2 ** NUM_ITEMS} combinations."
            )
        else:
            st.warning(
                f"The Genetic Algorithm's best-ever packing scored **{final['best_ever_fitness']}**, "
                f"but the true brute-force optimum is **{OPTIMAL_VALUE}** "
                f"(`{', '.join(packed_items(OPTIMAL_CHROMOSOME))}`) — a gap of {gap}."
            )
        with st.expander("🔍 Show the true optimal packing (brute-force ground truth)"):
            weight, value = weight_and_value(OPTIMAL_CHROMOSOME)
            st.write(f"**Items:** {', '.join(packed_items(OPTIMAL_CHROMOSOME))}")
            st.write(f"**Weight:** {weight} kg / {CAPACITY_KG} kg")
            st.write(f"**Value:** {value}")

st.divider()
st.info("When you're done exploring both tabs, fill out **A9_ReflectionQuestions.md** with your results.")
