"""Greedy Best-First Search and A* Search over the YucaExpress delivery map.

Both algorithms keep a priority queue of roads to try next; they differ only
in what they use as the priority:

  - Greedy Best-First orders purely by h(n) — "how close does this look to
    the destination, as the crow flies?" It never reconsiders a road once a
    junction has been reached.
  - A* orders by f(n) = g(n) + h(n) — the real distance already driven,
    PLUS the straight-line estimate of what's left. If a cheaper way to
    reach an already-known junction is found later, A* updates it.

Everything here is deterministic: same map in, same trace out, every time.
`GREEDY_TRACE` / `ASTAR_TRACE` are computed once and then just replayed step
by step in the UI.
"""

import heapq

from map_data import ADJACENCY, GOAL, ROAD_COST, START, heuristic


def _run(mode: str, start: str = START, goal: str = GOAL):
    assert mode in ("greedy", "astar")

    g_cost = {start: 0.0}
    parent = {start: None}
    closed: set[str] = set()
    pq: list[tuple[float, str]] = [(heuristic(start, goal), start)]
    trace = []

    while pq:
        priority, node = heapq.heappop(pq)

        if node in closed:
            trace.append(
                {
                    "action": "skip",
                    "node": node,
                    "priority": round(priority, 2),
                    "new_frontier": [],
                    "skipped": [],
                    "frontier_after": sorted(pq),
                    "message": f"We already settled the fastest way to **{node}** — skip this duplicate.",
                }
            )
            continue

        closed.add(node)
        is_goal = node == goal
        new_frontier = []
        skipped = []

        if not is_goal:
            for neighbor in ADJACENCY[node]:
                if neighbor in closed:
                    skipped.append(neighbor)
                    continue

                tentative_g = g_cost[node] + ROAD_COST[(node, neighbor)]
                already_known = neighbor in g_cost

                if mode == "greedy" and already_known:
                    # Greedy never reconsiders a junction it has already queued.
                    skipped.append(neighbor)
                    continue
                if mode == "astar" and already_known and tentative_g >= g_cost[neighbor]:
                    # A* only updates a junction if this route to it is cheaper.
                    skipped.append(neighbor)
                    continue

                g_cost[neighbor] = tentative_g
                parent[neighbor] = node
                h = heuristic(neighbor, goal)
                f = round(tentative_g + h, 2)
                p = h if mode == "greedy" else f
                heapq.heappush(pq, (p, neighbor))
                new_frontier.append({"node": neighbor, "g": round(tentative_g, 2), "h": h, "f": f})

        g_here = round(g_cost[node], 2)
        h_here = heuristic(node, goal)
        f_here = round(g_here + h_here, 2)

        if is_goal:
            message = f"**{node} reached!** Total distance driven: **{g_here} km**."
        elif new_frontier:
            names = ", ".join(f"{c['node']}" for c in new_frontier)
            message = f"From **{node}**, we can now reach: {names}."
        else:
            message = f"**{node}** has no new roads to offer — every road from here leads somewhere already settled."

        trace.append(
            {
                "action": "goal" if is_goal else "expand",
                "node": node,
                "priority": round(priority, 2),
                "g": g_here,
                "h": h_here,
                "f": f_here,
                "new_frontier": new_frontier,
                "skipped": skipped,
                "frontier_after": sorted(pq),
                "message": message,
            }
        )

        if is_goal:
            break

    return trace, parent, g_cost


def _discovery_path(parent: dict, goal: str = GOAL) -> list[str]:
    path = [goal]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return list(reversed(path))


GREEDY_TRACE, _GREEDY_PARENTS, _GREEDY_G = _run("greedy")
ASTAR_TRACE, _ASTAR_PARENTS, _ASTAR_G = _run("astar")

GREEDY_PATH = _discovery_path(_GREEDY_PARENTS)
ASTAR_PATH = _discovery_path(_ASTAR_PARENTS)
GREEDY_COST = round(_GREEDY_G[GOAL], 2)
ASTAR_COST = round(_ASTAR_G[GOAL], 2)
