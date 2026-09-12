"""The business-trip packing problem (Session 16: Genetic Algorithms).

A small, fixed Knapsack problem: which items should go in an 8 kg carry-on
so the total "usefulness" (value) is as high as possible without going over
the weight limit? There is no randomness in this file — the item list and
capacity never change.
"""

# (item name, weight in kg, value/usefulness score 1-10)
ITEMS: list[tuple[str, int, int]] = [
    ("Laptop", 3, 9),
    ("Charger", 1, 5),
    ("Suit", 2, 6),
    ("Dress Shoes", 2, 4),
    ("Umbrella", 1, 2),
    ("Camera", 2, 7),
    ("Client Gift", 2, 8),
    ("Snacks", 1, 2),
]

CAPACITY_KG = 8

NUM_ITEMS = len(ITEMS)


def weight_and_value(chromosome: tuple[int, ...]) -> tuple[int, int]:
    """A chromosome is a tuple of 0/1, one bit per item (1 = pack it)."""
    weight = sum(bit * ITEMS[i][1] for i, bit in enumerate(chromosome))
    value = sum(bit * ITEMS[i][2] for i, bit in enumerate(chromosome))
    return weight, value


def fitness(chromosome: tuple[int, ...]) -> int:
    """Total value if the bag isn't overweight, otherwise 0 (discarded) —
    matches the course's description: 'individuals who exceed the capacity
    of the backpack are discarded.'
    """
    weight, value = weight_and_value(chromosome)
    return value if weight <= CAPACITY_KG else 0


def packed_items(chromosome: tuple[int, ...]) -> list[str]:
    return [ITEMS[i][0] for i, bit in enumerate(chromosome) if bit]
