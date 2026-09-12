"""The Whispering Cave map (Sessions 10-12: Predicates/Recursion & Search).

A small, fixed, hand-designed cave: 10 chambers connected by tunnels. There is
no randomness anywhere in this file, so every student who runs the app gets
the exact same map and the exact same algorithm behavior.

The cave is one connected, UNDIRECTED graph: if chamber A lists chamber B as
a neighbor, chamber B also lists chamber A. It deliberately contains:
  - two dead-end branches (Underground Lake; Bottomless Pit) to demonstrate
    backtracking, and
  - one loop (Entrance - Torch Hallway - Echo Chamber - Bat Roost - Entrance)
    to demonstrate why a search algorithm must remember which chambers it
    already visited.

ADJACENCY order matters: it is the "signpost order" at each chamber, i.e. the
order in which a search algorithm considers each tunnel.
"""

START = "Entrance"
GOAL = "Treasure Room"

# node -> one-line kid-friendly description
DESCRIPTIONS = {
    "Entrance": "Where our explorer starts. Sunlight still pours in here.",
    "Torch Hallway": "A long hallway lit by old torches. Three tunnels branch off it.",
    "Bat Roost": "Sleepy bats hang from the ceiling. Two tunnels lead onward.",
    "Crystal Cavern": "Glittering crystals cover the walls. The treasure is close!",
    "Underground Lake": "Still, dark water. The tunnel just... ends here.",
    "Spider Tunnel": "Cobwebs everywhere. One tunnel keeps going.",
    "Echo Chamber": "Every whisper bounces back at you five times.",
    "Old Mine Shaft": "Rusty rail tracks from long-abandoned mining.",
    "Bottomless Pit": "The tunnel just stops at a dark, silent drop. A true dead end.",
    "Treasure Room": "X marks the spot! A chest of gold sits in the middle.",
}

# node -> "start" | "goal" | "deadend" | "normal" (used only for map coloring)
NODE_KIND = {
    "Entrance": "start",
    "Torch Hallway": "normal",
    "Bat Roost": "normal",
    "Crystal Cavern": "normal",
    "Underground Lake": "deadend",
    "Spider Tunnel": "normal",
    "Echo Chamber": "normal",
    "Old Mine Shaft": "normal",
    "Bottomless Pit": "deadend",
    "Treasure Room": "goal",
}

# Undirected adjacency list, in signpost order.
ADJACENCY = {
    "Entrance": ["Bat Roost", "Torch Hallway"],
    "Torch Hallway": ["Entrance", "Crystal Cavern", "Underground Lake", "Echo Chamber"],
    "Bat Roost": ["Entrance", "Spider Tunnel", "Echo Chamber"],
    "Crystal Cavern": ["Torch Hallway", "Treasure Room"],
    "Underground Lake": ["Torch Hallway"],
    "Spider Tunnel": ["Bat Roost", "Old Mine Shaft"],
    "Echo Chamber": ["Torch Hallway", "Bat Roost"],
    "Old Mine Shaft": ["Spider Tunnel", "Bottomless Pit"],
    "Bottomless Pit": ["Old Mine Shaft"],
    "Treasure Room": ["Crystal Cavern"],
}


def undirected_edges() -> list[tuple[str, str]]:
    """Each tunnel exactly once, as (a, b) with a < b alphabetically."""
    seen = set()
    edges = []
    for node, neighbors in ADJACENCY.items():
        for neighbor in neighbors:
            pair = tuple(sorted((node, neighbor)))
            if pair not in seen:
                seen.add(pair)
                edges.append(pair)
    return edges
