"""The ShopSmart inference engine (Session 15: Expert Systems).

This is a "direct inference engine" in the sense the course material
describes: it checks each rule, one at a time, against the known facts (a
profile), and activates any rule whose conditions are fully satisfied. There
is no randomness and no hidden state — the same profile always produces the
exact same trace.
"""

from rules_data import PROFILES, RULES


def evaluate_profile(profile_name: str) -> list[dict]:
    """Checks every rule against one profile's facts and returns one dict per
    rule: whether it fired, the per-condition breakdown, and its conclusion.
    """
    facts = PROFILES[profile_name]
    results = []

    for rule in RULES:
        condition_results = []
        for fact_name, comparison_text, check in rule["conditions"]:
            actual_value = facts[fact_name]
            holds = bool(check(actual_value))
            condition_results.append(
                {
                    "fact": fact_name,
                    "comparison": comparison_text,
                    "actual_value": actual_value,
                    "holds": holds,
                }
            )

        fired = all(c["holds"] for c in condition_results)

        results.append(
            {
                "id": rule["id"],
                "name": rule["name"],
                "department": rule["department"],
                "text": rule["text"],
                "condition_results": condition_results,
                "fired": fired,
                "conclusion": rule["conclusion"] if fired else None,
            }
        )

    return results


def fired_conclusions(profile_name: str) -> list[str]:
    return [r["conclusion"] for r in evaluate_profile(profile_name) if r["fired"]]
