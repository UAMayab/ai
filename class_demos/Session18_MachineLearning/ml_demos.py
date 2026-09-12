"""Deterministic data + training loops for the Session 18 ML demo.

Everything here uses a fixed random seed, so the app looks and behaves the
same on every run — there's nothing to submit for this session, but the
visuals should still be stable and reproducible for classroom demos.
"""

import numpy as np

# --------------------------------------------------------------------------
# Demo 1: Linear Regression — "Ice Cream Sales vs. Temperature"
# --------------------------------------------------------------------------

def linear_regression_demo(iterations: int = 30, learning_rate: float = 0.1):
    rng = np.random.default_rng(7)
    temperature = rng.uniform(15, 35, size=40)
    true_slope, true_intercept = 12.0, -110.0
    noise = rng.normal(0, 25, size=40)
    sales = true_slope * temperature + true_intercept + noise
    sales = np.clip(sales, 0, None)

    # Normalize for stable gradient descent, then convert back for display.
    x_mean, x_std = temperature.mean(), temperature.std()
    x_norm = (temperature - x_mean) / x_std

    w, b = 0.0, float(sales.mean())
    n = len(temperature)
    frames = []
    for _ in range(iterations):
        y_pred = w * x_norm + b
        error = y_pred - sales
        grad_w = (2 / n) * np.sum(error * x_norm)
        grad_b = (2 / n) * np.sum(error)
        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        # Convert normalized-space (w, b) back to real (slope, intercept)
        real_slope = w / x_std
        real_intercept = b - w * x_mean / x_std
        r_squared = 1 - np.sum((sales - y_pred) ** 2) / np.sum((sales - sales.mean()) ** 2)
        frames.append({"slope": real_slope, "intercept": real_intercept, "r_squared": r_squared})

    return {"x": temperature, "y": sales, "frames": frames}


# --------------------------------------------------------------------------
# Demo 2: Logistic Regression — "Will the Student Pass?"
# --------------------------------------------------------------------------

def _sigmoid(z):
    return 1 / (1 + np.exp(-z))


def classification_demo(iterations: int = 40, learning_rate: float = 0.5):
    rng = np.random.default_rng(21)
    n = 60
    hours = rng.uniform(0, 10, size=n)
    attendance = rng.uniform(40, 100, size=n)

    score = 0.6 * hours + 0.05 * attendance - 5
    prob = _sigmoid(score + rng.normal(0, 0.8, size=n))
    labels = (prob > 0.5).astype(float)

    # Normalize features for stable gradient descent.
    x1 = (hours - hours.mean()) / hours.std()
    x2 = (attendance - attendance.mean()) / attendance.std()
    X = np.column_stack([x1, x2])

    w = np.zeros(2)
    b = 0.0
    frames = []
    for _ in range(iterations):
        z = X @ w + b
        pred = _sigmoid(z)
        error = pred - labels
        grad_w = X.T @ error / n
        grad_b = np.sum(error) / n
        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        accuracy = np.mean((pred > 0.5).astype(float) == labels)
        # Boundary in real (hours, attendance) space: w1*x1 + w2*x2 + b = 0
        frames.append({"w": w.copy(), "b": b, "accuracy": accuracy})

    return {
        "hours": hours,
        "attendance": attendance,
        "labels": labels,
        "hours_mean": hours.mean(),
        "hours_std": hours.std(),
        "attendance_mean": attendance.mean(),
        "attendance_std": attendance.std(),
        "frames": frames,
    }


def boundary_line(frame: dict, hours_mean, hours_std, attendance_mean, attendance_std, hours_range):
    """Given a frame's (w, b) in normalized space, return attendance values
    tracing the decision boundary across the given hours_range."""
    w1, w2 = frame["w"]
    b = frame["b"]
    if abs(w2) < 1e-9:
        return np.full_like(hours_range, np.nan)
    x1 = (hours_range - hours_mean) / hours_std
    x2 = -(w1 * x1 + b) / w2
    return x2 * attendance_std + attendance_mean


# --------------------------------------------------------------------------
# Demo 3: K-Means Clustering — "Grouping Customers by Spending Habits"
# --------------------------------------------------------------------------

def kmeans_demo(k: int = 3, iterations: int = 8):
    rng = np.random.default_rng(3)
    centers = np.array([[25, 20], [55, 70], [85, 30]])
    points = np.vstack(
        [rng.normal(loc=c, scale=[6, 8], size=(25, 2)) for c in centers]
    )

    # Deliberately bad initial centroid guesses (not from the data's natural centers).
    centroids = np.array([[20, 80], [50, 10], [90, 90]], dtype=float)

    frames = []
    for _ in range(iterations):
        distances = np.linalg.norm(points[:, None, :] - centroids[None, :, :], axis=2)
        assignments = np.argmin(distances, axis=1)
        frames.append({"centroids": centroids.copy(), "assignments": assignments.copy()})

        new_centroids = centroids.copy()
        for cluster_id in range(k):
            members = points[assignments == cluster_id]
            if len(members) > 0:
                new_centroids[cluster_id] = members.mean(axis=0)
        centroids = new_centroids

    # One final frame showing the converged assignment.
    distances = np.linalg.norm(points[:, None, :] - centroids[None, :, :], axis=2)
    assignments = np.argmin(distances, axis=1)
    frames.append({"centroids": centroids.copy(), "assignments": assignments.copy()})

    return {"points": points, "frames": frames}
