"""Breadth-First Search over the professional network, plus a small
stack-based DFS used only for the optional "compare to last session" reveal.

Everything here is deterministic: same network in, same trace out, every
time. `compute_full_trace()` is computed once and then just replayed step by
step in the UI — there is no live/mutable search state to get out of sync.
"""

from collections import deque

from network_data import ADJACENCY, GOAL, START


def _describe_step(node: str, new_contacts: list[tuple[str, int]], skipped: list[str], goal_hit: bool) -> str:
    if goal_hit:
        target, _ = next(c for c in new_contacts if c[0] == GOAL)
        return f"**{node}** introduces you to **{target}** — that's the CFO! The search stops here."
    if new_contacts and skipped:
        names = ", ".join(n for n, _ in new_contacts)
        return f"**{node}** introduces you to {len(new_contacts)} new contact(s): {names}. (Also mentioned some people you already know — no need to re-add them.)"
    if new_contacts:
        names = ", ".join(n for n, _ in new_contacts)
        return f"**{node}** introduces you to {len(new_contacts)} new contact(s): {names}."
    if skipped:
        return f"**{node}** only knows people you've already reached — no new contacts here."
    return f"**{node}** has no further contacts to introduce."


def compute_full_trace(adjacency=ADJACENCY, start=START, goal=GOAL):
    """Runs queue-based Breadth-First Search and records one dict per person
    processed (dequeued).

    Algorithm (the one taught in Session 13): start a line (queue) with just
    yourself in it. Repeatedly take the person at the FRONT of the line, and
    ask them for introductions. Any contact you haven't reached before gets
    marked as reached *immediately* and joins the BACK of the line. Because
    everyone at the same "distance" joins the line before anyone farther away
    gets processed, the first time you reach the goal is guaranteed to be by
    the shortest possible chain of introductions.
    """
    visited = {start}
    level = {start: 0}
    parent = {start: None}
    discovered_order = [start]
    queue = deque([start])
    trace = []

    while queue:
        node = queue.popleft()
        new_contacts: list[tuple[str, int]] = []
        skipped: list[str] = []
        goal_hit = False

        for neighbor in adjacency.get(node, []):
            if neighbor in visited:
                skipped.append(neighbor)
                continue
            visited.add(neighbor)
            level[neighbor] = level[node] + 1
            parent[neighbor] = node
            discovered_order.append(neighbor)
            new_contacts.append((neighbor, level[neighbor]))
            queue.append(neighbor)
            if neighbor == goal:
                goal_hit = True

        trace.append(
            {
                "node": node,
                "level": level[node],
                "new_contacts": new_contacts,
                "skipped_contacts": skipped,
                "queue_after": list(queue),
                "discovered_so_far": list(discovered_order),
                "message": _describe_step(node, new_contacts, skipped, goal_hit),
            }
        )

        if goal_hit:
            break

    return trace, parent, level


FULL_TRACE, _PARENTS, _LEVELS = compute_full_trace()


def discovery_path(goal: str = GOAL) -> list[str]:
    """Walks parent pointers backward from the goal to reconstruct the
    shortest chain of introductions BFS found."""
    path = [goal]
    while _PARENTS[path[-1]] is not None:
        path.append(_PARENTS[path[-1]])
    return list(reversed(path))


def shortest_distance(goal: str = GOAL) -> int:
    return _LEVELS[goal]


def dfs_path(adjacency=ADJACENCY, start: str = START, goal: str = GOAL) -> list[str]:
    """A plain stack-based DFS (same algorithm as Activity 5's cave explorer)
    over this SAME network, used only for the optional "what would last
    session's algorithm have done here?" comparison.
    """
    stack = [(start, None)]
    visited: set[str] = set()
    parent: dict[str, str | None] = {}

    while stack:
        node, came_from = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        parent[node] = came_from
        if node == goal:
            break
        for neighbor in reversed(adjacency.get(node, [])):
            if neighbor not in visited:
                stack.append((neighbor, node))

    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return list(reversed(path))
