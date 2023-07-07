# CÓDIGO COM HEURISTICA

import numpy as np
from os import system, name

ROWS = 6
COLUMNS = 7

# ----------------------------------------------------------------------------------


def nos_explorados_contador(board, depth, maximizing_player):
    if is_winning_move(board, 2) or is_winning_move(board, 1) or len(get_valid_locations(board)) == 0 or depth == 0:
        return 1

    total_nodes = 0
    valid_locations = get_valid_locations(board)
    if maximizing_player:
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 2)
            total_nodes += nos_explorados_contador(
                temp_board, depth - 1, False)
    else:
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 1)
            total_nodes += nos_explorados_contador(temp_board, depth - 1, True)

    return total_nodes


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
            new_score = minimax(temp_board, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else:  # minimizing player
        value = np.Inf
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            temp_board = board.copy()
            drop_piece(temp_board, col, 1)
            new_score = minimax(temp_board, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value

# ----------------------------------------------------------------------------------
# FUNÇÕES QUE IRÃO SUBSTITUIR A FUNÇÃO DE UTILIDADE E O TESTE DE TÉRMINO


def evaluate_position(board, player):
    score = 0

    # Avaliar sequências horizontais
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            sequence = board[row, col:col + 4]
            score += evaluate_sequence(sequence, player)

    # Avaliar sequências verticais
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            sequence = board[row:row + 4, col]
            score += evaluate_sequence(sequence, player)

    # Avaliar sequências diagonais (para a direita e para a esquerda)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            sequence = [board[row + i, col + i] for i in range(4)]
            score += evaluate_sequence(sequence, player)

            sequence = [board[row + i, col + 3 - i] for i in range(4)]
            score += evaluate_sequence(sequence, player)

    return score


def evaluate_sequence(sequence, player):
    score = 0
    # Identificar o oponente (1 para o jogador 2, 2 para o jogador 1)
    opponent = 3 - player

    if sequence.
    (player) == 4:
        score += 100
    elif sequence.count(player) == 3 and sequence.count(0) == 1:
        score += 5
    elif sequence.count(player) == 2 and sequence.count(0) == 2:
        score += 2

    if sequence.count(opponent) == 3 and sequence.count(0) == 1:
        score -= 4

    return score


def evaluate(board, player):
    # Avaliar a posição do jogador
    player_score = evaluate_position(board, player)

    # Avaliar a posição do oponente
    # Identificar o oponente (1 para o jogador 2, 2 para o jogador 1)
    opponent = 3 - player
    opponent_score = evaluate_position(board, opponent)

    # Retornar a diferença entre as pontuações do jogador e do oponente
    return player_score - opponent_score


# ----------------------------------------------------------------------------------
def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMNS):
        if valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


# ----------------------------------------------------------------------------------
# CSI457 e CSI701
# Programa Principal
# Data: 06/05/2023
# ----------------------------------------------------------------------------------

print("CONECTA4 COM AVALIAÇÃO HEURÍSTICA")
board = create_board()
game_over = False
turn = 0

clear()

nos_explorados = 0

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
        col, minimax_score = minimax(board, 4, True)
        if valid_location(board, col):
            drop_piece(board, col, 2)
            if is_winning_move(board, 2):
                print("Jogador 2 Vence!!!")
                game_over = True
            else:
                evaluation = evaluate(board, 2)
                print("Avaliação do tabuleiro:", evaluation)

    nos_explorados += nos_explorados_contador(board, 4, turn == 1)
    print(board)
    print(" ")
    turn += 1
    turn = turn % 2

print("Número de nós explorados:", nos_explorados)
