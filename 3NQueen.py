def solve_n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        return all(board[i] not in (col, col + row - i, col - row + i) for i in range(row))

    def place_queen(row):
        if row == n: return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if place_queen(row + 1): return True
        return False

    if not place_queen(0):
        print("No solution exists.")
        return

    for row in range(n):
        print(" ".join("Q" if board[row] == col else "." for col in range(n)))

n = 4
solve_n_queens(n)



'''
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Create an n x n chessboard with all cells initialized to 0

    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1 or board[i][col] == 1:
                return False  # Check if there is a Queen in the same row or column
            for j in range(n):
                if (i+j == row+col or i-j == row-col) and board[i][j] == 1:
                    return False  # Check if there is a Queen in the same diagonal
        return True

    def backtrack(col):
        if col >= n:
            return True  # Base case: All columns are filled with Queens, solution found
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1  # Place a Queen in the current cell
                if backtrack(col + 1):
                    return True  # Recursively solve for the next column
                board[i][col] = 0  # Backtrack: Remove the Queen if the next column doesn't lead to a solution
        return False

    if not backtrack(0):
        print("No solution exists.")
        return

    for row in board:
        print(" ".join(["Q" if val == 1 else "." for val in row]))  # Print the final board representation

n = 4
solve_n_queens(n)  # Solve the N-Queens problem for n = 4
'''