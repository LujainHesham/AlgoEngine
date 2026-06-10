import random

def generate_dynamic_instance(problem_type: str, n: int):
    """Generate a problem instance of exactly size n."""
    if problem_type in ["knapsack", "fractional_knapsack", "subset"]:
        capacity = n * 10
        weights = [random.randint(1, n * 2) for _ in range(n)]
        values = [random.randint(10, 100) for _ in range(n)]
        # 'target' is needed by subset_sum_bruteforce (a random achievable sum)
        target = random.randint(sum(weights) // 4, sum(weights) // 2)
        return {"values": values, "weights": weights, "capacity": capacity, "target": target}
    
    elif problem_type in ["mst", "shortest_path"]:
        num_nodes = n
        edges = []
        for i in range(1, num_nodes):
            edges.append({"from": random.randint(0, i-1), "to": i, "weight": random.randint(1, 50)})
        extra = random.randint(0, n)
        for _ in range(extra):
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            if u != v: edges.append({"from": u, "to": v, "weight": random.randint(1, 50)})
        
        adjacency = [[] for _ in range(num_nodes)]
        for e in edges:
            adjacency[e["from"]].append({"to": e["to"], "weight": e["weight"]})
            adjacency[e["to"]].append({"to": e["from"], "weight": e["weight"]})
        return {"num_nodes": num_nodes, "edges": edges, "adjacency": adjacency, "source_node": 0}
    
    elif problem_type == "sorting":
        return {"array": [random.randint(1, 1000) for _ in range(n)]}
    
    elif problem_type == "sequence_alignment":
        dna = ['A', 'T', 'G', 'C']
        seq_a = "".join(random.choice(dna) for _ in range(n))
        seq_b = "".join(random.choice(dna) for _ in range(n))
        return {"seq_a": seq_a, "seq_b": seq_b, "gap_penalty": 1, "mismatch_penalty": 1}
    
    elif problem_type == "searching":
        arr = sorted([random.randint(1, 5000) for _ in range(n)])
        return {"array": arr, "sorted_array": arr, "target": random.choice(arr)}
    
    elif problem_type == "exponentiation":
        return {"base": random.randint(2, 10), "exponent": n, "modulus": 10**9 + 7}
    
    elif problem_type == "scheduling":
        intervals = []
        for _ in range(n):
            s = random.randint(1, 50); e = s + random.randint(1, 20); w = random.randint(10, 100)
            intervals.append((s, e, w))
        return {"intervals": intervals}
    
    elif problem_type == "matrix_mult":
        # Ensure n is power of 2 — required for recursive D&C splitting
        p2 = 1
        while p2 < n: p2 *= 2
        m = p2
        mat_a = [[random.randint(1, 5) for _ in range(m)] for _ in range(m)]
        mat_b = [[random.randint(1, 5) for _ in range(m)] for _ in range(m)]
        return {"mat_a": mat_a, "mat_b": mat_b}
    
    return {}


def get_problem_instance(problem_type: str, n: int):
    """
    Returns a dynamically generated problem instance.
    This replaces the old JSON-based loading logic.
    """
    return generate_dynamic_instance(problem_type, n)
