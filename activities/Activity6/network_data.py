"""The Meridian professional network (Session 13: Breadth-First Search).

A small, fixed, hand-designed network of professional contacts. There is no
randomness anywhere in this file, so every student who runs the app gets the
exact same network and the exact same algorithm behavior.

The network is one connected, UNDIRECTED graph ("knows" is a two-way
relationship). It deliberately contains:
  - one weak-tie dead end (Diego Torres has only one contact) to show that
    not every connection leads somewhere new, and
  - two overlapping loops (You-Marco-Valentina-Sofia-You, and
    Valentina-Camila-Roberto-Sofia-Valentina) to show why a search algorithm
    must remember who it has already reached.

ADJACENCY order matters: it is the order in which each person would make
introductions, i.e. the order a search algorithm considers each contact.
"""

START = "You"
GOAL = "Elena Ruiz"

# node -> one-line business description
DESCRIPTIONS = {
    "You": "Business Development Associate at Meridian Consulting Group. This is where your search starts.",
    "Marco Aguilar": "Senior Account Manager at Meridian. One of your closest work contacts.",
    "Sofia Chan": "Marketing Director at Meridian. Knows people across several client accounts.",
    "Diego Torres": "Operations Lead at Meridian. Friendly, but his network doesn't extend beyond Marco.",
    "Valentina Cruz": "Alumni Network Coordinator. A natural connector between different circles.",
    "Roberto Kim": "Regional Sales VP at a partner firm.",
    "Camila Duarte": "Independent Consultant who works with several manufacturing clients.",
    "Javier Mendez": "Procurement Manager at Grupo Katún.",
    "Ana Beltran": "Executive Assistant to the CFO at Grupo Katún.",
    "Elena Ruiz": "CFO of Grupo Katún — the decision-maker you're ultimately trying to reach.",
}

# node -> "start" | "goal" | "deadend" | "normal" (used only for map coloring)
NODE_KIND = {
    "You": "start",
    "Marco Aguilar": "normal",
    "Sofia Chan": "normal",
    "Diego Torres": "deadend",
    "Valentina Cruz": "normal",
    "Roberto Kim": "normal",
    "Camila Duarte": "normal",
    "Javier Mendez": "normal",
    "Ana Beltran": "normal",
    "Elena Ruiz": "goal",
}

# Undirected adjacency list, in introduction order.
ADJACENCY = {
    "You": ["Marco Aguilar", "Sofia Chan"],
    "Marco Aguilar": ["You", "Diego Torres", "Valentina Cruz"],
    "Sofia Chan": ["You", "Roberto Kim", "Valentina Cruz"],
    "Diego Torres": ["Marco Aguilar"],
    "Valentina Cruz": ["Marco Aguilar", "Sofia Chan", "Camila Duarte"],
    "Roberto Kim": ["Sofia Chan", "Camila Duarte"],
    "Camila Duarte": ["Valentina Cruz", "Roberto Kim", "Javier Mendez"],
    "Javier Mendez": ["Camila Duarte", "Ana Beltran"],
    "Ana Beltran": ["Javier Mendez", "Elena Ruiz"],
    "Elena Ruiz": ["Ana Beltran"],
}


def undirected_edges() -> list[tuple[str, str]]:
    """Each professional connection exactly once, as (a, b) sorted alphabetically."""
    seen = set()
    edges = []
    for node, neighbors in ADJACENCY.items():
        for neighbor in neighbors:
            pair = tuple(sorted((node, neighbor)))
            if pair not in seen:
                seen.add(pair)
                edges.append(pair)
    return edges
