"""The YucaExpress delivery map (Session 14: Heuristic Search).

A small, fixed, hand-designed street network for a fictional last-mile
delivery courier in Mérida. There is no randomness anywhere in this file, so
every student who runs the app gets the exact same map and the exact same
algorithm behavior.

Every node has real (x, y) coordinates (in kilometers), so the heuristic
h(n) = straight-line distance from n to the Client's office is a genuine,
computable number, not just a made-up estimate. Every road's real cost is
set to be AT LEAST its straight-line length (most roads equal it exactly;
one — the lakeshore road — is deliberately a long detour). This guarantees
the straight-line heuristic never overestimates the true remaining cost,
which is exactly the "admissible heuristic" condition A* depends on.
"""

import math

START = "Depot"
GOAL = "Client Office"

# node -> (x, y) in kilometers on a simple city grid
COORDINATES = {
    "Depot": (0, 0),
    "Hub Norte": (3, 2),
    "Hub Sur": (2, -2),
    "Parque Cruce": (5, 3),
    "Retorno del Lago": (9, 3),
    "Anillo Periferico": (5, -2),
    "Circuito Sur": (8, -1),
    "Client Office": (10, 0),
}

DESCRIPTIONS = {
    "Depot": "The YucaExpress warehouse. Your delivery starts here.",
    "Hub Norte": "A northern transfer hub.",
    "Hub Sur": "A southern transfer hub.",
    "Parque Cruce": "A crossing next to Parque de las Américas.",
    "Retorno del Lago": "A scenic turnaround right by the lake — tantalizingly close to the client's office as the crow flies.",
    "Anillo Periferico": "A ring-road junction to the south.",
    "Circuito Sur": "The last junction before the client's neighborhood.",
    "Client Office": "Your delivery destination.",
}

NODE_KIND = {
    "Depot": "start",
    "Hub Norte": "normal",
    "Hub Sur": "normal",
    "Parque Cruce": "normal",
    "Retorno del Lago": "normal",
    "Anillo Periferico": "normal",
    "Circuito Sur": "normal",
    "Client Office": "goal",
}


def _euclid(a: str, b: str) -> float:
    (x1, y1), (x2, y2) = COORDINATES[a], COORDINATES[b]
    return math.hypot(x2 - x1, y2 - y1)


# (node_a, node_b, cost_multiplier) — multiplier is 1.0 for a direct road,
# and > 1.0 for a road that winds around an obstacle (here: the lake).
_RAW_ROADS = [
    ("Depot", "Hub Norte", 1.0),
    ("Depot", "Hub Sur", 1.0),
    ("Hub Norte", "Parque Cruce", 1.0),
    ("Parque Cruce", "Retorno del Lago", 1.0),
    ("Retorno del Lago", "Client Office", 3.0),  # long way around the lake
    ("Hub Sur", "Anillo Periferico", 1.0),
    ("Anillo Periferico", "Circuito Sur", 1.0),
    ("Circuito Sur", "Client Office", 1.0),
    ("Parque Cruce", "Anillo Periferico", 1.0),
]

ADJACENCY: dict[str, list[str]] = {n: [] for n in COORDINATES}
ROAD_COST: dict[tuple[str, str], float] = {}
for _a, _b, _mult in _RAW_ROADS:
    _cost = round(_euclid(_a, _b) * _mult, 2)
    ADJACENCY[_a].append(_b)
    ADJACENCY[_b].append(_a)
    ROAD_COST[(_a, _b)] = _cost
    ROAD_COST[(_b, _a)] = _cost


def heuristic(node: str, goal: str = GOAL) -> float:
    """Straight-line ('as the crow flies') distance from node to goal, in km."""
    return round(_euclid(node, goal), 2)


def undirected_edges() -> list[tuple[str, str, float]]:
    """Each road exactly once, as (a, b, cost)."""
    seen = set()
    edges = []
    for (a, b), cost in ROAD_COST.items():
        pair = tuple(sorted((a, b)))
        if pair not in seen:
            seen.add(pair)
            edges.append((pair[0], pair[1], cost))
    return edges
