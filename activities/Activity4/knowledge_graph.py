"""The ReelWave content knowledge graph (Session 8: Knowledge Representation).

Nodes: content titles, genres, and age groups.
Edges: genre_of, appropriate_for (structural), and similar_to (weighted,
used by the recommendation engine). One similar_to edge is a deliberately
planted error for students to find and fix.
"""

import networkx as nx

CONTENT = [
    ("Bunny Buddies", "Cartoon", "kids"),
    ("Sparkle Ponies", "Cartoon", "kids"),
    ("Puppy Playhouse", "Cartoon", "kids"),
    ("Space Explorers", "SciFi", "all"),
    ("Midnight Slasher", "Horror", "adult"),
    ("Haunted Manor", "Horror", "adult"),
    ("Cooking with Chef Lupe", "Cooking", "adult"),
    ("Teen Drama High", "Drama", "teen"),
    ("Comedy Nights", "Comedy", "adult"),
]

# (source, target, weight) — the recommendation engine walks these edges.
SIMILAR_TO_EDGES = [
    ("Bunny Buddies", "Midnight Slasher", 0.9),  # BUG: a kids cartoon wrongly linked to adult horror
    ("Bunny Buddies", "Sparkle Ponies", 0.8),
    ("Bunny Buddies", "Space Explorers", 0.6),
    ("Bunny Buddies", "Puppy Playhouse", 0.5),
    ("Midnight Slasher", "Haunted Manor", 0.85),
    ("Cooking with Chef Lupe", "Comedy Nights", 0.4),
    ("Teen Drama High", "Space Explorers", 0.3),
]

BUGGED_EDGE = ("Bunny Buddies", "Midnight Slasher")


def build_graph(removed_edges: set | None = None) -> nx.DiGraph:
    removed_edges = removed_edges or set()
    graph = nx.DiGraph()
    for title, genre, age in CONTENT:
        graph.add_node(title, node_type="content")
        graph.add_node(genre, node_type="genre")
        graph.add_node(age, node_type="age_group")
        graph.add_edge(title, genre, relation="genre_of")
        graph.add_edge(title, age, relation="appropriate_for")
    for src, dst, weight in SIMILAR_TO_EDGES:
        if (src, dst) in removed_edges:
            continue
        graph.add_edge(src, dst, relation="similar_to", weight=weight)
    return graph


def get_top_recommendations(graph: nx.DiGraph, seed: str, n: int = 3) -> list[tuple[str, float]]:
    candidates = [
        (target, data["weight"])
        for _, target, data in graph.out_edges(seed, data=True)
        if data.get("relation") == "similar_to"
    ]
    candidates.sort(key=lambda pair: -pair[1])
    return candidates[:n]
