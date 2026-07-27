"""
Graph Generator for BFS and Heuristic Search Assignments
=========================================================
This script generates structured weighted directed graphs of different sizes
and saves them to JSON files.

Graph Structure: Transportation/Logistics Network
- Nodes represent distribution centers/warehouses/stores
- Edges represent shipping routes with distances (weights)
- Node properties: id, name, type, region, capacity

Author: AI Course Materials
Date: February 2026
"""

import json
import random
import math

def generate_structured_graph(num_nodes, graph_type="small"):
    """
    Generate a structured weighted directed graph.

    Args:
        num_nodes (int): Number of nodes in the graph
        graph_type (str): Size category for naming

    Returns:
        dict: Graph structure with nodes and edges
    """

    # Define node types and regions for structured generation
    node_types = ["warehouse", "distribution_center", "retail_store", "hub", "depot"]
    regions = ["north", "south", "east", "west", "central"]

    # Initialize graph structure
    graph = {
        "metadata": {
            "num_nodes": num_nodes,
            "graph_type": graph_type,
            "description": "Structured transportation/logistics network"
        },
        "nodes": {},
        "edges": []
    }

    # Generate nodes with properties
    print(f"Generating {num_nodes} nodes...")
    for i in range(num_nodes):
        node_id = f"node_{i}"

        # Assign properties to each node
        node_type = random.choice(node_types)
        region = random.choice(regions)
        capacity = random.randint(100, 5000)
        priority = random.randint(1, 5)

        # Calculate coordinates for spatial structure (for heuristic)
        # Distribute nodes in a 2D space
        angle = 2 * math.pi * i / num_nodes
        radius = math.sqrt(i) * 10  # Spiral distribution
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        graph["nodes"][node_id] = {
            "id": node_id,
            "name": f"{node_type}_{region}_{i}",
            "type": node_type,
            "region": region,
            "capacity": capacity,
            "priority": priority,
            "coordinates": {"x": round(x, 2), "y": round(y, 2)}
        }

    # Generate edges with structured connectivity
    # Create a mix of local and long-distance connections
    print(f"Generating edges...")

    node_ids = list(graph["nodes"].keys())
    num_edges = 0

    # Strategy: Each node connects to several nearby nodes and a few distant ones
    edges_per_node_avg = max(3, min(10, num_nodes // 100))  # Scale with graph size

    for i, source_id in enumerate(node_ids):
        source_node = graph["nodes"][source_id]

        # Calculate number of edges for this node (with some randomness)
        num_connections = random.randint(
            max(2, edges_per_node_avg - 2),
            edges_per_node_avg + 3
        )

        # Connect to nearby nodes (by index)
        nearby_indices = []
        for offset in range(1, num_connections):
            target_idx = (i + offset) % num_nodes
            if target_idx != i:
                nearby_indices.append(target_idx)

        # Add some random long-distance connections
        num_random = max(1, num_connections // 3)
        random_indices = random.sample(range(num_nodes), num_random)
        random_indices = [idx for idx in random_indices if idx != i]

        all_target_indices = set(nearby_indices + random_indices[:num_random])

        # Create edges
        for target_idx in all_target_indices:
            target_id = node_ids[target_idx]
            target_node = graph["nodes"][target_id]

            # Calculate weight based on Euclidean distance
            dx = source_node["coordinates"]["x"] - target_node["coordinates"]["x"]
            dy = source_node["coordinates"]["y"] - target_node["coordinates"]["y"]
            distance = math.sqrt(dx**2 + dy**2)

            # Add some randomness to weight (±20%)
            weight = max(1, int(distance * random.uniform(0.8, 1.2)))

            # Add edge
            graph["edges"].append({
                "source": source_id,
                "target": target_id,
                "weight": weight
            })

            num_edges += 1

    graph["metadata"]["num_edges"] = num_edges

    print(f"Generated {num_nodes} nodes and {num_edges} edges")

    return graph


def save_graph_to_json(graph, filename):
    """
    Save graph to JSON file.

    Args:
        graph (dict): Graph structure
        filename (str): Output filename
    """
    with open(filename, 'w') as f:
        json.dump(graph, f, indent=2)
    print(f"Graph saved to {filename}")


def generate_all_graphs():
    """
    Generate all three graph sizes for the assignment.
    """
    print("="*60)
    print("GRAPH GENERATION FOR BFS AND HEURISTIC SEARCH ASSIGNMENTS")
    print("="*60)
    print()

    # Small graph: 500 nodes
    print("Generating SMALL graph (500 nodes)...")
    small_graph = generate_structured_graph(500, "small")
    save_graph_to_json(small_graph, "graph_small.json")
    print()

    # Medium graph: 3000 nodes
    print("Generating MEDIUM graph (3000 nodes)...")
    medium_graph = generate_structured_graph(3000, "medium")
    save_graph_to_json(medium_graph, "graph_medium.json")
    print()

    # Large graph: 10000 nodes
    print("Generating LARGE graph (10000 nodes)...")
    large_graph = generate_structured_graph(10000, "large")
    save_graph_to_json(large_graph, "graph_large.json")
    print()

    print("="*60)
    print("ALL GRAPHS GENERATED SUCCESSFULLY")
    print("="*60)
    print("\nFiles created:")
    print("  - graph_small.json (500 nodes)")
    print("  - graph_medium.json (3000 nodes)")
    print("  - graph_large.json (10000 nodes)")
    print("\nGraph Properties:")
    print("  - Node properties: id, name, type, region, capacity, priority, coordinates")
    print("  - Edge properties: source, target, weight")
    print("  - Graph type: Structured weighted directed graph")


if __name__ == "__main__":
    generate_all_graphs()
