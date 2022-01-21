import argparse
from tqdm import tqdm
import numpy as np
from itertools import permutations


def check_board(board):
    # Check total pieces
    if board.sum() != board.shape[0]:
        return False
    # Check horizontal
    if board.sum(axis=1).max() > 1:
        return False
    # Check vertical
    if board.sum(axis=0).max() > 1:
        return False

    # Check Diagonals
    for i in range(board.shape[0]):
        # Down-Right Diagonals
        if np.diag(board, k=i).sum() > 1 or np.diag(board, k=-i).sum() > 1:
            return False
        # Up-Right Diagonals
        flipped_board = np.flipud(board)
        if np.diag(flipped_board, k=i).sum() > 1 or np.diag(flipped_board, k=-i).sum() > 1:
            return False

    return True


def find_solution(dim=8, return_on_first_solution=True):
    all_possible_files = set(permutations(np.arange(dim)))

    solutions = []

    for file_option in tqdm(all_possible_files):
        # Generate board and place pieces in rank & file indexes
        board = np.zeros((dim,dim))
        board[np.arange(dim), file_option] = 1
        if check_board(board):
            if return_on_first_solution:
                return board
            solutions.append(board)

    return solutions
  
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dim', type=int, nargs='?', default=8,
                    help='''Table dimensions. 
                    Example, `-d 8` will use an 8x8 board''')
    parser.add_argument('-a', '--all', nargs='?', default=False,
                    help='''Whether to return the first solution found or return all found solutions
                    NOTE: searching for all solutions can take a large time, especially if dim>11''')

    args = parser.parse_args()

    return_on_first_solution = False if args.all else True

    solutions = find_solution(dim=args.dim, return_on_first_solution=return_on_first_solution)
    print(f'{len(solutions)} found')
    for s in solutions:
        print(s)
        print('----------')
