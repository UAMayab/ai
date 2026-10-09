"""Helpers around scikit-learn's SVC (which uses libsvm) for Activity 17.

- Kernels: linear, polynomial (gamma * x.x' + 1) ** degree, RBF
  exp(-gamma * |x - x'|^2), and sigmoid tanh(gamma * x.x').
- For the diagnosis data, features are standardized inside a pipeline, so the
  scaler only ever learns from the rows it is trained on (no test-set leakage,
  also inside every cross-validation fold).
- Metrics treat class 1 (malignant) as the positive class and are computed
  from the confusion matrix directly.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

KERNELS = ("linear", "poly", "rbf", "sigmoid")
KERNEL_LABELS = {"linear": "Linear", "poly": "Polynomial", "rbf": "RBF (radial)", "sigmoid": "Sigmoid"}
METRICS = ("accuracy", "recall", "precision", "f1")


def svc(kernel, C, gamma="scale", degree=3):
    # tol=1e-6 (libsvm's default is 1e-3) so margins and support vectors are exact to the digits shown
    return SVC(kernel=kernel, C=C, gamma=gamma, degree=degree, coef0=1.0 if kernel == "poly" else 0.0, tol=1e-6)


def scaled_svc(kernel, C, gamma="scale", degree=3):
    return make_pipeline(StandardScaler(), svc(kernel, C, gamma, degree))


def scaled_logistic(C):
    return make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=10_000))


def one_vs_rest(kernel, C, gamma="scale"):
    return OneVsRestClassifier(svc(kernel, C, gamma))


def scores(y_true, y_pred):
    """Accuracy, recall, precision, F1 (class 1 = positive) and the confusion matrix [[TN, FP], [FN, TP]]."""
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    recall = tp / (tp + fn) if tp + fn else 0.0
    precision = tp / (tp + fp) if tp + fp else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"accuracy": (tp + tn) / len(y_true), "recall": recall, "precision": precision, "f1": f1,
            "confusion": np.array([[tn, fp], [fn, tp]]), "tp": tp, "tn": tn, "fp": fp, "fn": fn}


def linear_margin(model, X, y):
    """For a linear SVC on raw 2D data: w, b, margin width 2/|w|, and how training points sit relative to the margin."""
    w, b = model.coef_[0], model.intercept_[0]
    f = model.decision_function(X)
    signed = np.where(y == model.classes_[1], f, -f)  # >= 1: outside the margin on the correct side
    return {
        "w": w, "b": b, "width": 2 / np.linalg.norm(w),
        "n_support": int(model.n_support_.sum()),
        "misclassified": int(np.sum(signed < 0)),
        "inside_margin": int(np.sum((signed >= 0) & (signed < 1 - 1e-6))),
    }


def grid(X, pad=0.6, n=220):
    x0, x1 = X[:, 0].min() - pad * X[:, 0].std(), X[:, 0].max() + pad * X[:, 0].std()
    y0, y1 = X[:, 1].min() - pad * X[:, 1].std(), X[:, 1].max() + pad * X[:, 1].std()
    xs, ys = np.linspace(x0, x1, n), np.linspace(y0, y1, n)
    xx, yy = np.meshgrid(xs, ys)
    return xs, ys, np.column_stack([xx.ravel(), yy.ravel()])


def cv_grid_search(X, y, C_values, gamma_values, metric, n_splits=5, seed=31):
    """Mean cross-validated score of an RBF SVM for every (C, gamma), using only the rows given (the training set).

    Ties are broken toward the smaller C, then the smaller gamma (the simpler model).
    """
    folds = list(StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed).split(X, y))
    table = np.zeros((len(C_values), len(gamma_values)))
    for i, C in enumerate(C_values):
        for j, g in enumerate(gamma_values):
            vals = []
            for fit_idx, val_idx in folds:
                model = scaled_svc("rbf", C, g).fit(X[fit_idx], y[fit_idx])
                vals.append(scores(y[val_idx], model.predict(X[val_idx]))[metric])
            table[i, j] = np.mean(vals)
    best = max(((i, j) for i in range(len(C_values)) for j in range(len(gamma_values))),
               key=lambda ij: (round(table[ij], 12), -ij[0], -ij[1]))
    return table, (C_values[best[0]], gamma_values[best[1]])
