"""The SmartWash fuzzy logic controller (Session 17: Fuzzy Logic).

A small, fixed fuzzy controller — the same "fuzzy washing machine" example
described in the course material: Load Size and Dirtiness (both 0-10) go in,
Wash Time (0-90 minutes) comes out. There is no randomness anywhere in this
file, and the rule base / membership functions never change.
"""

LOAD_RANGE = (0, 10)
DIRT_RANGE = (0, 10)
TIME_RANGE = (0, 90)


def _low_shoulder(x: float, cross: float) -> float:
    """1 at x=0, falling straight to 0 at x=cross."""
    return max(0.0, min(1.0, (cross - x) / cross))


def _mid_triangle(x: float, center: float, half_width: float) -> float:
    """A triangular peak: 0 at the edges, 1 at the center."""
    return max(0.0, 1 - abs(x - center) / half_width)


def _high_shoulder(x: float, cross: float, top: float) -> float:
    """0 at x=cross, rising straight to 1 at x=top (and staying at 1 beyond)."""
    return max(0.0, min(1.0, (x - cross) / (top - cross)))


# Load Size membership functions (kg, 0-10)
def load_small(x: float) -> float:
    return _low_shoulder(x, 5)


def load_medium(x: float) -> float:
    return _mid_triangle(x, 5, 5)


def load_large(x: float) -> float:
    return _high_shoulder(x, 5, 10)


LOAD_TERMS = {"Small": load_small, "Medium": load_medium, "Large": load_large}

# Dirtiness membership functions (sensor reading, 0-10) — same shape as load
DIRT_TERMS = {"Light": load_small, "Moderate": load_medium, "Heavy": load_large}

# Wash Time output terms: representative crisp value used for defuzzification
# (the "weighted average" technique named in the course material)
OUTPUT_CENTERS = {"Short": 15, "Medium": 45, "Long": 75}

# The rule base (knowledge base): (Load term, Dirt term) -> Time term
RULES: list[tuple[str, str, str]] = [
    ("Small", "Light", "Short"),
    ("Small", "Moderate", "Short"),
    ("Small", "Heavy", "Medium"),
    ("Medium", "Light", "Short"),
    ("Medium", "Moderate", "Medium"),
    ("Medium", "Heavy", "Long"),
    ("Large", "Light", "Medium"),
    ("Large", "Moderate", "Long"),
    ("Large", "Heavy", "Long"),
]

# Fixed, deterministic test profiles used for the graded reflection questions.
PROFILES: dict[str, tuple[float, float]] = {
    "P1 — Small load, light dirt": (1, 1),
    "P2 — Right in the middle": (5, 5),
    "P3 — Large load, heavy dirt": (9, 9),
    "P4 — Small load, heavy dirt": (2, 8),
    "P5 — Large load, light dirt": (8, 2),
}
