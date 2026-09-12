"""The Mérida Homes dataset (Sessions 20-21: Linear Regression).

A small, fixed, synthetic dataset of 60 fictional houses for sale in Mérida,
Yucatán. There is no randomness anywhere a student can trigger — the data is
generated once, with a fixed seed, at import time.
"""

import numpy as np

FEATURE_LABELS = {
    "size_m2": "Size (m²)",
    "bedrooms": "Bedrooms",
    "age_years": "Age (years)",
    "distance_km": "Distance to downtown (km)",
}
TARGET_LABEL = "Price (thousands of MXN)"


def _generate(seed: int = 50, n: int = 60):
    rng = np.random.default_rng(seed)

    size_m2 = rng.uniform(60, 300, n)
    bedrooms = np.clip(np.round(size_m2 / 55 + rng.normal(0, 0.5, n)), 1, 6)
    age_years = rng.uniform(0, 40, n)
    distance_km = rng.uniform(0.5, 20, n)

    true_price = 8.0 * size_m2 + 60.0 * bedrooms - 9.0 * age_years - 18.0 * distance_km + 300
    noise = rng.normal(0, 120, n)
    price = np.clip(true_price + noise, 300, None)

    return {
        "size_m2": size_m2,
        "bedrooms": bedrooms,
        "age_years": age_years,
        "distance_km": distance_km,
        "price": price,
    }


DATA = _generate()

ALL_FEATURES = ["size_m2", "bedrooms", "age_years", "distance_km"]


def feature_matrix(feature_names: list[str]) -> np.ndarray:
    return np.column_stack([DATA[name] for name in feature_names])


PRICE = DATA["price"]
