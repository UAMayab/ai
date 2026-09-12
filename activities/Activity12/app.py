"""Mérida Homes: Predicting Property Prices — Activity 12 (Sessions 20-21).

Run locally with:
    streamlit run app.py

Or use the shared class link once deployed to Streamlit Community Cloud.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from house_data import ALL_FEATURES, DATA, FEATURE_LABELS, PRICE, TARGET_LABEL
from regression_engine import CANONICAL_ITERATIONS, CANONICAL_LEARNING_RATE, CANONICAL_MULTI_VAR, CANONICAL_ONE_VAR, predict, run

st.set_page_config(page_title="Mérida Homes", page_icon="🏠", layout="wide")

st.title("🏠 Mérida Homes: Predicting Property Prices")
st.markdown(
    "**Mérida Homes** is a fictional real-estate agency. Before listing a property, agents want "
    "a quick, data-driven price estimate — a job perfectly suited to **Linear Regression**: "
    "learning a straight-line (or flat-plane) relationship between a house's features and its "
    "price from 60 real past sales."
)

PLAY_BUTTON = dict(
    type="buttons",
    showactive=False,
    x=0.05,
    y=1.15,
    xanchor="left",
    buttons=[
        dict(label="▶️ Play", method="animate", args=[None, {"frame": {"duration": 200, "redraw": True}, "fromcurrent": True}]),
        dict(label="⏸️ Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]),
    ],
)



tab_data, tab_simple, tab_multi = st.tabs(
    ["🏠 The Dataset", "📈 One-Variable Regression (Session 20)", "📊 Multi-Variable Regression (Session 21)"]
)

# --------------------------------------------------------------- Dataset tab
with tab_data:
    st.header("60 Recent Sales in Mérida")
    df = pd.DataFrame({FEATURE_LABELS[k]: DATA[k] for k in ALL_FEATURES})
    df[TARGET_LABEL] = PRICE
    st.dataframe(df, use_container_width=True)

    st.subheader("How Does Each Feature Relate to Price?")
    cols = st.columns(2)
    for i, feature in enumerate(ALL_FEATURES):
        with cols[i % 2]:
            fig = go.Figure(go.Scatter(x=DATA[feature], y=PRICE, mode="markers", marker=dict(color="#4C8BF5", size=8)))
            fig.update_layout(
                title=f"{FEATURE_LABELS[feature]} vs. {TARGET_LABEL}",
                xaxis_title=FEATURE_LABELS[feature],
                yaxis_title=TARGET_LABEL,
                height=320,
                margin=dict(t=40, b=10, l=10, r=10),
            )
            st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Notice **Size** has the clearest, strongest-looking relationship with price — that's "
        "why Session 20 starts with size alone, before Session 21 adds the other three features."
    )

# --------------------------------------------------------------- One-variable tab
with tab_simple:
    st.header("Session 20: One-Variable Linear Regression")
    st.markdown(
        "The model is just `price = w × size + b`. Training means using **gradient descent** "
        "to nudge `w` and `b` so the line fits the 60 points as closely as possible, minimizing "
        "the **cost function** (mean squared error)."
    )

    st.subheader("🎛️ Playground — try your own learning rate and iteration count")
    st.caption("This section is for exploration only — it does not affect your graded questions below.")
    col_lr, col_it = st.columns(2)
    with col_lr:
        lr = st.slider("Learning rate", 0.01, 1.2, 0.3, 0.01, key="simple_lr")
    with col_it:
        iters = st.slider("Iterations", 10, 300, 100, 10, key="simple_iters")

    playground = run(["size_m2"], lr, iters)
    x_line = np.array([DATA["size_m2"].min(), DATA["size_m2"].max()])

    frames = []
    for i, snap in enumerate(playground["snapshots"]):
        y_line = snap["weights"][0] * x_line + snap["bias"]
        frames.append(
            go.Frame(
                data=[go.Scatter(x=DATA["size_m2"], y=PRICE, mode="markers"), go.Scatter(x=x_line, y=y_line, mode="lines")],
                name=str(i),
                layout=go.Layout(title=f"Iteration {snap['iteration']} — cost = {snap['cost']:,.0f}"),
            )
        )
    first = playground["snapshots"][0]
    fig = go.Figure(
        data=[
            go.Scatter(x=DATA["size_m2"], y=PRICE, mode="markers", name="Actual sales", marker=dict(color="#4C8BF5", size=9)),
            go.Scatter(x=x_line, y=first["weights"][0] * x_line + first["bias"], mode="lines", name="Model's line", line=dict(color="#E94F64", width=3)),
        ],
        layout=go.Layout(
            xaxis_title=FEATURE_LABELS["size_m2"], yaxis_title=TARGET_LABEL, height=480,
            updatemenus=[PLAY_BUTTON],
            sliders=[dict(active=0, x=0.15, y=1.15, len=0.8, currentvalue={"prefix": "Iteration "},
                          steps=[dict(method="animate", args=[[str(i)], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}], label=str(s["iteration"])) for i, s in enumerate(playground["snapshots"])])],
        ),
        frames=frames,
    )
    st.plotly_chart(fig, use_container_width=True)
    diverged = not np.isfinite(playground["bias"]) or abs(playground["bias"]) > 1e6 or playground["cost_history"][-1] > playground["cost_history"][0]
    col1, col2, col3 = st.columns(3)
    if diverged:
        col1.metric("Final slope (w)", "⚠️ diverged")
        col2.metric("Final intercept (b)", "⚠️ diverged")
        col3.metric("R²", "⚠️ diverged")
        st.warning(
            "The cost went UP instead of down — this learning rate is too high and the model "
            "**diverged** (its numbers blew up instead of settling). Try a smaller learning rate."
        )
    else:
        col1.metric("Final slope (w)", f"{playground['weights'][0]:.3f}")
        col2.metric("Final intercept (b)", f"{playground['bias']:.2f}")
        col3.metric("R²", f"{playground['r2']:.3f}")

    st.divider()
    st.subheader("📌 Canonical Model (this is what your reflection questions are graded against)")
    st.caption(f"Fixed settings: learning rate = {CANONICAL_LEARNING_RATE}, iterations = {CANONICAL_ITERATIONS}.")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Slope (w)", f"{CANONICAL_ONE_VAR['weights'][0]:.3f}")
    c2.metric("Intercept (b)", f"{CANONICAL_ONE_VAR['bias']:.2f}")
    c3.metric("R²", f"{CANONICAL_ONE_VAR['r2']:.4f}")
    c4.metric("MSE", f"{CANONICAL_ONE_VAR['mse']:,.1f}")

    st.subheader("🔮 Predict a Price (using the canonical model)")
    size_input = st.slider("House size (m²)", 60, 300, 150, 5, key="predict_size_simple")
    predicted = predict(CANONICAL_ONE_VAR, {"size_m2": size_input})
    st.success(f"Predicted price for a {size_input} m² house: **{predicted:,.1f} thousand MXN**")

# --------------------------------------------------------------- Multi-variable tab
with tab_multi:
    st.header("Session 21: Multi-Variable Linear Regression")
    st.markdown(
        "Real prices depend on more than size. The model becomes "
        "`price = w1·size + w2·bedrooms + w3·age + w4·distance + b` — one weight per feature."
    )

    st.subheader("🎛️ Playground — choose which features to include")
    st.caption("This section is for exploration only — it does not affect your graded questions below.")
    chosen = ["size_m2"]
    cols = st.columns(4)
    cols[0].checkbox(FEATURE_LABELS["size_m2"], value=True, disabled=True, key="feat_size")
    for i, feature in enumerate(["bedrooms", "age_years", "distance_km"]):
        if cols[i + 1].checkbox(FEATURE_LABELS[feature], value=(feature != "distance_km"), key=f"feat_{feature}"):
            chosen.append(feature)

    col_lr, col_it = st.columns(2)
    with col_lr:
        lr_m = st.slider("Learning rate", 0.01, 1.2, 0.3, 0.01, key="multi_lr")
    with col_it:
        iters_m = st.slider("Iterations", 10, 300, 100, 10, key="multi_iters")

    playground_m = run(chosen, lr_m, iters_m)

    diverged_m = not np.isfinite(playground_m["bias"]) or abs(playground_m["bias"]) > 1e6 or playground_m["cost_history"][-1] > playground_m["cost_history"][0]

    st.write(f"**Features used:** {', '.join(FEATURE_LABELS[f] for f in chosen)}")
    coef_cols = st.columns(len(chosen) + 2)
    if diverged_m:
        for i in range(len(chosen)):
            coef_cols[i].metric(FEATURE_LABELS[chosen[i]], "⚠️ diverged")
        coef_cols[-2].metric("R²", "⚠️ diverged")
        coef_cols[-1].metric("MSE", "⚠️ diverged")
        st.warning(
            "The cost went UP instead of down — this learning rate is too high and the model "
            "**diverged**. Try a smaller learning rate."
        )
    else:
        for i, feature in enumerate(chosen):
            coef_cols[i].metric(FEATURE_LABELS[feature], f"{playground_m['weights'][i]:.2f}")
        coef_cols[-2].metric("R²", f"{playground_m['r2']:.3f}")
        coef_cols[-1].metric("MSE", f"{playground_m['mse']:,.0f}")

    cost_fig = go.Figure(go.Scatter(y=playground_m["cost_history"], mode="lines", line=dict(color="#4C8BF5", width=3)))
    cost_fig.update_layout(title="Cost vs. Iteration (this playground run)", xaxis_title="Iteration", yaxis_title="Cost (MSE)", height=320, margin=dict(t=40, b=10, l=10, r=10))
    st.plotly_chart(cost_fig, use_container_width=True)

    st.divider()
    st.subheader("📌 Canonical Model (this is what your reflection questions are graded against)")
    st.caption(f"Fixed settings: ALL 4 features, learning rate = {CANONICAL_LEARNING_RATE}, iterations = {CANONICAL_ITERATIONS}.")
    c = st.columns(6)
    for i, feature in enumerate(ALL_FEATURES):
        c[i].metric(FEATURE_LABELS[feature], f"{CANONICAL_MULTI_VAR['weights'][i]:.2f}")
    c[4].metric("Intercept", f"{CANONICAL_MULTI_VAR['bias']:.2f}")
    c[5].metric("R²", f"{CANONICAL_MULTI_VAR['r2']:.4f}")
    st.caption(f"MSE = {CANONICAL_MULTI_VAR['mse']:,.1f}")

    st.subheader("🔮 Predict a Price (using the canonical multi-variable model)")
    p1, p2, p3, p4 = st.columns(4)
    size_i = p1.slider("Size (m²)", 60, 300, 150, 5, key="predict_size_multi")
    bed_i = p2.slider("Bedrooms", 1, 6, 3, 1, key="predict_bed_multi")
    age_i = p3.slider("Age (years)", 0, 40, 5, 1, key="predict_age_multi")
    dist_i = p4.slider("Distance (km)", 0.5, 20.0, 4.0, 0.5, key="predict_dist_multi")
    predicted_multi = predict(CANONICAL_MULTI_VAR, {"size_m2": size_i, "bedrooms": bed_i, "age_years": age_i, "distance_km": dist_i})
    st.success(f"Predicted price: **{predicted_multi:,.1f} thousand MXN**")

    st.divider()
    st.subheader("One-Variable vs. Multi-Variable: Which Predicts Better?")
    comp1, comp2 = st.columns(2)
    with comp1:
        st.metric("One-variable R² (size only)", f"{CANONICAL_ONE_VAR['r2']:.4f}")
        st.metric("One-variable MSE", f"{CANONICAL_ONE_VAR['mse']:,.1f}")
    with comp2:
        st.metric("Multi-variable R² (all 4 features)", f"{CANONICAL_MULTI_VAR['r2']:.4f}")
        st.metric("Multi-variable MSE", f"{CANONICAL_MULTI_VAR['mse']:,.1f}")

st.divider()
st.info("When you're done exploring all three tabs, fill out **A12_ReflectionQuestions.md** with your results.")
