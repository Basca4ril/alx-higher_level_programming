#!/usr/bin/python3

import sys
"""
Defines Nqueen
"""
def is_safe(bd, row, col, n):
    """
    Check if there is queen in same column

    Args:
    bd: board
    row: row
    col: column
    n: number

    Returns:
    Boolean
    """
    for x in range(row):
        if bd[x] == col or abs(bd[x] - col) == row - x:
            return False

    return True

def solve_nqueen(bd, row, n):
    if row == n:
        sol = [[r, c] for r, c in enumerate(bd)]
        print(sol)
        return

    for col in range(n):
        if is_safe(bd, row, col, n):
            bd[row] = col
            solve_nqueen(bd[:], row + 1, n)

def solve_nqueens(n):
    if not str(n).isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = [[0 for _ in range(n)] for _ in range(n)]

    solve_nqueen(bd, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
