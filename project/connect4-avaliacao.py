# CÓDIGO AVALIAÇÃO HEURÍSTICA

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
    if column >= 0 and column <= ROWS:
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


def minimax(board, depth, maximizing_player):
    if is_winning_move(board, 2):  # IA vence
        return (None, 100, 1)  # retorna 1 como a contagem de nós para uma jogada vencedora
    elif is_winning_move(board, 1):  # jogador humano vence
        return (None, -100, 1)  # retorna 1 como a contagem de nós para uma jogada vencedora
    elif len(get_valid_locations(board)) == 0:  # jogo empatado
        return (None, 0, 1)  # retorna 1 como a contagem de nós para um jogo empatado
    elif depth == 0:  # profundidade máxima atingida
        return (None, evaluate_board(board)[0], evaluate_board(board)[1])  # usa a função de avaliação heurística para avaliar o tabuleiro atual

    valid_locations = get_valid_locations(board)
    if maximizing_player:
        value = -np.Inf
        column = np.random.choice(valid_locations)
        total_nodes = 1  # inicializa a contagem de nós para 1 para o nó atual
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 2)
            new_score, new_nodes = minimax(temp_board, depth - 1, False)[1:]  # ignora o primeiro elemento (coluna)
            if new_score > value:
                value = new_score
                column = col
            total_nodes += new_nodes
        return column, value, total_nodes

    else:  # minimizing player
        value = np.Inf
        column = np.random.choice(valid_locations)
        total_nodes = 1  # inicializa a contagem de nós para 1 para o nó atual
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 1)
            new_score, new_nodes = minimax(temp_board, (depth - 1), True)[1:]  # ignora o primeiro elemento (coluna)
            if new_score < value:
                value = new_score
                column = col
            total_nodes += new_nodes
        return column, value, total_nodes


def evaluate_board(board):
    # avalia o tabuleiro atual, retorna uma pontuação e o número de nós explorados
    score = 0
    nodes_explored = 1  # inicializa a contagem de nós para 1 para o nó atual

    # avalia linhas
    for r in range(ROWS):
        row = board[r]
        for c in range(COLUMNS - 3):
            window = row[c: c + 4]
            score += evaluate_window(window)
            nodes_explored += 1  # incrementa a contagem de nós para cada janela avaliada

    # avalia colunas
    for c in range(COLUMNS):
        column = board[:, c]
        for r in range(ROWS - 3):
            window = column[r: r + 4]
            score += evaluate_window(window)
            nodes_explored += 1  # incrementa a contagem de nós para cada janela avaliada

    # avalia diagonais (inclinação positiva)
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window)
            nodes_explored += 1  # incrementa a contagem de nós para cada janela avaliada

    # avalia diagonais (inclinação negativa)
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window)
            nodes_explored += 1  # incrementa a contagem de nós para cada janela avaliada

    return score, nodes_explored

def evaluate_window(window):
    # avalia uma janela de 4 peças
    score = 0
    player_pieces = 0
    opponent_pieces = 0

    for piece in window:
        if piece == 1:
            player_pieces += 1
        elif piece == 2:
            opponent_pieces += 1

    if player_pieces == 4:
        score += 100
    elif player_pieces == 3 and opponent_pieces == 0:
        score += 5
    elif player_pieces == 2 and opponent_pieces == 0:
        score += 2
    elif opponent_pieces == 3 and player_pieces == 0:
        score -= 4

    return score


# ----------------------------------------------------------------------------------


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMNS):
        if valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


# ----------------------------------------------------------------------------------
# CSI701
# Projeto: Implementação de um jogo de tabuleiro com IA
# Data: 09/07/2023
# ----------------------------------------------------------------------------------
print("CONECTA4 COM PADRÃO SIMPLES")
board = create_board()
game_over = False
turn = 0

clear()

while not game_over:
    # movimento do Jogador 1
    if turn == 0:
        col = int(input("Jogador 1, selecione a coluna (0-6): "))
        if valid_location(board, col):
            drop_piece(board, col, 1)
            if is_winning_move(board, 1):
                print("Jogador 1 Vence!! Parabéns!!")
                game_over = True
        else:
            while not valid_location(board, col):
                col = int(input("Não disponível! Jogador1, selecione a coluna (0-6):"))
                if valid_location(board, col):
                    drop_piece(board, col, 1)
                    if is_winning_move(board, 1):
                        print("Jogador 1 Vence!! Parabéns!!")
                        game_over = True

    # movimento da IA
    else:
        col, minimax_score, nodes = minimax(board, 4, True)
        nodes += nodes
        if valid_location(board, col):
            drop_piece(board, col, 2)
            if is_winning_move(board, 2):
                print("Jogador 2 Vence!!!")
                game_over = True

    print(board)
    print(" ")
    turn += 1
    turn = turn % 2

print("Número de nós explorados:", nodes)
