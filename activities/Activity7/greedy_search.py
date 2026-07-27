"""
Greedy Best-First Search Implementation
========================================
This module implements Greedy Best-First Search for searching nodes in a
weighted directed graph based on node properties.

Greedy Best-First Search uses a heuristic function to prioritize which nodes
to explore next, always choosing the node that appears closest to the goal.

Usage:
    python greedy_search.py <graph_size> <search_property> <search_value>

    graph_size: small, medium, or large
    search_property: type, region, capacity_min, priority
    search_value: value to search for

Examples:
    python greedy_search.py small type warehouse
    python greedy_search.py medium region north
    python greedy_search.py large capacity_min 3000

Author: AI Course Materials
Date: February 2026
"""

import json
import sys
import time
import heapq
import math


def load_graph(filename):
    """
    Load graph from JSON file.

    Args:
        filename (str): Path to JSON graph file

    Returns:
        dict: Graph structure with nodes and edges
    """
    try:
        with open(filename, 'r') as f:
            graph = json.load(f)
        return graph
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Please run graph_generator.py first to create graph files.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not valid JSON!")
        sys.exit(1)


def build_adjacency_list(graph):
    """
    Build adjacency list representation from graph data.

    Args:
        graph (dict): Graph structure

    Returns:
        dict: Adjacency list {node_id: [list of neighbor node_ids]}
    """
    adjacency_list = {node_id: [] for node_id in graph["nodes"].keys()}

    for edge in graph["edges"]:
        source = edge["source"]
        target = edge["target"]
        adjacency_list[source].append(target)

    return adjacency_list


def matches_search_criteria(node, search_property, search_value):
    """
    Check if a node matches the search criteria.

    Args:
        node (dict): Node data
        search_property (str): Property to search by
        search_value (str): Value to match

    Returns:
        bool: True if node matches criteria
    """
    if search_property == "type":
        return node["type"] == search_value

    elif search_property == "region":
        return node["region"] == search_value

    elif search_property == "capacity_min":
        try:
            min_capacity = int(search_value)
            return node["capacity"] >= min_capacity
        except ValueError:
            print(f"Error: capacity_min requires an integer value")
            return False

    elif search_property == "capacity_max":
        try:
            max_capacity = int(search_value)
            return node["capacity"] <= max_capacity
        except ValueError:
            print(f"Error: capacity_max requires an integer value")
            return False

    elif search_property == "priority":
        try:
            priority = int(search_value)
            return node["priority"] == priority
        except ValueError:
            print(f"Error: priority requires an integer value")
            return False

    else:
        print(f"Error: Unknown search property '{search_property}'")
        return False


def calculate_heuristic(node, search_property, search_value, graph):
    """
    Calculate heuristic value for Greedy Best-First Search.

    The heuristic estimates how "close" a node is to matching our search criteria.
    Lower values indicate nodes that are more likely to lead to matching nodes.

    Heuristic Design:
    - For type/region: use spatial distance to center of matching nodes
    - For capacity: use absolute difference from target capacity
    - For priority: use absolute difference from target priority

    Args:
        node (dict): Current node
        search_property (str): Property being searched
        search_value (str): Target value
        graph (dict): Full graph structure

    Returns:
        float: Heuristic value (lower is better)
    """

    # If we're searching for categorical properties (type, region),
    # use spatial proximity to guide search
    if search_property in ["type", "region"]:
        # Calculate center of mass for all matching nodes
        matching_nodes = [
            n for n in graph["nodes"].values()
            if matches_search_criteria(n, search_property, search_value)
        ]

        if matching_nodes:
            # Calculate average coordinates of matching nodes
            avg_x = sum(n["coordinates"]["x"] for n in matching_nodes) / len(matching_nodes)
            avg_y = sum(n["coordinates"]["y"] for n in matching_nodes) / len(matching_nodes)

            # Calculate Euclidean distance from current node to this center
            dx = node["coordinates"]["x"] - avg_x
            dy = node["coordinates"]["y"] - avg_y
            distance = math.sqrt(dx**2 + dy**2)

            return distance
        else:
            # No matching nodes found yet, use distance from origin
            return math.sqrt(
                node["coordinates"]["x"]**2 +
                node["coordinates"]["y"]**2
            )

    # For numerical properties (capacity, priority), use value difference
    elif search_property == "capacity_min":
        target_capacity = int(search_value)
        # Lower heuristic for nodes closer to target capacity
        return abs(node["capacity"] - target_capacity)

    elif search_property == "capacity_max":
        target_capacity = int(search_value)
        return abs(node["capacity"] - target_capacity)

    elif search_property == "priority":
        target_priority = int(search_value)
        # Multiply by 1000 to make priority differences more significant
        return abs(node["priority"] - target_priority) * 1000

    else:
        # Default: no heuristic guidance
        return 0


def greedy_search(graph, start_node_id, search_property, search_value):
    """
    Perform Greedy Best-First Search to find all nodes matching criteria.

    Greedy Best-First Search Algorithm:
    1. Start from a given node
    2. Always explore the node with the lowest heuristic value next
    3. Use a priority queue (min-heap) to efficiently get the best node
    4. Track visited nodes to avoid cycles

    Unlike BFS which explores level-by-level, Greedy Best-First Search
    "greedily" pursues the most promising direction based on the heuristic.

    Args:
        graph (dict): Graph structure
        start_node_id (str): Starting node ID
        search_property (str): Property to search by
        search_value (str): Value to match

    Returns:
        tuple: (found_nodes, nodes_explored, time_taken)
            found_nodes (list): List of node IDs that match criteria
            nodes_explored (int): Total number of nodes explored
            time_taken (float): Time in seconds
    """

    start_time = time.time()

    # Build adjacency list for efficient neighbor lookup
    adjacency_list = build_adjacency_list(graph)

    # Initialize Greedy Best-First Search data structures
    # Priority queue: stores (heuristic_value, node_id)
    # Python's heapq implements a min-heap (lowest value has highest priority)
    start_node = graph["nodes"][start_node_id]
    start_heuristic = calculate_heuristic(start_node, search_property, search_value, graph)

    priority_queue = [(start_heuristic, start_node_id)]
    visited = set([start_node_id])  # Track visited nodes
    found_nodes = []  # Nodes that match search criteria
    nodes_explored = 0  # Counter for performance analysis

    # Check if start node matches criteria
    if matches_search_criteria(start_node, search_property, search_value):
        found_nodes.append(start_node_id)

    # Greedy Best-First Search main loop
    while priority_queue:
        # Get node with lowest heuristic value (most promising)
        _, current_node_id = heapq.heappop(priority_queue)
        nodes_explored += 1

        # Get all neighbors of current node
        neighbors = adjacency_list.get(current_node_id, [])

        # Explore each neighbor
        for neighbor_id in neighbors:
            # Only visit if not already visited (prevents cycles)
            if neighbor_id not in visited:
                visited.add(neighbor_id)

                # Calculate heuristic for this neighbor
                neighbor_node = graph["nodes"][neighbor_id]
                heuristic = calculate_heuristic(
                    neighbor_node, search_property, search_value, graph
                )

                # Add to priority queue with its heuristic value
                heapq.heappush(priority_queue, (heuristic, neighbor_id))

                # Check if neighbor matches search criteria
                if matches_search_criteria(neighbor_node, search_property, search_value):
                    found_nodes.append(neighbor_id)

    end_time = time.time()
    time_taken = end_time - start_time

    return found_nodes, nodes_explored, time_taken


def greedy_search_all_components(graph, search_property, search_value):
    """
    Perform Greedy Best-First Search across all connected components.

    This ensures we search the entire graph even if it's not fully connected.

    Args:
        graph (dict): Graph structure
        search_property (str): Property to search by
        search_value (str): Value to match

    Returns:
        tuple: (found_nodes, nodes_explored, time_taken)
    """
    start_time = time.time()

    adjacency_list = build_adjacency_list(graph)
    all_node_ids = list(graph["nodes"].keys())

    visited_global = set()
    found_nodes = []
    total_nodes_explored = 0

    # Iterate through all nodes to handle disconnected components
    for start_node_id in all_node_ids:
        if start_node_id in visited_global:
            continue

        # Greedy Best-First Search from this starting node
        start_node = graph["nodes"][start_node_id]
        start_heuristic = calculate_heuristic(
            start_node, search_property, search_value, graph
        )

        priority_queue = [(start_heuristic, start_node_id)]
        visited_global.add(start_node_id)

        # Check start node
        if matches_search_criteria(start_node, search_property, search_value):
            if start_node_id not in found_nodes:
                found_nodes.append(start_node_id)

        # Greedy search loop
        while priority_queue:
            _, current_node_id = heapq.heappop(priority_queue)
            total_nodes_explored += 1

            neighbors = adjacency_list.get(current_node_id, [])

            for neighbor_id in neighbors:
                if neighbor_id not in visited_global:
                    visited_global.add(neighbor_id)

                    neighbor_node = graph["nodes"][neighbor_id]
                    heuristic = calculate_heuristic(
                        neighbor_node, search_property, search_value, graph
                    )

                    heapq.heappush(priority_queue, (heuristic, neighbor_id))

                    if matches_search_criteria(neighbor_node, search_property, search_value):
                        if neighbor_id not in found_nodes:
                            found_nodes.append(neighbor_id)

    end_time = time.time()
    time_taken = end_time - start_time

    return found_nodes, total_nodes_explored, time_taken


def display_results(found_nodes, nodes_explored, time_taken, graph, search_property, search_value):
    """
    Display search results in a formatted manner.

    Args:
        found_nodes (list): Node IDs that match criteria
        nodes_explored (int): Total nodes explored
        time_taken (float): Time in seconds
        graph (dict): Graph structure
        search_property (str): Property searched
        search_value (str): Value searched for
    """
    print("\n" + "="*70)
    print("GREEDY BEST-FIRST SEARCH RESULTS")
    print("="*70)
    print(f"Graph: {graph['metadata']['graph_type']} ({graph['metadata']['num_nodes']} nodes)")
    print(f"Search Property: {search_property}")
    print(f"Search Value: {search_value}")
    print(f"Nodes Explored: {nodes_explored}")
    print(f"Nodes Found: {len(found_nodes)}")
    print(f"Time Taken: {time_taken:.6f} seconds")
    print("="*70)

    if found_nodes:
        print(f"\nFound {len(found_nodes)} matching nodes:")
        # Display first 10 matches
        display_limit = min(10, len(found_nodes))
        for i, node_id in enumerate(found_nodes[:display_limit]):
            node = graph["nodes"][node_id]
            print(f"  {i+1}. {node['name']} (ID: {node_id})")
            print(f"      Type: {node['type']}, Region: {node['region']}, " +
                  f"Capacity: {node['capacity']}, Priority: {node['priority']}")

        if len(found_nodes) > display_limit:
            print(f"  ... and {len(found_nodes) - display_limit} more")
    else:
        print("\nNo nodes found matching the search criteria.")

    print()


def main():
    """
    Main function to run Greedy Best-First Search from command line.
    """
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: python greedy_search.py <graph_size> <search_property> <search_value>")
        print()
        print("Arguments:")
        print("  graph_size: small, medium, or large")
        print("  search_property: type, region, capacity_min, capacity_max, or priority")
        print("  search_value: value to search for")
        print()
        print("Examples:")
        print("  python greedy_search.py small type warehouse")
        print("  python greedy_search.py medium region north")
        print("  python greedy_search.py large capacity_min 3000")
        print("  python greedy_search.py small priority 5")
        sys.exit(1)

    # Parse arguments
    graph_size = sys.argv[1].lower()
    search_property = sys.argv[2].lower()
    search_value = sys.argv[3]

    # Validate graph size
    if graph_size not in ["small", "medium", "large"]:
        print(f"Error: Invalid graph size '{graph_size}'")
        print("Valid options: small, medium, large")
        sys.exit(1)

    # Determine filename
    filename = f"graph_{graph_size}.json"

    # Load graph
    print(f"Loading graph from {filename}...")
    graph = load_graph(filename)
    print(f"Loaded graph with {graph['metadata']['num_nodes']} nodes " +
          f"and {graph['metadata']['num_edges']} edges")

    # Perform Greedy Best-First Search across all components
    print(f"\nSearching for nodes where {search_property} = {search_value}...")
    print("Using Greedy Best-First Search with heuristic guidance...")
    found_nodes, nodes_explored, time_taken = greedy_search_all_components(
        graph, search_property, search_value
    )

    # Display results
    display_results(found_nodes, nodes_explored, time_taken, graph, search_property, search_value)


if __name__ == "__main__":
    main()
