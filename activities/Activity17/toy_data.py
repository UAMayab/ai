"""Small 2D teaching datasets for Activity 17 (Session 31: Support Vector Machines).

Every dataset is generated once, with a fixed seed, at import time, and comes
as (X_train, y_train, X_test, y_test). The test points are drawn from the same
distribution as the training points but are never used for training.

- clean:    two well-separated groups (a straight line can separate them).
- outlier:  two groups that a line separates, plus ONE mislabeled training
            point sitting close to the other group. The test set has no
            outlier, so it shows which boundary generalizes.
- circles:  one ring of points inside another (no straight line works).
- moons:    two interleaved half-circles.
- xor:      four corner groups, opposite corners share a class.
- center:   four classes: one in the middle, three around it (multi-class).
"""

import numpy as np


def _two_blobs(rng, n, centers, sd):
    X = np.vstack([rng.normal(centers[0], sd, (n, 2)), rng.normal(centers[1], sd, (n, 2))])
    return X, np.array([0] * n + [1] * n)


def _clean(seed=31):
    rng = np.random.default_rng(seed)
    X_tr, y_tr = _two_blobs(rng, 20, ([-2.0, -1.0], [2.0, 1.0]), 0.7)
    X_te, y_te = _two_blobs(rng, 200, ([-2.0, -1.0], [2.0, 1.0]), 0.7)
    return X_tr, y_tr, X_te, y_te


def _outlier(seed=10):
    rng = np.random.default_rng(seed)
    X_tr, y_tr = _two_blobs(rng, 40, ([-2.5, 0.0], [2.5, 0.0]), 0.8)
    X_te, y_te = _two_blobs(rng, 300, ([-2.5, 0.0], [2.5, 0.0]), 0.8)
    # one training point labeled class 0 but sitting next to class 1
    return np.vstack([X_tr, [1.2, -1.5]]), np.append(y_tr, 0), X_te, y_te


def _rings(rng, n, noise):
    t0, t1 = rng.uniform(0, 2 * np.pi, n), rng.uniform(0, 2 * np.pi, n)
    inner = np.column_stack([np.cos(t0), np.sin(t0)]) * 1.0
    outer = np.column_stack([np.cos(t1), np.sin(t1)]) * 2.2
    X = np.vstack([inner, outer]) + rng.normal(0, noise, (2 * n, 2))
    return X, np.array([0] * n + [1] * n)


def _moon_points(rng, n, noise):
    t0, t1 = rng.uniform(0, np.pi, n), rng.uniform(0, np.pi, n)
    upper = np.column_stack([np.cos(t0), np.sin(t0)])
    lower = np.column_stack([1 - np.cos(t1), 0.5 - np.sin(t1)])
    X = np.vstack([upper, lower]) + rng.normal(0, noise, (2 * n, 2))
    return X, np.array([0] * n + [1] * n)


def _xor_points(rng, n, sd):
    X = np.vstack([rng.normal(c, sd, (n, 2)) for c in ([1.5, 1.5], [-1.5, -1.5], [1.5, -1.5], [-1.5, 1.5])])
    return X, np.array([0] * (2 * n) + [1] * (2 * n))


def _split_pair(make, seed, n_train, n_test, *args):
    rng = np.random.default_rng(seed)
    X_tr, y_tr = make(rng, n_train, *args)
    X_te, y_te = make(rng, n_test, *args)
    return X_tr, y_tr, X_te, y_te


def _center(seed=4, n_train=40, n_test=200):
    rng = np.random.default_rng(seed)
    centers = [[0.0, 0.0], [0.0, 3.0], [-2.6, -1.5], [2.6, -1.5]]

    def make(n):
        X = np.vstack([rng.normal(c, 0.7, (n, 2)) for c in centers])
        return X, np.repeat(np.arange(4), n)

    X_tr, y_tr = make(n_train)
    X_te, y_te = make(n_test)
    return X_tr, y_tr, X_te, y_te


CLEAN = _clean()
OUTLIER = _outlier()
OUTLIER_POINT = OUTLIER[0][-1]
SHAPES = {
    "Circles (one ring inside another)": _split_pair(_rings, 7, 100, 300, 0.15),
    "Moons (two interleaved half-circles)": _split_pair(_moon_points, 8, 100, 300, 0.15),
    "XOR (opposite corners share a class)": _split_pair(_xor_points, 9, 50, 150, 0.6),
}
CENTER = _center()
CENTER_CLASS_NAMES = ["Middle", "Top", "Bottom left", "Bottom right"]
