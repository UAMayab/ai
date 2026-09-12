"""The Mamdani-style fuzzy inference pipeline: Fuzzification -> Inference ->
Defuzzification (Session 17's four key elements, minus the rule base itself,
which lives in fuzzy_data.py).

Everything here is a pure function of its numeric inputs — there is no
randomness, so the same (load, dirt) pair always produces the exact same
result.
"""

from fuzzy_data import DIRT_TERMS, LOAD_TERMS, OUTPUT_CENTERS, RULES


def fuzzify(load: float, dirt: float) -> tuple[dict[str, float], dict[str, float]]:
    """Step 1: turn crisp Load/Dirt numbers into a degree of membership
    (0 to 1) in each linguistic term."""
    load_degrees = {name: fn(load) for name, fn in LOAD_TERMS.items()}
    dirt_degrees = {name: fn(dirt) for name, fn in DIRT_TERMS.items()}
    return load_degrees, dirt_degrees


def evaluate_rules(load_degrees: dict[str, float], dirt_degrees: dict[str, float]) -> list[dict]:
    """Step 2 (Inference): every rule's firing strength is the MIN of its two
    antecedents' membership degrees (fuzzy AND)."""
    fired = []
    for load_term, dirt_term, time_term in RULES:
        strength = min(load_degrees[load_term], dirt_degrees[dirt_term])
        fired.append(
            {
                "load_term": load_term,
                "dirt_term": dirt_term,
                "time_term": time_term,
                "strength": strength,
            }
        )
    return fired


def aggregate(fired_rules: list[dict]) -> dict[str, float]:
    """Step 3: for each output term, take the MAX firing strength among all
    rules that conclude that term (fuzzy OR across rules)."""
    aggregated = {term: 0.0 for term in OUTPUT_CENTERS}
    for rule in fired_rules:
        term = rule["time_term"]
        aggregated[term] = max(aggregated[term], rule["strength"])
    return aggregated


def defuzzify(aggregated: dict[str, float]) -> float:
    """Step 4: the weighted-average defuzzification method named in the
    course material — each output term's representative crisp value,
    weighted by how strongly that term was activated."""
    total_strength = sum(aggregated.values())
    if total_strength == 0:
        return 0.0
    weighted_sum = sum(aggregated[term] * OUTPUT_CENTERS[term] for term in aggregated)
    return weighted_sum / total_strength


def run(load: float, dirt: float) -> dict:
    """Runs the full pipeline and returns every intermediate result, for
    display and grading."""
    load_degrees, dirt_degrees = fuzzify(load, dirt)
    fired_rules = evaluate_rules(load_degrees, dirt_degrees)
    aggregated = aggregate(fired_rules)
    wash_time = defuzzify(aggregated)
    return {
        "load": load,
        "dirt": dirt,
        "load_degrees": load_degrees,
        "dirt_degrees": dirt_degrees,
        "fired_rules": fired_rules,
        "aggregated": aggregated,
        "wash_time": round(wash_time, 2),
    }
