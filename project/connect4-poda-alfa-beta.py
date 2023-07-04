# CÓDIGO COM PODA ALFA-BETA

import numpy as np
from os import system, name

ROWS = 6
COLUMNS = 7


# ----------------------------------------------------------------------------------
def clear():
    # para windows
    if name == 'nt':
        _ = system('cls')

    # para mac e linux(aqui, os.name eh 'posix')
    else:
        _ = system('clear')

# ----------------------------------------------------------------------------------


def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

# ----------------------------------------------------------------------------------


def valid_location(board, column):
    if column >= 0 and column <= COLUMNS:
        return board[ROWS - 1][column] == 0

# ----------------------------------------------------------------------------------


def drop_piece(board, column, piece):
    for r in range(ROWS):
        if board[r][column] == 0:
            board[r][column] = piece
            return

# ----------------------------------------------------------------------------------


def is_winning_move(board, piece):
    # verifica se existem quatro peças em linha na horizontal, vertical e diagonais
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                return True
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                    c + 3] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                    c + 3] == piece:
                return True


# ----------------------------------------------------------------------------------
def minimax(board, depth, alpha, beta, maximizing_player):
    if is_winning_move(board, 2):  # IA ganhou
        return (None, 100)
    elif is_winning_move(board, 1):  # jogador humano ganhou
        return (None, -100)
    elif len(get_valid_locations(board)) == 0:  # jogo empatado
        return (None, 0)
    elif depth == 0:  # profundidade máxima atingida
        return (None, 0)

    valid_locations = get_valid_locations(board)
    if maximizing_player:
        value = -np.Inf
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 2)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Poda Alfa-Beta
        return column, value

    else:  # minimizing player
        value = np.Inf
        # column = np.random.choice(valid_locations)
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 1)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break  # Poda Alfa-Beta
        return column, value


# ----------------------------------------------------------------------------------
def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMNS):
        if valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


# ----------------------------------------------------------------------------------
# CSI301
# Programa Principal
# Data: 06/05/2023
# ----------------------------------------------------------------------------------
print("CONECTA4 COM PODA ALFA-BETA")
board = create_board()
game_over = False
turn = 0

clear()
while not game_over:
    # Movimento do Jogador 1
    if turn == 0:
        col = int(input("Jogador 1, selecione a coluna (0-6):"))
        if valid_location(board, col):
            drop_piece(board, col, 1)
            if is_winning_move(board, 1):
                print("Jogador 1 Vence!! Parabéns!!")
                game_over = True
        else:
            while not valid_location(board, col):
                col = int(
                    input("Não disponível! Jogador1, selecione a coluna (0-6):"))
                if valid_location(board, col):
                    drop_piece(board, col, 1)
                    if is_winning_move(board, 1):
                        print("Jogador 1 Vence!! Parabéns!!")
                        game_over = True

    # Movimento da IA
    else:
        col, minimax_score = minimax(board, 4, -np.Inf, np.Inf, True)
        if valid_location(board, col):
            drop_piece(board, col, 2)
            if is_winning_move(board, 2):
                print("Jogador 2 Vence!!!")
                game_over = True

    print(board)
    print(" ")
    turn += 1
    turn = turn % 2
