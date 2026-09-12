"""Linear regression via batch gradient descent, implemented from scratch
(Sessions 20-21). No scikit-learn — this is the algorithm itself, not a
library call.

`run()` is a pure function of its inputs (features, learning rate, iteration
count), so the same call always returns the same result. The two
**canonical models** (fixed learning rate and iteration count, computed once
at import time) are what every reflection question is graded against; the
app also lets students freely vary the learning rate/iterations/features for
exploration, which does not affect the canonical numbers below.
"""

import numpy as np

from house_data import ALL_FEATURES, PRICE, feature_matrix

CANONICAL_LEARNING_RATE = 0.3
CANONICAL_ITERATIONS = 200


def run(feature_names: list[str], learning_rate: float, iterations: int) -> dict:
    X = feature_matrix(feature_names)
    y = PRICE
    n, d = X.shape

    x_mean, x_std = X.mean(axis=0), X.std(axis=0)
    X_norm = (X - x_mean) / x_std

    w = np.zeros(d)
    b = 0.0
    cost_history = []
    snapshot_every = max(1, iterations // 30)  # cap animation frames at ~30
    snapshots = []

    for i in range(iterations):
        pred = X_norm @ w + b
        error = pred - y
        cost = float(np.mean(error ** 2))
        cost_history.append(cost)

        grad_w = (2 / n) * (X_norm.T @ error)
        grad_b = (2 / n) * np.sum(error)
        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        if i % snapshot_every == 0 or i == iterations - 1:
            real_w = w / x_std
            real_b = b - np.sum(w * x_mean / x_std)
            snapshots.append({"iteration": i + 1, "weights": real_w.copy(), "bias": real_b, "cost": cost})

    real_w = w / x_std
    real_b = b - np.sum(w * x_mean / x_std)
    final_pred = X @ real_w + real_b
    r2 = float(1 - np.sum((y - final_pred) ** 2) / np.sum((y - y.mean()) ** 2))
    mse = float(np.mean((y - final_pred) ** 2))

    return {
        "feature_names": feature_names,
        "weights": real_w,
        "bias": real_b,
        "r2": r2,
        "mse": mse,
        "cost_history": cost_history,
        "snapshots": snapshots,
    }


def predict(model: dict, feature_values: dict) -> float:
    x = np.array([feature_values[name] for name in model["feature_names"]])
    return float(x @ model["weights"] + model["bias"])


CANONICAL_ONE_VAR = run(["size_m2"], CANONICAL_LEARNING_RATE, CANONICAL_ITERATIONS)
CANONICAL_MULTI_VAR = run(ALL_FEATURES, CANONICAL_LEARNING_RATE, CANONICAL_ITERATIONS)
