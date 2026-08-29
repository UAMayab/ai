"""A tiny fact/rule/query engine (Session 9: Prolog terminology).

This is NOT real Prolog — it is a hand-built, transparent stand-in that
exposes the same core ideas (facts, rules, queries, inference) without
requiring students to install SWI-Prolog.

Rule (in Prolog-like notation, for display to students):

    suspect(X) :- has_access(X, knowledge_graph),
                  edited_at(X, Time),
                  overnight(Time).
"""

SUSPECTS = ["etl_script", "recommendation_model", "content_editor", "cache_server"]

FACTS = {
    "has_access": {"etl_script", "recommendation_model", "content_editor", "cache_server"},
    "edited_at": {"etl_script": "03:14", "content_editor": "14:00"},
}


def is_overnight(time_str: str) -> bool:
    hour = int(time_str.split(":")[0])
    return 0 <= hour <= 5


def query(suspect: str, extra_edited_at: dict | None = None) -> tuple[bool, list[str]]:
    """Runs the suspect(X) rule for one suspect, given the base facts plus
    any extra edited_at facts the student has added. Returns (verdict, trace).
    """
    edited_at = dict(FACTS["edited_at"])
    if extra_edited_at:
        edited_at.update(extra_edited_at)

    trace = [f"?- suspect({suspect})."]

    has_access = suspect in FACTS["has_access"]
    trace.append(f"has_access({suspect}, knowledge_graph) = {has_access}")
    if not has_access:
        trace.append("Rule requires has_access(X, knowledge_graph) — FAILED.")
        trace.append(f"VERDICT: {suspect} is NOT GUILTY (no access).")
        return False, trace

    time_str = edited_at.get(suspect)
    if time_str is None:
        trace.append(f"edited_at({suspect}, Time) — no matching fact found.")
        trace.append("Rule requires edited_at(X, Time) — FAILED (no evidence).")
        trace.append(f"VERDICT: {suspect} is NOT GUILTY (insufficient evidence).")
        return False, trace

    trace.append(f"edited_at({suspect}, {time_str}) = True")
    overnight = is_overnight(time_str)
    trace.append(f"overnight({time_str}) = {overnight}")
    if not overnight:
        trace.append("Rule requires overnight(Time) — FAILED.")
        trace.append(f"VERDICT: {suspect} is NOT GUILTY (edit was not made overnight).")
        return False, trace

    trace.append(f"All conditions of suspect(X) satisfied for X = {suspect}.")
    trace.append(f"VERDICT: {suspect} is GUILTY.")
    return True, trace
