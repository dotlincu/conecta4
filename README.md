# Connect Four with Heuristic Evaluation and Alpha-Beta Pruning

This repository contains an implementation of the Connect Four game with heuristic evaluation and alpha-beta pruning in Python. The Connect Four game is a two-player board game where the objective is to be the first to connect four of your own pieces in a row, column, or diagonal on a grid.

The implementation includes the following features:

1. Connect Four game logic: The game is played on a 6x7 grid, and the players take turns dropping their pieces into the columns. The game checks for winning moves and detects a draw.

2. Heuristic Evaluation: A heuristic evaluation function is used to estimate the strength of a game position for the AI player. The evaluation function assigns higher scores to positions that are more likely to lead to a win and lower scores to positions that are less favorable.

3. Alpha-Beta Pruning: The alpha-beta pruning algorithm is applied to the minimax search to improve the efficiency of the AI player's move selection. Alpha-beta pruning reduces the number of game positions that need to be evaluated by ignoring branches that are guaranteed to be worse than previously examined moves.

## Getting Started

To run the Connect Four game with heuristic evaluation and alpha-beta pruning, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sirlincu/conecta4.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd conecta4
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## How to Play

The game is played in the command line interface. The board is displayed as a grid of numbers, where each number represents a column. Players take turns entering the column number to drop their pieces. The game continues until one player connects four pieces in a row, column, or diagonal, or the game ends in a draw.

## Customization

The implementation allows for customization of certain parameters:

- `ROWS` and `COLUMNS` variables in `connect_four.py`: These variables define the size of the game board. Modify them to change the dimensions of the grid.

- Heuristic Evaluation Function: The `heuristic_evaluation` function in `connect_four.py` determines the score of a game position. You can customize this function to create your own evaluation strategy.

- Search Depth: The search depth in the `alphabeta` function in `connect_four.py` determines the depth of the alpha-beta search. A higher depth allows for a more thorough evaluation of future game positions but increases the computation time.

Feel free to experiment with different settings to explore the behavior of the game and AI player.

## About
Work carried out during the course CSI701 - Artficial Intelligence, taught by Professor Talles Henrique de Medeiros, offered in the 5th period of the Information Systems course, at the Federal University of Ouro Preto.

<ul>
    <li><a href="https://github.com/sirlincu">Lincoln Rebouças</a></li>
    <li><a href="https://github.com/Ibsiany">Ibsiany Dias</a></li>
    <li><a href="https://github.com/rafaelc-teixeira">Rafael Teixeira</a></li>
</ul>

## Contributing

Contributions to this repository are welcome. If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

## Acknowledgments

This implementation is inspired by the game Connect Four and the concepts of heuristic evaluation and alpha-beta pruning in artificial intelligence.

