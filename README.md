# Tic Tac Toe Game Algorithms
This repository contains implementations of the Tic Tac Toe game using various algorithms. Each file in the repository represents a different algorithm designed to ensure the player never wins. Below is a brief description of each algorithm and its mechanism.

# Files and Algorithms

# A_star.py
A Algorithm*

The A* algorithm uses a heuristic to guide its search. It combines the cost to reach a node and the estimated cost from that node to the goal. This makes it efficient in finding the shortest path to victory while blocking the opponent.

# Uniformed_Cost.py
Uniform Cost Search

Uniform Cost Search explores all possible moves, expanding the least costly nodes first. This ensures that the algorithm finds the least cost path to victory or a draw, preventing the player from winning.

# bfs.py
Breadth-First Search (BFS)

BFS explores all nodes at the present depth level before moving on to nodes at the next depth level. This guarantees that the shortest path to a win or draw is found, effectively blocking the player's attempts to win.

# bidirectional.py
Bidirectional Search

Bidirectional Search runs two simultaneous searches: one forward from the initial state and one backward from the goal state. When the two searches meet, the algorithm finds the optimal path. This approach reduces the search space and time, ensuring the player cannot win.

# dfs.py
Depth-First Search (DFS)

DFS explores as far down a branch as possible before backtracking. This algorithm might not always find the shortest path to victory but can still prevent the player from winning by thoroughly exploring possible moves.

# greedy.py
Greedy Search

Greedy Search makes decisions based on the best immediate, short-term benefit. It uses a heuristic to choose the move that seems best at each step. Although it doesn't guarantee the shortest path, it effectively blocks the player's winning moves.

# minmax.py
Minimax Algorithm

The Minimax algorithm is a backtracking algorithm used in decision-making and game theory. It provides an optimal move for the player assuming that the opponent is also playing optimally. The algorithm minimizes the possible loss in a worst-case scenario, ensuring the player never wins.

# poeBI.py
Player-Optimal with Bidirectional Search

This algorithm combines bidirectional search with strategies to optimize the player's moves while preventing the player from winning. It ensures a balanced game by exploring optimal paths from both perspectives.

# poeGUI_BI.py
Player-Optimal with GUI and Bidirectional Search

This is an extension of the poeBI.py algorithm with a graphical user interface (GUI). The GUI allows players to interact with the game visually while the bidirectional search ensures the player cannot win.

# poeIDS.py
Player-Optimal with Iterative Deepening Search

This algorithm combines player optimization with iterative deepening search (IDS). IDS performs a depth-first search to a limited depth, increasing the depth limit iteratively. This approach ensures that the player is optimally blocked from winning.

# poebfs.py
Player-Optimal with Breadth-First Search

Combines player optimization strategies with BFS. This algorithm ensures that the player's winning moves are blocked while exploring all possible moves level by level, guaranteeing a fair and balanced game.

# Getting Started
To run any of these algorithms, you will need Python installed on your machine. Clone the repository and run the desired algorithm file using Python.

bash
Copy code
git clone https://github.com/yourusername/tictactoe-algorithms.git
cd tictactoe-algorithms
python A_star.py  # Example for running the A* algorithm
Each file is self-contained and can be run independently. The algorithms are designed to prevent the player from winning, providing a challenging game experience.

# Contributing
Feel free to contribute to this repository by adding new algorithms or improving existing ones. Create a pull request with your changes, and ensure your code follows the repository's style and guidelines.
