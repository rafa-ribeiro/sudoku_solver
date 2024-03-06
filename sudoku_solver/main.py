from backtracking_solver import core

def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    board_2 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    print_board(board=board_2)
    print(" ")
    print(" ")
    print(" ")
    core.solve_sudoku(board=board_2)
    print_board(board=board_2)


def print_board(board):
    cell_template = " X "
    line_template = "═"
    h_border = "╔" + line_template * len(cell_template) * 3 + "╦" + line_template * len(cell_template) * 3 + "╦" + line_template * len(cell_template) * 3 + "╗"
    m_border = "╠" + line_template * len(cell_template) * 3 + "╬" + line_template * len(cell_template) * 3 + "╬" + line_template * len(cell_template) * 3 + "╣"
    l_border = "╚" + line_template * len(cell_template) * 3 + "╩" + line_template * len(cell_template) * 3 + "╩" + line_template * len(cell_template) * 3 + "╝"

    print(h_border)
    for row in range(len(board)):
        line = "║"
        for col in range(len(board[row])):
            cell_value = board[row][col]
            cell_num = " " + (str(cell_value) if cell_value > 0 else "_") + " "
            line += cell_num
            if (col + 1) % 3 == 0:
                line += "║"

        print(line)
        if (row + 1) % 3 == 0 and row +1 != len(board):
            print(m_border)

    print(l_border)


if __name__ == '__main__':
    main()
