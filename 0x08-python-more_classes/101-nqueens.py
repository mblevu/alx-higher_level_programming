#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    check is a queen can be p;aced at board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return (False)
    """
    check left side of row
    """
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return (False)
        i -= 1
        j -= 1

    """
    Check lower diagonal on left side
    """
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return (False)
        i += 1
        j -= 1
    return (True)


def solve_nqueens(N):
    """
    Solve the N queens probelm using backtracking
    """
    def backtrack(board, col, N, solutions):
        if col == N:
            """
            All queens are placed,add solution to the list
            """
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                """
                place queen at board[row][col]
                """
                board[row][col] = 1
                """recur for the next column"""
                backtrack(board, col+1, N, solutions)
                """remove the queen to backtrack"""
                board[row][col] = 0

    """check if N is valid"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """create an empty chessboard"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    """list of all possible solutions found so far"""
    solutions = []
    """solve the problem"""
    backtrack(board, 0, N, solutions)
    """Print solutions"""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """get the value of N from command line argument"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
