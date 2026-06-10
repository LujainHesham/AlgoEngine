# ⚙ Multi-Algorithm Decision Engine

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.1-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-cyan)
![License](https://img.shields.io/badge/license-MIT-purple)

**An intelligent problem-solving assistant that automatically selects the optimal algorithm based on problem constraints**

[Features](#features) • [Quick Start](#quick-start) • [Architecture](#architecture) • [Team Roles](#team-roles) • [API Documentation](#api-documentation)

</div>

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Quick Start](#quick-start)
4. [Architecture](#architecture)
5. [Algorithms Implemented](#algorithms-implemented)
6. [Decision Engine Logic](#decision-engine-logic)
7. [API Documentation](#api-documentation)
8. [Team Roles & Responsibilities](#team-roles--responsibilities)
9. [File Structure](#file-structure)
10. [Screenshots](#screenshots)
11. [Troubleshooting](#troubleshooting)
12. [Future Improvements](#future-improvements)

---

## 🎯 Project Overview

The **Multi-Algorithm Decision Engine** is an intelligent assistant that:

1. **Accepts** problem descriptions (type, input size, time budget, quality requirement)
2. **Analyzes** the problem structure using rule-based logic
3. **Selects** the most appropriate algorithm (DP, Greedy, D&C, or Brute Force)
4. **Executes** the chosen algorithm
5. **Reports** both the solution AND a justification for the algorithm choice
6. **Compares** algorithms in experiment mode

### Problem Types Supported

| Problem Type | Algorithms | Quality |
|--------------|------------|---------|
| 0/1 Knapsack | DP, Greedy, Brute Force | Exact/Approx |
| Fractional Knapsack | Greedy | Exact |
| Minimum Spanning Tree | Kruskal, Prim | Exact |
| Shortest Path | Dijkstra, Bellman-Ford | Exact |
| Sorting | Merge Sort, Quick Sort, Bubble Sort | Exact |
| Sequence Alignment | DP, Brute Force | Exact |
| Matrix Multiplication | D&C, Naive | Exact |
| Weighted Interval Scheduling | DP, Brute Force | Exact |
| Binary Search | D&C, Linear Search | Exact |
| Fast Exponentiation | D&C, Linear | Exact |
| Subset Enumeration | Brute Force | Exact |

---

## ✨ Features

### 🧠 Intelligent Decision Engine
- Rule-based algorithm selection using problem properties
- Automatic justification generation
- Threshold-based feasibility checking (n≤15 for brute force, n×capacity≤10M for DP)

### ⚡ Multiple Algorithm Families
- **Dynamic Programming** - Exact solutions for overlapping subproblems
- **Greedy** - Fast approximations for tight time budgets
- **Divide & Conquer** - Optimal for independent subproblems
- **Brute Force** - Exact solutions for n≤15 (safety guarded)

### 📊 Experiment Mode
- Runs ALL applicable algorithms
- Generates ranked comparison table
- Shows approximation ratios
- Visual runtime comparison charts

### 📈 Benchmark Mode
- Tests algorithms across multiple input sizes (n=10,20,50,100,200)
- Generates scaling analysis charts
- Compares theoretical vs actual complexity

### 📄 PDF Report Generation
- Professional algorithm benchmark reports
- Includes decision justification, complexity analysis, and results

### 🎨 Modern UI
- Dark theme with cyan/amber/purple accents
- Interactive decision flowchart (SVG)
- DP table visualization
- Real-time input validation

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
Modern web browser (Chrome, Firefox, Edge)
```

### Installation

```bash
# 1. Clone or download the project
cd MultiAlgo-DecisionEngine/Algorithms+bonus

# 2. Install dependencies
pip install fastapi uvicorn pydantic reportlab

# 3. Generate datasets (first time only)
python generate_datasets.py

# 4. Start the backend server
python Backend.py

# 5. In a NEW terminal, start the frontend server
python -m http.server 8000

# 6. Open your browser to:
# http://localhost:8000
```

### Alternative: One-Click Launch (Windows)

Create a `start.bat` file:

```batch
@echo off
start cmd /k "python Backend.py"
timeout /t 2
start cmd /k "python -m http.server 8000"
timeout /t 2
start http://localhost:8000
```

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                      (HTML/CSS/JavaScript)                      │
│                           index.html                            │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP/REST API
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                          BACKEND API                            │
│                         (FastAPI/Python)                        │
│                          Backend.py                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  /solve     │  │  /compare   │  │ /benchmark  │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DECISION ENGINE                           │
│                     Decision_Engine.py                          │
│                                                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  choose_algorithm(problem_type, n, T, quality, **kwargs)│   │
│  │                                                         │   │
│  │  Rules:                                                 │   │
│  │  1. n≤15 & exact → Brute Force                         │   │
│  │  2. n×capacity≤10M & exact → DP                        │   │
│  │  3. T<100ms OR approximate → Greedy                    │   │
│  │  4. Sorting/Searching/Exponentiation → D&C             │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                        ALGORITHMS                               │
│                         AlgoImpl.py                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │    DP    │  │  Greedy  │  │   D&C    │  │   BF     │        │
│  │ Knapsack │  │ Fractional│ │ MergeSort│ │ Subset   │        │
│  │Alignment │  │ Kruskal  │ │BinarySearch│ │Enumeration│       │
│  │BellmanFord│ │ Dijkstra │ │FastExp   │ │          │        │
│  │Scheduling│  │          │ │MatrixMult│ │          │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Algorithms Implemented

### Dynamic Programming (DP)

| Algorithm | Complexity | Returns | When to Use |
|-----------|------------|---------|-------------|
| **knapsack_dp** | O(n × W) | DP table, backtrack sequence | Exact 0/1 knapsack |
| **sequence_alignment_dp** | O(n × m) | Alignment, DP table | String comparison |
| **bellman_ford_dp** | O(V × E) | Distances, path | Shortest path with negative weights |
| **weighted_interval_scheduling_dp** | O(n log n) | Selected intervals | Job scheduling with profits |

### Greedy Algorithms

| Algorithm | Complexity | Approximation | When to Use |
|-----------|------------|---------------|-------------|
| **knapsack_greedy** | O(n log n) | No guaranteed bound | Tight time budget |
| **fractional_knapsack_greedy** | O(n log n) | 1.0 (optimal) | Items can be split |
| **kruskal_mst_greedy** | O(E log E) | 1.0 (optimal) | Minimum Spanning Tree |
| **dijkstra_greedy** | O(V²) | 1.0 (optimal) | Non-negative weights |

### Divide & Conquer (D&C)

| Algorithm | Complexity | Returns | How It Works |
|-----------|------------|---------|--------------|
| **merge_sort_dc** | O(n log n) | Sorted array, recursion depth | Split, sort halves, merge |
| **binary_search_dc** | O(log n) | Index, steps | Halve search space each step |
| **fast_exponentiation_dc** | O(log n) | Result, multiplications | Square and multiply |
| **matrix_multiplication_dc** | O(n³) | Product matrix | Split into quadrants |

### Brute Force

| Algorithm | Complexity | Safety | When to Use |
|-----------|------------|--------|-------------|
| **knapsack_brute_force** | O(2ⁿ) | n ≤ 15 only | Exact solution verification |

---

## 🧠 Decision Engine Logic

### Priority Order (Highest to Lowest)

```
1. INPUT VALIDATION
   ├─ n > 0?
   ├─ T > 0?
   ├─ Valid problem type?
   └─ Valid quality?

2. DIVIDE & CONQUER (Special cases)
   ├─ Sorting → Merge Sort
   ├─ Searching → Binary Search (requires sorted array)
   ├─ Exponentiation → Fast Exponentiation
   └─ Matrix Multiplication → D&C

3. MST PROBLEM
   └─ Kruskal's Algorithm

4. SCHEDULING PROBLEM
   └─ Weighted Interval Scheduling DP

5. SEQUENCE ALIGNMENT
   └─ Needleman-Wunsch DP

6. SHORTEST PATH
   ├─ Negative weights → Bellman-Ford
   └─ Non-negative → Dijkstra

7. KNAPSACK & SUBSET
   ├─ Fractional → Greedy (optimal)
   ├─ Approximate/Best-effort/T<100ms → Greedy
   ├─ n ≤ 15 & exact → Brute Force
   ├─ n×capacity ≤ 10M & exact → DP
   └─ Fallback → Greedy (with warning)
```

### Thresholds

| Algorithm | Condition | Reason |
|-----------|-----------|--------|
| Brute Force | n ≤ 15 | 2ⁿ = 32,768 max subsets |
| DP | n × capacity ≤ 10,000,000 | ~80MB memory limit |
| Dijkstra | n ≤ 10,000 | O(n²) complexity |
| Bellman-Ford | n ≤ 500 | O(V × E) slower |

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### `GET /health`
Check server status

**Response:**
```json
{
  "status": "healthy",
  "server_time": "2024-01-15 10:30:00",
  "algorithms_loaded": 24
}
```

#### `POST /solve`
Run the best algorithm for your problem

**Request Body:**
```json
{
  "problem_type": "knapsack",
  "n": 20,
  "time_budget_ms": 500,
  "quality_requirement": "exact",
  "parameters": {
    "values": [60, 100, 120],
    "weights": [10, 20, 30],
    "capacity": 50
  }
}
```

**Response:**
```json
{
  "status": "success",
  "decision": {
    "algorithm_name": "knapsack_dp",
    "justification": "Dynamic Programming selected because...",
    "expected_complexity": "O(n × capacity)",
    "quality_guarantee": "100% optimal"
  },
  "solution": {
    "selected_items": [1, 2],
    "total_value": 220,
    "dp_table": [[...]]
  },
  "runtime_ms": 12.5
}
```

#### `POST /compare`
Run multiple algorithms and compare

**Request Body:**
```json
{
  "problem_type": "knapsack",
  "n": 10,
  "runs": 3,
  "algorithms": ["knapsack_dp", "knapsack_greedy", "knapsack_brute_force"],
  "parameters": {...}
}
```

#### `GET /algorithms`
List all available algorithms

#### `POST /benchmark`
Run scaling analysis across input sizes

#### `POST /export-pdf`
Generate PDF report

---

## 👥 Team Roles & Responsibilities

### Member 1: Algorithm Engineer
**Files:** `AlgoImpl.py`

| Task | Status |
|------|--------|
| Implement DP (Knapsack, Alignment, Bellman-Ford, Scheduling) | ✅ |
| Implement Greedy (Fractional Knapsack, Kruskal, Dijkstra) | ✅ |
| Implement D&C (Merge Sort, Binary Search, Fast Exponentiation) | ✅ |
| Implement Brute Force (Subset enumeration with n≤15 guard) | ✅ |
| Create ALGORITHM_REGISTRY with metadata | ✅ |
| Implement run_algorithm() dispatcher | ✅ |
| Implement run_experiment_mode() | ✅ |

### Member 2: Decision Engine Engineer
**Files:** `Decision_Engine.py`

| Task | Status |
|------|--------|
| Define rules based on (problem_type, n, T, quality) | ✅ |
| Implement choose_algorithm() function | ✅ |
| Add thresholds (n<15 → BF, n×capacity≤10M → DP) | ✅ |
| Generate justification paragraphs | ✅ |
| Return algorithm + reason + complexity | ✅ |

### Member 3: Backend Engineer
**Files:** `Backend.py`, `dataset_loader.py`, `pdf_generator.py`

| Task | Status |
|------|--------|
| Build FastAPI server | ✅ |
| Create /solve and /compare endpoints | ✅ |
| Connect Decision Engine with Algorithms | ✅ |
| Implement timeout protection | ✅ |
| Add PDF report generation | ✅ |
| Add benchmark endpoint | ✅ |

### Member 4: Frontend Engineer
**Files:** `index.html`, `frontend.js`

| Task | Status |
|------|--------|
| Build input form (dropdown, sliders, radio buttons) | ✅ |
| Display recommendation card with justification | ✅ |
| Show solution visualizations (DP tables, arrays, graphs) | ✅ |
| Build experiment mode comparison table | ✅ |
| Generate decision flowchart (SVG) | ✅ |
| Add benchmark mode with charts | ✅ |

---

## 📁 File Structure

```
MultiAlgo-DecisionEngine/
└── Algorithms+bonus/
    ├── index.html              # Main UI (Member 4)
    ├── frontend.js             # JavaScript logic (Member 4)
    ├── Backend.py              # FastAPI server (Member 3)
    ├── AlgoImpl.py             # All algorithms (Member 1)
    ├── Decision_Engine.py      # Algorithm selection (Member 2)
    ├── dataset_loader.py       # Dynamic data generation
    ├── pdf_generator.py        # PDF report generation
    ├── generate_datasets.py    # Initial dataset creation
    ├── data/                   # JSON dataset files
    │   ├── knapsack_cases.json
    │   ├── graph_cases.json
    │   ├── sorting_cases.json
    │   └── ...
    └── README.md               # This file
```

---

## 📸 Screenshots

### Main Dashboard
```
┌─────────────────────────────────────────────────────────────────┐
│  ⚙ ALGORITHM.ENGINE                              [STANDARD MODE] │
├─────────────────────────────────────────────────────────────────┤
│ ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐ │
│ │ Problem Type     │ │ RECOMMENDATION   │ │ Decision Path    │ │
│ │ [Knapsack ▼]     │ │ ┌──────────────┐ │ │ ┌──────────────┐ │ │
│ │ n = 20 ━━━━━━━━━━│ │ │ DP Selected  │ │ │ │ START →      │ │ │
│ │ T = 500ms ━━━━━━━│ │ │ Justification│ │ │ │ Type? → DP   │ │ │
│ │ Quality: ○ Exact │ │ │ O(n×W)       │ │ │ │ → END        │ │ │
│ │ [SOLVE]          │ │ └──────────────┘ │ │ └──────────────┘ │ │
│ └──────────────────┘ └──────────────────┘ └──────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Experiment Mode
```
┌─────────────────────────────────────────────────────────────────┐
│ EXPERIMENT RESULTS                                    [EXPORT PDF]│
├─────────────────────────────────────────────────────────────────┤
│ ┌────────────┬──────────┬──────────┬────────┬─────┐              │
│ │ Algorithm  │ Runtime  │ Value    │ Ratio  │ Rank│              │
│ ├────────────┼──────────┼──────────┼────────┼─────┤              │
│ │ DP         │ 2.3 ms   │ 220      │ 1.00   │ #1  │              │
│ │ Greedy     │ 0.5 ms   │ 210      │ 0.95   │ #2  │              │
│ │ Brute Force│ 45.2 ms  │ 220      │ 1.00   │ #3  │              │
│ └────────────┴──────────┴──────────┴────────┴─────┘              │
│                                                                   │
│ Best algorithm: DP with value 220 in 2.3ms                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Module not found errors** | Run `pip install fastapi uvicorn pydantic reportlab` |
| **Port 5000 already in use** | Change port in Backend.py: `port=5001` |
| **CORS errors** | Backend.py already has CORS middleware enabled |
| **Brute force runs forever** | Check n ≤ 15 (safety guard is built-in) |
| **DP table too large** | Threshold n×capacity ≤ 10M prevents memory issues |
| **Blank page on load** | Open browser console (F12) to see JavaScript errors |
| **API not connecting** | Ensure Backend.py is running on port 5000 |

### Port Conflicts

```bash
# Change backend port (in Backend.py)
uvicorn.run(app, host="0.0.0.0", port=5001)  # Change 5000 to 5001

# Update frontend.js
const API_URL = "http://localhost:5001";  # Match the new port
```

---

## 🚀 Future Improvements

- [ ] Add more problem types (TSP, Graph Coloring, Hamiltonian Path)
- [ ] Implement Strassen's matrix multiplication (O(n^log₂7))
- [ ] Add parallel algorithm execution
- [ ] Machine learning for algorithm selection
- [ ] Docker containerization
- [ ] User accounts and saved sessions
- [ ] More visualization options (graph drawing, tree animations)

---

## 📞 Support

For issues or questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Open browser console (F12) for JavaScript errors
3. Check terminal output for Python errors
4. Ensure all dependencies are installed

---

## 📄 License

This project is created for educational purposes as part of **Project 19 - Multi-Algorithm Decision Engine**.

---

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Chart.js for beautiful visualizations
- ReportLab for PDF generation
- All team members for their hard work

---

<div align="center">

**Made with ⚙ by Team Project 19**

[Back to Top](#multi-algorithm-decision-engine)

</div>