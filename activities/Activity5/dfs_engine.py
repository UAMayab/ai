"""Depth-First Search over the cave map, plus a tiny recursive
fact/rule engine for Session 10 (predicates & recursion).

Everything here is deterministic: same cave map in, same trace out, every
time. `compute_full_trace()` is computed once and then just replayed step by
step in the UI — there is no live/mutable search state to get out of sync.
"""

from cave_data import ADJACENCY, GOAL, START


def slug(name: str) -> str:
    """'Bat Roost' -> 'bat_roost', for Prolog-style display."""
    return name.lower().replace(" ", "_")


# --------------------------------------------------------------------------
# Part 1 (Session 12): the full, precomputed Depth-First Search trace
# --------------------------------------------------------------------------

def compute_full_trace(adjacency=ADJACENCY, start=START, goal=GOAL) -> list[dict]:
    """Runs iterative, stack-based DFS and records one dict per stack-pop.

    Algorithm (the one taught in Session 12): push the start chamber; then
    repeatedly pop a chamber off the stack. If we've already visited it,
    skip it (this is what stops the algorithm from looping forever around a
    cycle). Otherwise mark it visited, and push its neighbors (in reverse
    signpost order, so the first-listed neighbor is explored first). Stop as
    soon as the goal chamber is actually visited.
    """
    stack = [(start, None)]  # (chamber, chamber_that_led_here)
    visited_set: set[str] = set()
    visited_order: list[str] = []
    trace = []

    while stack:
        node, parent = stack.pop()

        if node in visited_set:
            trace.append(
                {
                    "action": "skip",
                    "node": node,
                    "parent": parent,
                    "stack_after": [n for n, _ in stack],
                    "visited_after": list(visited_order),
                    "message": (
                        f"We're back at **{node}**, but it's already explored — "
                        "skip it and keep backtracking."
                    ),
                }
            )
            continue

        visited_set.add(node)
        visited_order.append(node)
        is_goal = node == goal

        neighbors = adjacency.get(node, [])
        if is_goal:
            # Found it — stop immediately, don't bother exploring past the goal.
            new_neighbors = []
            message = f"**TREASURE FOUND** at {node}! The search stops right here."
        else:
            for neighbor in reversed(neighbors):
                stack.append((neighbor, node))
            new_neighbors = [n for n in neighbors if n not in visited_set]
            if not new_neighbors:
                message = f"**{node}** is a dead end — nowhere new to go. Time to backtrack!"
            else:
                message = f"New chamber! We step into **{node}** for the first time and peek down its tunnels."

        trace.append(
            {
                "action": "goal" if is_goal else "visit",
                "node": node,
                "parent": parent,
                "stack_after": [n for n, _ in stack],
                "visited_after": list(visited_order),
                "message": message,
            }
        )

        if is_goal:
            break

    return trace


FULL_TRACE = compute_full_trace()


def discovery_path(trace: list[dict] = FULL_TRACE, goal: str = GOAL) -> list[str]:
    """Walks parent pointers backward from the goal to reconstruct the exact
    path DFS actually used to reach it (which may not be the shortest one!).
    """
    parents = {step["node"]: step["parent"] for step in trace if step["action"] in ("visit", "goal")}
    path = [goal]
    while parents[path[-1]] is not None:
        path.append(parents[path[-1]])
    return list(reversed(path))


# --------------------------------------------------------------------------
# Part 2 (Session 11): brute-force enumeration of the whole search space
# --------------------------------------------------------------------------

def enumerate_all_paths(start: str = START, goal: str = GOAL) -> list[list[str]]:
    """All simple (no-repeated-chamber) paths from start to goal."""
    results: list[list[str]] = []

    def backtrack(current: str, path: list[str], visited: set[str]):
        if current == goal:
            results.append(list(path))
            return
        for neighbor in ADJACENCY.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                backtrack(neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)

    backtrack(start, [start], {start})
    results.sort(key=len)
    return results


# --------------------------------------------------------------------------
# Part 3 (Session 10): facts, rules, and a recursive query
# --------------------------------------------------------------------------

def query_reachable(start: str, goal: str) -> tuple[bool, list[str]]:
    """Mirrors this recursive rule:

        reachable(X, Y) :- tunnel(X, Y).
        reachable(X, Y) :- tunnel(X, Z), reachable(Z, Y).

    Returns (True/False, a step-by-step derivation trace). This is the same
    depth-first exploration idea as Session 12, just phrased as logic rules
    instead of a stack.
    """
    trace = [f"?- reachable({slug(start)}, {slug(goal)})."]
    visited: set[str] = set()

    def search(current: str, depth: int) -> list[str] | None:
        indent = "  " * depth
        visited.add(current)
        if current == goal:
            trace.append(f"{indent}tunnel(_, {slug(goal)}) reached — base case of the rule is satisfied.")
            return [current]
        for neighbor in ADJACENCY.get(current, []):
            if neighbor in visited:
                continue
            trace.append(
                f"{indent}tunnel({slug(current)}, {slug(neighbor)}) is true — trying "
                f"reachable({slug(neighbor)}, {slug(goal)})..."
            )
            result = search(neighbor, depth + 1)
            if result is not None:
                return [current] + result
        trace.append(f"{indent}no more untried tunnels from {slug(current)} — this branch fails.")
        return None

    result = search(start, 0)
    if result is not None:
        trace.append(f"VERDICT: reachable({slug(start)}, {slug(goal)}) = TRUE.")
    else:
        trace.append(f"VERDICT: reachable({slug(start)}, {slug(goal)}) = FALSE.")
    return result is not None, trace
