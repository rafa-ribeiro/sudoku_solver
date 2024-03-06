from typing import Sequence, Tuple, Union, Any


def _is_valid(board: Sequence[Sequence], row: int, col: int, candidate_num: int) -> bool:
    # check if the candidate_num is unique in the row and in the column
    for i in range(9):
        if board[row][i] == candidate_num or board[i][col] == candidate_num:
            return False

    # check if candidate_num is unique in the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(3):
        for c in range(3):
            if board[start_row + r][c + start_col] == candidate_num:
                return False

    return True 


def _find_empty_cell(board) -> Union[Tuple[int, int], None]:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row, col
    
    return None

def solve_sudoku(board: Sequence[Sequence[int]]) -> bool:
    empty_cell = _find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for i in range(1, 10):
        if _is_valid(board=board, row=row, col=col, candidate_num=i):
            board[row][col] = i
            if solve_sudoku(board=board):
                return True
            board[row][col] = 0

    return False
