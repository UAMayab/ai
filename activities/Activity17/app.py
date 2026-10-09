"""Second Opinion: Support Vector Machines for Breast-Cancer Diagnosis
— Activity 17 (Session 31).

Run locally with:
    streamlit run app.py
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import diagnosis_data as dd
import svm_tools as sv
from toy_data import CENTER, CENTER_CLASS_NAMES, CLEAN, OUTLIER, OUTLIER_POINT, SHAPES

st.set_page_config(page_title="Second Opinion: SVMs", page_icon="🩺", layout="wide")

BLUE, RED = "#4C8BF5", "#E94F64"
CLASS_COLORS = [BLUE, RED, "#2BB673", "#F5A623"]
REGION_COLORS = ["rgba(76,139,245,0.18)", "rgba(233,79,100,0.18)", "rgba(43,182,115,0.18)", "rgba(245,166,35,0.18)"]
C_VALUES = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000]
GAMMA_VALUES = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
GRID_C = [0.01, 0.1, 1, 10, 100, 1000]
GRID_GAMMA = [0.001, 0.01, 0.1, 1, 10]
METRIC_LABELS = {"accuracy": "Accuracy", "recall": "Recall (sensitivity)", "precision": "Precision", "f1": "F1 score"}

st.title("🩺 Second Opinion: Support Vector Machines")
st.markdown(
    "A **support vector machine (SVM)** is a supervised learning model that separates two classes with "
    "the widest possible \"street\". In this activity you first see how it works on small 2D examples, then "
    "use it on a real medical problem: telling **malignant** from **benign** breast masses using "
    "measurements of cell nuclei."
)


# ------------------------------------------------------------ shared plotting
def discrete_scale(n_classes):
    """Colorscale that gives class i (heatmap value i) its own flat color."""
    scale = []
    for i in range(n_classes):
        scale += [[i / n_classes, REGION_COLORS[i]], [(i + 1) / n_classes, REGION_COLORS[i]]]
    return scale


def region_figure(model, X, y, title, class_names, X_extra=None, y_extra=None, support=None, margins=False,
                  equal_axis=True, highlight=None, axis_titles=("x₁", "x₂"), height=470):
    xs, ys, G = sv.grid(np.vstack([X] + ([X_extra] if X_extra is not None else [])))
    pred = model.predict(G).reshape(len(ys), len(xs))
    n_classes = len(class_names)
    fig = go.Figure(go.Heatmap(
        x=xs, y=ys, z=pred, zmin=-0.5, zmax=n_classes - 0.5, showscale=False, hoverinfo="skip",
        colorscale=discrete_scale(n_classes),
    ))
    if margins and hasattr(model, "decision_function") and n_classes == 2:
        f = model.decision_function(G).reshape(len(ys), len(xs))
        for level, name in [(0, "Decision boundary (f = 0)"), (-1, "Edges of the street (f = ±1)"), (1, None)]:
            fig.add_trace(go.Contour(x=xs, y=ys, z=f, showscale=False, hoverinfo="skip", name=name, showlegend=name is not None,
                                     contours=dict(start=level, end=level, size=1, coloring="none"),
                                     line=dict(color="#2BB673", width=3 if level == 0 else 2, dash="solid" if level == 0 else "dash")))
    for c in range(n_classes):
        m = y == c
        fig.add_trace(go.Scatter(x=X[m, 0], y=X[m, 1], mode="markers", name=f"{class_names[c]} (training)",
                                 marker=dict(color=CLASS_COLORS[c], size=8, line=dict(width=0.5, color="white"))))
        if X_extra is not None:
            m2 = y_extra == c
            fig.add_trace(go.Scatter(x=X_extra[m2, 0], y=X_extra[m2, 1], mode="markers", name=f"{class_names[c]} (test)",
                                     marker=dict(color=CLASS_COLORS[c], size=6, symbol="x", opacity=0.55)))
    if support is not None and len(support):
        fig.add_trace(go.Scatter(x=X[support, 0], y=X[support, 1], mode="markers", name="Support vectors",
                                 marker=dict(size=16, color="rgba(0,0,0,0)", line=dict(width=2.5, color="#FFD400"))))
    if highlight is not None:
        fig.add_trace(go.Scatter(x=[highlight[0]], y=[highlight[1]], mode="markers", name="The outlier",
                                 marker=dict(size=18, symbol="star", color="white", line=dict(width=1.5, color="black"))))
    fig.update_layout(title=title, height=height, margin=dict(t=50), legend=dict(orientation="h", y=-0.15),
                      xaxis_title=axis_titles[0], yaxis_title=axis_titles[1],
                      xaxis_range=[xs[0], xs[-1]], yaxis_range=[ys[0], ys[-1]])
    if equal_axis:
        fig.update_yaxes(scaleanchor="x", scaleratio=1)
        fig.update_xaxes(constrain="domain")  # shrink the plot area instead of padding the x-range
    return fig


def metric_row(scores, n_support=None):
    cols = st.columns(5 if n_support is not None else 4)
    for col, key in zip(cols, ("accuracy", "recall", "precision", "f1")):
        col.metric(METRIC_LABELS[key], f"{scores[key]:.1%}" if key != "f1" else f"{scores[key]:.3f}")
    if n_support is not None:
        cols[4].metric("Support vectors", n_support)


def confusion_table(scores):
    tn, fp, fn, tp = scores["tn"], scores["fp"], scores["fn"], scores["tp"]
    return pd.DataFrame(
        {"Predicted benign": [f"{tn} correct", f"{fn} missed cancers (false negatives)"],
         "Predicted malignant": [f"{fp} false alarms (false positives)", f"{tp} cancers found"]},
        index=["Truly benign", "Truly malignant"])


# ------------------------------------------------------------ cached model fits
@st.cache_data(show_spinner=False)
def clean_models():
    X, y, _, _ = CLEAN
    full = sv.svc("linear", 1e5).fit(X, y)
    only_sv = sv.svc("linear", 1e5).fit(X[full.support_], y[full.support_])
    return full, only_sv


@st.cache_data(show_spinner=False)
def outlier_sweep():
    X, y, Xt, yt = OUTLIER
    rows = []
    for C in C_VALUES:
        m = sv.svc("linear", C).fit(X, y)
        info = sv.linear_margin(m, X, y)
        rows.append({"C": C, "width": info["width"], "n_support": info["n_support"], "misclassified": info["misclassified"],
                     "inside": info["inside_margin"], "train": m.score(X, y), "test": m.score(Xt, yt),
                     "outlier_correct": bool(m.predict([OUTLIER_POINT])[0] == 0)})
    return rows


@st.cache_data(show_spinner=False)
def fit_toy(dataset, kernel, C, gamma, degree):
    X, y, Xt, yt = SHAPES[dataset]
    m = sv.svc(kernel, C, gamma, degree).fit(X, y)
    return m, m.score(X, y), m.score(Xt, yt)


@st.cache_data(show_spinner=False)
def fit_multiclass(kernel, C, gamma):
    X, y, Xt, yt = CENTER
    return sv.svc(kernel, C, gamma).fit(X, y), sv.one_vs_rest(kernel, C, gamma).fit(X, y)


@st.cache_data(show_spinner=False)
def fit_diagnosis(cols, model_name, kernel, C, gamma, degree):
    model = sv.scaled_logistic(C) if model_name == "logistic" else sv.scaled_svc(kernel, C, gamma, degree)
    model.fit(dd.X_TRAIN[:, list(cols)], dd.Y_TRAIN)
    scores = sv.scores(dd.Y_TEST, model.predict(dd.X_TEST[:, list(cols)]))
    n_support = int(model[-1].n_support_.sum()) if model_name == "svm" else None
    return model, scores, n_support


@st.cache_data(show_spinner=False)
def grid_search(cols, metric):
    table, best = sv.cv_grid_search(dd.X_TRAIN[:, list(cols)], dd.Y_TRAIN, GRID_C, GRID_GAMMA, metric)
    return table, best


def gamma_input(label, key, options=GAMMA_VALUES, default=1):
    return st.select_slider(label, options, default, key=key,
                            help="How far the influence of one training point reaches: small gamma = smooth, wide influence; large gamma = each point only affects its close neighborhood.")


tab_street, tab_c, tab_kernels, tab_multi, tab_dx, tab_vs = st.tabs([
    "🛣️ The Widest Street", "🎚️ C and the Soft Margin", "🌀 Kernels", "🎨 Multi-class",
    "🩺 Second Opinion: Diagnosis", "⚖️ SVM vs. Logistic Regression",
])

# ------------------------------------------------------------ The Widest Street
with tab_street:
    st.header("The widest street between two classes")
    st.markdown(
        "Many straight lines separate the blue and red points below. An SVM picks the one with the widest "
        "**margin**: the empty \"street\" between the two dashed lines. The solid line in the middle is the "
        "**decision boundary** (in 2D the hyperplane is a line). The circled points touching the edges of the street are "
        "the **support vectors**: they alone hold the street in place."
    )
    X, y, Xt, yt = CLEAN
    full, only_sv = clean_models()
    info = sv.linear_margin(full, X, y)
    retrain = st.toggle("Retrain the SVM using only the support vectors", key="street_retrain")
    model = only_sv if retrain else full
    title = (f"Retrained on the {len(full.support_)} support vectors only (the other points are shown but were not used)"
             if retrain else f"Trained on all {len(X)} training points")
    fig = region_figure(model, X, y, title, ["Class A", "Class B"], support=full.support_, margins=True)
    col_fig, col_info = st.columns([3, 1])
    col_fig.plotly_chart(fig, width="stretch", key="street_chart")
    with col_info:
        st.metric("Training points used", len(full.support_) if retrain else len(X))
        st.metric("Support vectors", info["n_support"])
        st.metric("Margin width (street width)", f"{info['width']:.3f}")
        st.metric("Test accuracy (400 new points)", f"{full.score(Xt, yt):.1%}")
        if retrain:
            diff = max(np.abs(only_sv.coef_[0] - full.coef_[0]).max(), abs(only_sv.intercept_[0] - full.intercept_[0]))
            st.success(f"Largest change in the line's equation after retraining: {diff:.1e} (practically zero).")
    w, b = full.coef_[0], full.intercept_[0]
    st.caption(f"Boundary trained on all points: {w[0]:.4f}·x₁ + {w[1]:.4f}·x₂ + {b:.4f} = 0. "
               "Margin width = 2 / |w|, the distance between the two dashed lines (both axes use the same scale).")

# ------------------------------------------------------------ C and the Soft Margin
with tab_c:
    st.header("C: how much is a mistake worth?")
    st.markdown(
        "Real data is messy. These training points contain **one mislabeled point** (the star): it is labeled "
        "blue but sits next to the red group. The **C** parameter is the penalty the SVM pays for every training "
        "point that falls inside the street or on the wrong side. **Small C**: mistakes are cheap, so the street "
        "can stay wide (a *soft* margin). **Large C**: mistakes are expensive, so the SVM narrows and tilts the "
        "street to classify every training point correctly. The test points (600 new points without the outlier) "
        "show which boundary generalizes."
    )
    X, y, Xt, yt = OUTLIER
    C = st.select_slider("C", C_VALUES, 1, key="c_value")
    show_test = st.toggle("Show the test points", key="c_show_test")
    m = sv.svc("linear", C).fit(X, y)
    info = sv.linear_margin(m, X, y)
    col_fig, col_info = st.columns([3, 1])
    col_fig.plotly_chart(region_figure(m, X, y, f"Linear SVM with C = {C:g}", ["Blue", "Red"],
                                       Xt if show_test else None, yt if show_test else None,
                                       support=m.support_, margins=True, highlight=OUTLIER_POINT),
                         width="stretch", key="c_chart")
    with col_info:
        st.metric("Margin width", f"{info['width']:.3f}")
        st.metric("Support vectors", info["n_support"])
        st.metric("Training points on the wrong side", info["misclassified"])
        st.metric("Training points inside the street", info["inside_margin"])
        st.metric("Training accuracy", f"{m.score(X, y):.1%}")
        st.metric("Test accuracy", f"{m.score(Xt, yt):.1%}")
        st.metric("The outlier is classified as", "Blue (its label)" if m.predict([OUTLIER_POINT])[0] == 0 else "Red")

    rows = outlier_sweep()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[r["C"] for r in rows], y=[r["width"] for r in rows], name="Margin width", mode="lines+markers", line_color=BLUE))
    fig.add_trace(go.Scatter(x=[r["C"] for r in rows], y=[r["test"] for r in rows], name="Test accuracy", mode="lines+markers",
                             line_color=RED, yaxis="y2"))
    fig.add_vline(x=C, line_dash="dot")
    fig.update_layout(title="Every C at once", xaxis=dict(type="log", title="C (log scale)"), yaxis_title="Margin width",
                      yaxis2=dict(title="Test accuracy", overlaying="y", side="right", tickformat=".0%", range=[0.9, 1.005]), height=360,
                      margin=dict(t=50), legend=dict(orientation="h", y=-0.25))
    st.plotly_chart(fig, width="stretch", key="c_sweep")
    best_test = max(r["test"] for r in rows)
    best_cs = [r["C"] for r in rows if r["test"] == best_test]
    lo, hi = rows[0], rows[-1]
    notes = []
    if hi["test"] < best_test:
        fit_all = "gets every training point right, including the mislabeled outlier" if hi["train"] == 1 else "chases the training points"
        notes.append(f"At the largest C ({hi['C']:g}) the SVM {fit_all}, with a street only {hi['width']:.3f} wide, and "
                     f"its test accuracy falls to {hi['test']:.1%}, below the best {best_test:.1%} (reached for C from "
                     f"{min(best_cs):g} to {max(best_cs):g}).")
    if lo["test"] < best_test:
        notes.append(f"At the smallest C ({lo['C']:g}) mistakes are so cheap that the street becomes very wide "
                     f"({lo['width']:.1f}) and {lo['n_support']} of the {len(y)} training points become support vectors: "
                     f"test accuracy {lo['test']:.1%}. That is *underfitting*.")
    if notes:
        st.info("**What the numbers show.** " + " ".join(notes))

# ------------------------------------------------------------ Kernels
with tab_kernels:
    st.header("When no straight line works: kernels")
    st.markdown(
        "A **kernel** lets the SVM draw curved boundaries. It measures how similar two points are in a way that "
        "acts like adding new features (for example x₁², x₂², x₁·x₂), so a flat hyperplane in that bigger space "
        "becomes a curve back in 2D, without ever computing the new features (the *kernel trick*)."
    )
    c1, c2, c3, c4, c5 = st.columns(5)
    dataset = c1.radio("Dataset", list(SHAPES), key="k_dataset")
    kernel = c2.selectbox("Kernel", sv.KERNELS, index=0, format_func=sv.KERNEL_LABELS.get, key="k_kernel")
    Ck = c3.select_slider("C", [0.01, 0.1, 1, 10, 100, 1000], 1, key="k_C")
    with c4:
        gamma = gamma_input("gamma (poly, RBF, sigmoid)", "k_gamma") if kernel != "linear" else "scale"
    degree = c5.slider("Degree (polynomial only)", 2, 5, 2, key="k_degree", disabled=kernel != "poly")
    show_test_k = c5.toggle("Show the test points", key="k_show_test")
    model, train_acc, test_acc = fit_toy(dataset, kernel, Ck, gamma, degree)
    X, y, Xt, yt = SHAPES[dataset]
    col_fig, col_info = st.columns([3, 1])
    col_fig.plotly_chart(region_figure(model, X, y, f"{sv.KERNEL_LABELS[kernel]} kernel on {dataset.split(' (')[0]}",
                                       ["Class A", "Class B"], Xt if show_test_k else None, yt if show_test_k else None,
                                       support=model.support_, margins=True), width="stretch", key="k_chart")
    with col_info:
        st.metric("Training accuracy", f"{train_acc:.1%}")
        st.metric("Test accuracy", f"{test_acc:.1%}")
        st.metric("Support vectors", f"{model.n_support_.sum()} of {len(y)}")
        if train_acc - test_acc >= 0.05:
            st.warning(f"Training accuracy is {100 * (train_acc - test_acc):.1f} points higher than test accuracy: "
                       "the boundary is fitting the training points rather than the pattern (overfitting).")
    with st.expander("The kernel formulas used here"):
        st.markdown(
            "- **Linear:** x · x′ (a straight line)\n"
            "- **Polynomial:** (gamma · x · x′ + 1)^degree\n"
            "- **RBF (radial basis function):** exp(−gamma · |x − x′|²)\n"
            "- **Sigmoid:** tanh(gamma · x · x′)"
        )

# ------------------------------------------------------------ Multi-class
with tab_multi:
    st.header("More than two classes")
    st.markdown(
        "An SVM separates **two** classes. For four classes there are two common strategies, and each model "
        "uses **one** of them: **one-vs-one** trains an SVM for every *pair* of classes (4 × 3 / 2 = 6 SVMs) and "
        "lets them vote; **one-vs-rest** trains one SVM per class against all the others together (4 SVMs) and "
        "picks the most confident. (scikit-learn's `SVC` always uses one-vs-one; the one-vs-rest model here is "
        "built with `OneVsRestClassifier`.)"
    )
    c1, c2, c3 = st.columns(3)
    mk = c1.selectbox("Kernel", ["linear", "rbf"], format_func=sv.KERNEL_LABELS.get, key="m_kernel")
    Cm = c2.select_slider("C", [0.01, 0.1, 1, 10, 100], 1, key="m_C")
    with c3:
        gm = gamma_input("gamma (RBF only)", "m_gamma") if mk == "rbf" else "scale"
    ovo, ovr = fit_multiclass(mk, Cm, gm)
    X, y, Xt, yt = CENTER
    col_a, col_b, col_c = st.columns(3)
    col_a.plotly_chart(region_figure(ovo, X, y, "One-vs-one (6 SVMs vote)", CENTER_CLASS_NAMES, height=430),
                       width="stretch", key="m_ovo")
    col_b.plotly_chart(region_figure(ovr, X, y, "One-vs-rest (4 SVMs compete)", CENTER_CLASS_NAMES, height=430),
                       width="stretch", key="m_ovr")
    xs, ys, G = sv.grid(X)
    disagree = (ovo.predict(G) != ovr.predict(G)).reshape(len(ys), len(xs)).astype(int)
    fig = go.Figure(go.Heatmap(x=xs, y=ys, z=disagree, colorscale=[[0, "rgba(0,0,0,0)"], [1, "rgba(233,79,100,0.55)"]],
                               showscale=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=X[:, 0], y=X[:, 1], mode="markers", showlegend=False,
                             marker=dict(color=[CLASS_COLORS[c] for c in y], size=6)))
    fig.update_layout(title=f"Where they disagree (red): {disagree.mean():.1%} of the area", height=430, margin=dict(t=50),
                      xaxis_range=[xs[0], xs[-1]], yaxis_range=[ys[0], ys[-1]])
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain="domain")
    col_c.plotly_chart(fig, width="stretch", key="m_disagree")
    po, pr = ovo.predict(Xt), ovr.predict(Xt)
    st.dataframe(pd.DataFrame({
        "Class": CENTER_CLASS_NAMES + ["All classes"],
        "One-vs-one test accuracy": [f"{np.mean(po[yt == c] == c):.1%}" for c in range(4)] + [f"{np.mean(po == yt):.1%}"],
        "One-vs-rest test accuracy": [f"{np.mean(pr[yt == c] == c):.1%}" for c in range(4)] + [f"{np.mean(pr == yt):.1%}"],
    }), hide_index=True, width="stretch")

# ------------------------------------------------------------ Diagnosis
with tab_dx:
    st.header("A second opinion for breast-cancer diagnosis")
    st.warning(
        "**This is a teaching tool, not a medical device.** It uses a public research dataset from the 1990s and "
        "must never be used to make decisions about real patients."
    )
    st.markdown(
        f"**The data (real):** {len(dd.Y)} breast masses from the University of Wisconsin. For each one, a doctor "
        "took a small sample with a fine needle, and 30 measurements were computed from a microscope image of the "
        "cell nuclei (size, shape, texture...). Each mass was diagnosed as **malignant** (cancer) or **benign**. "
        f"The app trains on {len(dd.Y_TRAIN)} patients and tests on the other {len(dd.Y_TEST)}, which the model never "
        "sees during training. Features are rescaled (standardized) using the training patients only."
    )
    mode = st.radio("Features", ["Two features (with a picture)", "All 30 features"], horizontal=True, key="dx_mode")
    if mode.startswith("Two"):
        c1, c2 = st.columns(2)
        f1 = c1.selectbox("Feature on the x-axis", dd.FEATURE_NAMES, index=dd.FEATURE_NAMES.index(dd.DEFAULT_FEATURES[0]), key="dx_f1")
        f2 = c2.selectbox("Feature on the y-axis", dd.FEATURE_NAMES, index=dd.FEATURE_NAMES.index(dd.DEFAULT_FEATURES[1]), key="dx_f2")
        cols = (dd.FEATURE_NAMES.index(f1), dd.FEATURE_NAMES.index(f2))
    else:
        cols = tuple(range(30))
    c1, c2, c3, c4 = st.columns(4)
    kd = c1.selectbox("Kernel", sv.KERNELS, index=2, format_func=sv.KERNEL_LABELS.get, key="dx_kernel")
    Cd = c2.select_slider("C", [0.01, 0.1, 1, 10, 100, 1000], 1, key="dx_C")
    gd = c3.selectbox("gamma", ["scale", 0.001, 0.01, 0.1, 1, 10], key="dx_gamma", disabled=kd == "linear",
                      format_func=lambda g: f"scale (= 1 / {len(cols)} features)" if g == "scale" else str(g))
    dd_deg = c4.slider("Degree (polynomial only)", 2, 5, 3, key="dx_degree", disabled=kd != "poly")
    model, scores, n_sup = fit_diagnosis(cols, "svm", kd, Cd, gd, dd_deg)

    st.subheader("Results on the test patients")
    metric_row(scores, n_sup)
    st.caption("Malignant is the *positive* class. **Recall** = share of real cancers the model found. **Precision** = "
               "share of \"malignant\" predictions that were really malignant. **F1** combines both (their harmonic mean).")
    col_conf, col_fig = st.columns([2, 3])
    col_conf.markdown("**Confusion matrix** (test patients)")
    col_conf.dataframe(confusion_table(scores), width="stretch")
    if len(cols) == 2:
        col_fig.plotly_chart(region_figure(model, dd.X_TRAIN[:, list(cols)], dd.Y_TRAIN, f"{sv.KERNEL_LABELS[kd]} SVM",
                                           dd.CLASS_NAMES, dd.X_TEST[:, list(cols)], dd.Y_TEST, equal_axis=False,
                                           axis_titles=(dd.FEATURE_NAMES[cols[0]], dd.FEATURE_NAMES[cols[1]])),
                             width="stretch", key="dx_chart")
    else:
        col_fig.info("With 30 features the boundary lives in 30 dimensions, so there is no picture. Compare the numbers instead.")

    st.subheader("Grid search with cross-validation")
    st.markdown(
        "Which C and gamma should a real team use? They must **not** peek at the test patients. Instead, the "
        "training patients are split into 5 parts (*folds*); each combination of C and gamma (RBF kernel) is trained "
        "on 4 folds and scored on the 5th, 5 times, and the scores are averaged. Only the winning combination is "
        "then tested, once, on the test patients."
    )
    metric = st.radio("Choose the combination with the best", ["accuracy", "recall", "f1"], horizontal=True,
                      format_func=METRIC_LABELS.get, key="dx_grid_metric")
    with st.spinner("Running 150 cross-validation fits..."):
        table, (best_C, best_g) = grid_search(cols, metric)
    fig = go.Figure(go.Heatmap(z=table, x=[str(g) for g in GRID_GAMMA], y=[str(c) for c in GRID_C], colorscale="Blues",
                               text=np.round(table, 3), texttemplate="%{text}", hovertemplate="C=%{y}, gamma=%{x}: %{z:.4f}<extra></extra>"))
    fig.add_trace(go.Scatter(x=[str(best_g)], y=[str(best_C)], mode="markers", showlegend=False, hoverinfo="skip",
                             marker=dict(symbol="square-open", size=46, line=dict(width=3, color="#E94F64"))))
    fig.update_layout(title=f"Mean cross-validated {METRIC_LABELS[metric].lower()} (training patients only)", height=420,
                      xaxis_title="gamma", yaxis_title="C", margin=dict(t=50), xaxis_type="category", yaxis_type="category")
    st.plotly_chart(fig, width="stretch", key="dx_grid")
    st.markdown(f"**Best on cross-validation:** C = {best_C}, gamma = {best_g}, mean {METRIC_LABELS[metric].lower()} "
                f"= {table.max():.3f} (ties go to the smaller C, then the smaller gamma).")
    _, best_scores, best_sup = fit_diagnosis(cols, "svm", "rbf", best_C, best_g, 3)
    st.markdown("**That model, tested once on the test patients:**")
    metric_row(best_scores, best_sup)
    st.dataframe(confusion_table(best_scores), width="stretch")

# ------------------------------------------------------------ SVM vs. Logistic Regression
with tab_vs:
    st.header("SVM vs. logistic regression")
    st.markdown(
        "Logistic regression (Activity 14) also draws a boundary, but it is always straight (in the original "
        "features) and it uses *every* training point, not only support vectors. Both models use a **C** that "
        "controls regularization (larger C = less regularization), but the same number does not mean exactly the "
        "same thing in both."
    )
    c1, c2, c3, c4 = st.columns(4)
    mode_v = c1.radio("Features", ["Two features (default pair)", "All 30 features"], key="vs_mode")
    cols_v = tuple(dd.FEATURE_NAMES.index(f) for f in dd.DEFAULT_FEATURES) if mode_v.startswith("Two") else tuple(range(30))
    kv = c2.selectbox("SVM kernel", sv.KERNELS, index=2, format_func=sv.KERNEL_LABELS.get, key="vs_kernel")
    Cv = c3.select_slider("C (both models)", [0.01, 0.1, 1, 10, 100, 1000], 1, key="vs_C")
    gv = c4.selectbox("SVM gamma", ["scale", 0.001, 0.01, 0.1, 1, 10], key="vs_gamma", disabled=kv == "linear")
    svm_model, svm_scores, svm_sup = fit_diagnosis(cols_v, "svm", kv, Cv, gv, 3)
    lr_model, lr_scores, _ = fit_diagnosis(cols_v, "logistic", kv, Cv, gv, 3)
    st.dataframe(pd.DataFrame({
        "Model": [f"SVM ({sv.KERNEL_LABELS[kv]})", "Logistic regression"],
        "Accuracy": [f"{svm_scores['accuracy']:.1%}", f"{lr_scores['accuracy']:.1%}"],
        "Recall": [f"{svm_scores['recall']:.1%}", f"{lr_scores['recall']:.1%}"],
        "Precision": [f"{svm_scores['precision']:.1%}", f"{lr_scores['precision']:.1%}"],
        "F1": [f"{svm_scores['f1']:.3f}", f"{lr_scores['f1']:.3f}"],
        "Missed cancers": [svm_scores["fn"], lr_scores["fn"]],
        "False alarms": [svm_scores["fp"], lr_scores["fp"]],
    }), hide_index=True, width="stretch")
    diff = svm_scores["accuracy"] - lr_scores["accuracy"]
    winner = "the SVM" if diff > 0 else "logistic regression" if diff < 0 else "neither (a tie)"
    st.info(f"On these test patients, the higher accuracy comes from **{winner}**"
            + (f" (by {abs(diff) * 100:.1f} points, which is {round(abs(diff) * len(dd.Y_TEST))} patient(s))." if diff else "."))
    if len(cols_v) == 2:
        col_a, col_b = st.columns(2)
        axes = (dd.FEATURE_NAMES[cols_v[0]], dd.FEATURE_NAMES[cols_v[1]])
        col_a.plotly_chart(region_figure(svm_model, dd.X_TRAIN[:, list(cols_v)], dd.Y_TRAIN, f"SVM ({sv.KERNEL_LABELS[kv]})",
                                         dd.CLASS_NAMES, equal_axis=False, axis_titles=axes, height=420), width="stretch", key="vs_svm")
        col_b.plotly_chart(region_figure(lr_model, dd.X_TRAIN[:, list(cols_v)], dd.Y_TRAIN, "Logistic regression",
                                         dd.CLASS_NAMES, equal_axis=False, axis_titles=axes, height=420), width="stretch", key="vs_lr")

    st.subheader("A shape where the difference is obvious")
    circles = "Circles (one ring inside another)"
    X, y, Xt, yt = SHAPES[circles]
    lr_c = sv.scaled_logistic(1).fit(X, y)
    rbf_c = sv.svc("rbf", 1, 1).fit(X, y)
    col_a, col_b = st.columns(2)
    col_a.plotly_chart(region_figure(lr_c, X, y, f"Logistic regression: test accuracy {lr_c.score(Xt, yt):.1%}", ["Class A", "Class B"], height=420),
                       width="stretch", key="vs_circ_lr")
    col_b.plotly_chart(region_figure(rbf_c, X, y, f"RBF SVM (C = 1, gamma = 1): test accuracy {rbf_c.score(Xt, yt):.1%}", ["Class A", "Class B"], height=420),
                       width="stretch", key="vs_circ_svm")
