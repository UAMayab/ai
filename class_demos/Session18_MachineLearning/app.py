"""Session 18 Class Demo: Supervised & Unsupervised Learning — a visual,
animated teaching tool. Nothing here is graded and there is nothing to
submit; it's meant to be shown in class and explored freely.

Run locally with:
    streamlit run app.py
"""

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from ml_demos import boundary_line, classification_demo, kmeans_demo, linear_regression_demo

st.set_page_config(page_title="Supervised vs. Unsupervised Learning", page_icon="🤖", layout="wide")

st.title("🤖 Supervised vs. Unsupervised Learning")
st.markdown(
    "#### Session 18 — a visual tour, not an assignment\n"
    "There's nothing to submit here! Explore the animations, press play, drag the sliders, and "
    "use this alongside the class discussion."
)

PLAY_BUTTON = dict(
    type="buttons",
    showactive=False,
    x=0.05,
    y=1.15,
    xanchor="left",
    buttons=[
        dict(
            label="▶️ Play",
            method="animate",
            args=[None, {"frame": {"duration": 350, "redraw": True}, "fromcurrent": True, "transition": {"duration": 150}}],
        ),
        dict(
            label="⏸️ Pause",
            method="animate",
            args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}],
        ),
    ],
)


def slider_for(n_frames: int, prefix: str):
    return dict(
        active=0,
        x=0.15,
        y=1.15,
        len=0.8,
        currentvalue={"prefix": prefix},
        steps=[
            dict(method="animate", args=[[str(i)], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}], label=str(i + 1))
            for i in range(n_frames)
        ],
    )


tab_supervised, tab_unsupervised, tab_threats = st.tabs(
    ["🎯 Supervised Learning", "🧩 Unsupervised Learning", "⚠️ ML Threats 101"]
)

# --------------------------------------------------------------- Supervised
with tab_supervised:
    st.header("Supervised Learning: Learning from Labeled Examples")
    st.markdown(
        "In **supervised learning**, we show the model many examples that already have the "
        "*correct answer* attached (the \"label\"), and it learns a rule that maps input → "
        "answer. Once trained, it predicts the answer for brand-new examples it has never seen."
    )
    st.info(
        "**Real-life examples:** email spam filters (email text → spam/not spam) · medical "
        "diagnosis (scan → tumor benign/malignant) · credit scoring (financial history → "
        "approve/deny) · house price estimators (size/location → price) · voice assistants "
        "(audio → transcribed words) · face unlock (photo → is this you?)."
    )

    demo_choice = st.radio(
        "Pick a demo:", ["📈 Regression: Predict a number", "🟢🔴 Classification: Predict a category"], horizontal=True
    )

    if demo_choice.startswith("📈"):
        st.subheader("Predicting Ice Cream Sales from Temperature")
        st.caption(
            "The model starts with a random guess for the line, then nudges it a little closer "
            "to the data with every step — that nudging process is called **gradient descent**."
        )
        data = linear_regression_demo()
        x, y = data["x"], data["y"]
        x_line = np.array([x.min(), x.max()])

        frame_list = []
        for i, f in enumerate(data["frames"]):
            y_line = f["slope"] * x_line + f["intercept"]
            frame_list.append(
                go.Frame(
                    data=[go.Scatter(x=x, y=y, mode="markers"), go.Scatter(x=x_line, y=y_line, mode="lines")],
                    name=str(i),
                    layout=go.Layout(title=f"Step {i + 1} of {len(data['frames'])} — R² = {f['r_squared']:.2f}"),
                )
            )

        first = data["frames"][0]
        fig = go.Figure(
            data=[
                go.Scatter(x=x, y=y, mode="markers", name="Actual sales", marker=dict(color="#4C8BF5", size=9)),
                go.Scatter(
                    x=x_line,
                    y=first["slope"] * x_line + first["intercept"],
                    mode="lines",
                    name="Model's current guess",
                    line=dict(color="#E94F64", width=3),
                ),
            ],
            layout=go.Layout(
                xaxis_title="Temperature (°C)",
                yaxis_title="Ice cream sales ($)",
                updatemenus=[PLAY_BUTTON],
                sliders=[slider_for(len(frame_list), "Step ")],
                height=520,
            ),
            frames=frame_list,
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.subheader("Will the Student Pass? (Hours Studied vs. Attendance)")
        st.caption(
            "Green = passed, red = failed. The line is the model's current guess at the "
            "boundary between the two — watch it swing into place as training progresses."
        )
        data = classification_demo()
        hours, attendance, labels = data["hours"], data["attendance"], data["labels"]
        hours_range = np.linspace(hours.min(), hours.max(), 50)
        colors = np.where(labels == 1, "#3CB371", "#E94F64")

        frame_list = []
        for i, f in enumerate(data["frames"]):
            att_line = boundary_line(f, data["hours_mean"], data["hours_std"], data["attendance_mean"], data["attendance_std"], hours_range)
            frame_list.append(
                go.Frame(
                    data=[
                        go.Scatter(x=hours, y=attendance, mode="markers"),
                        go.Scatter(x=hours_range, y=att_line, mode="lines"),
                    ],
                    name=str(i),
                    layout=go.Layout(title=f"Step {i + 1} of {len(data['frames'])} — Accuracy = {f['accuracy']:.0%}"),
                )
            )

        first = data["frames"][0]
        first_line = boundary_line(first, data["hours_mean"], data["hours_std"], data["attendance_mean"], data["attendance_std"], hours_range)
        fig = go.Figure(
            data=[
                go.Scatter(x=hours, y=attendance, mode="markers", name="Students", marker=dict(color=colors, size=10)),
                go.Scatter(x=hours_range, y=first_line, mode="lines", name="Decision boundary", line=dict(color="#333333", width=3, dash="dash")),
            ],
            layout=go.Layout(
                xaxis_title="Hours studied",
                yaxis_title="Attendance (%)",
                yaxis_range=[35, 105],
                updatemenus=[PLAY_BUTTON],
                sliders=[slider_for(len(frame_list), "Step ")],
                height=520,
            ),
            frames=frame_list,
        )
        st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------------- Unsupervised
with tab_unsupervised:
    st.header("Unsupervised Learning: Finding Structure Without Labels")
    st.markdown(
        "In **unsupervised learning**, nobody tells the model the \"right answer\" — there are "
        "no labels at all. Instead, the model looks for patterns or natural groupings hiding in "
        "the data on its own."
    )
    st.info(
        "**Real-life examples:** customer segmentation for marketing campaigns · fraud/anomaly "
        "detection (flagging transactions that don't look like the rest) · recommendation "
        "systems grouping similar shoppers or songs · organizing news articles by topic · "
        "grouping genes with similar expression patterns in biology."
    )

    st.subheader("Grouping Customers by Spending Habits")
    st.caption(
        "Each dot is a customer (income vs. spending score). The three big X's are the "
        "algorithm's current guess at where each group's 'center' is — watch them walk toward "
        "the real clusters. This is **K-Means clustering**."
    )
    km = kmeans_demo()
    points = km["points"]
    palette = ["#4C8BF5", "#F5A623", "#9B59B6"]

    frame_list = []
    for i, f in enumerate(km["frames"]):
        centroids = f["centroids"]
        assignments = f["assignments"]
        point_colors = [palette[a] for a in assignments]
        frame_list.append(
            go.Frame(
                data=[
                    go.Scatter(x=points[:, 0], y=points[:, 1], mode="markers"),
                    go.Scatter(x=centroids[:, 0], y=centroids[:, 1], mode="markers"),
                ],
                name=str(i),
                layout=go.Layout(title=f"Round {i + 1} of {len(km['frames'])}"),
            )
        )
        frame_list[-1].data[0].marker = dict(color=point_colors, size=10, line=dict(width=1, color="white"))
        frame_list[-1].data[1].marker = dict(color=palette, size=22, symbol="x", line=dict(width=3, color="black"))

    first = km["frames"][0]
    first_colors = [palette[a] for a in first["assignments"]]
    fig = go.Figure(
        data=[
            go.Scatter(
                x=points[:, 0], y=points[:, 1], mode="markers", name="Customers",
                marker=dict(color=first_colors, size=10, line=dict(width=1, color="white")),
            ),
            go.Scatter(
                x=first["centroids"][:, 0], y=first["centroids"][:, 1], mode="markers", name="Cluster centers",
                marker=dict(color=palette, size=22, symbol="x", line=dict(width=3, color="black")),
            ),
        ],
        layout=go.Layout(
            xaxis_title="Annual income (thousands)",
            yaxis_title="Spending score",
            updatemenus=[PLAY_BUTTON],
            sliders=[slider_for(len(frame_list), "Round ")],
            height=520,
        ),
        frames=frame_list,
    )
    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------------- Threats
with tab_threats:
    st.header("⚠️ A Brief Look at Threats Facing Machine Learning")
    st.write(
        "ML systems don't just fail randomly — they can be deliberately attacked, or can quietly "
        "absorb problems from the data they were trained on. Here are four to know about."
    )

    with st.container(border=True):
        st.subheader("🖼️ Adversarial Examples")
        st.write(
            "Tiny changes to an input — invisible or meaningless to a human — can completely "
            "fool a trained model."
        )
        st.caption(
            "**Real example:** researchers showed that a few small stickers placed on a stop "
            "sign could cause a computer-vision model (of the kind used in early self-driving "
            "car research) to misread it as a speed limit sign, even though a human driver "
            "wouldn't be fooled for a second."
        )

    with st.container(border=True):
        st.subheader("☠️ Data Poisoning")
        st.write(
            "If an attacker can sneak bad examples into a model's training data, they can "
            "corrupt what it learns — sometimes in a very targeted way."
        )
        st.caption(
            "**Real example:** Microsoft's 'Tay' chatbot (2016) was designed to learn from "
            "conversations with the public on Twitter. Coordinated users flooded it with "
            "offensive input, and within 24 hours Tay had 'learned' to repeat offensive content "
            "— it had to be taken offline."
        )

    with st.container(border=True):
        st.subheader("⚖️ Bias & Discrimination")
        st.write(
            "A model trained on biased historical data will learn — and often amplify — that "
            "same bias, even with nobody intending it to."
        )
        st.caption(
            "**Real example:** Amazon scrapped an internal AI recruiting tool in 2018 after "
            "discovering it penalized résumés containing words like 'women's' (as in 'women's "
            "chess club'), because it was trained on a decade of résumés submitted mostly by men."
        )

    with st.container(border=True):
        st.subheader("🔓 Privacy Leakage")
        st.write(
            "Models can sometimes memorize specific details from their training data — and "
            "leak them back out."
        )
        st.caption(
            "**Real example:** researchers have shown that large language models can, under the "
            "right prompting, reproduce verbatim snippets of text (including personal "
            "information) that appeared in their training data."
        )

    st.divider()
    st.info(
        "The common thread: an ML model is only as trustworthy as the data it learned from and "
        "the assumptions built into how it's used — testing and validation matter as much as "
        "raw accuracy."
    )
