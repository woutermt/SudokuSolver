"""
Author: Wouter Tijs
Date: 20 Jan 2022

Challenge to read, interpret and solve sudoku puzzles
"""


import pandas as pd
import numpy as np

from CV.CV_matrify import SudokuFinder
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# ARGS
arg_puzzle_img = "Sudoku_puzzles/Easy/easy001-1.gif"
clean_img = "Sudoku_puzzles/Easy/1200px-Sudoku_Puzzle.png"
color_img = "Sudoku_puzzles/Easy/Sudoku_color.jpg"
easy_puzzle_dir = "Sudoku_puzzles/Easy"

test_puzzle_easy10 = [[3, 9, 0, 0, 0, 0, 0, 4, 6],
                     [0, 0, 0, 9, 3, 7, 2, 0, 8],
                     [0, 7, 0, 0, 6, 0, 0, 0, 5],
                     [0, 1, 3, 0, 2, 0, 8, 6, 0],
                     [2, 0, 0, 0, 9, 3, 1, 0, 7],
                     [0, 0, 0, 0, 1, 8, 4, 0, 2],
                     [8, 0, 0, 0, 0, 0, 0, 2, 1],
                     [0, 3, 0, 0, 5, 0, 0, 7, 4],
                     [5, 0, 4, 1, 7, 0, 9, 8, 3]]

test_puzzle_hard10 = [[0, 1, 0, 9, 0, 0, 0, 0, 0],
                      [4, 0, 0, 5, 0, 6, 0, 0, 0],
                      [0, 0, 0, 1, 0, 7, 0, 3, 8],
                      [0, 7, 9, 0, 0, 0, 0, 2, 0],
                      [3, 0, 0, 0, 6, 1, 0, 5, 0],
                      [0, 0, 8, 0, 0, 0, 0, 0, 0],
                      [0, 8, 0, 0, 0, 0, 0, 0, 0],
                      [0, 4, 0, 0, 0, 8, 1, 6, 9],
                      [2, 0, 0, 0, 4, 5, 0, 0, 0]]

solve_method = "other"              # manual


""" 
MANUAL SOLVER 
https://www.youtube.com/watch?v=G_UYXzGuqvM&t=18s&ab_channel=Computerphile
"""
def possible(test_puzz, y, x, n):

    for i in range(9):
        if test_puzz[y][i] == n:
            return False

        if test_puzz[i][x] == n:
            return False

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3

        for i in range(0, 3):
            for j in range(0, 3):
                if test_puzz[y0 + i][x0 + j] == n:
                    return False

        return True


def brute_force_solve_puzzle(test_puzz):
    for y in range(9):
        for x in range(9):
            if test_puzz[y][x] == 0:
                for n in range(1, 10):
                    if possible(test_puzz, y, x, n):
                        test_puzz[y][x] = n
                        brute_force_solve_puzzle(test_puzz)
                        test_puzz[y][x] = 0
                return
    print(np.matrix(test_puzz))
    input("more?")


""" OTHER METHOD """
def get_puzzle(puzz):

    # Create an instance for image mutations
    sudoku = SudokuFinder()

    # Read image and add to instance
    ing_puzz = sudoku.read_img(puzz)

    # Image convert to grayscale
    img_grey = sudoku.black_white(ing_puzz)

    # Image blurring
    img_blur = sudoku.gaussian(img_grey)

    # Image adaptive thresholding and invert colors
    img_thres = sudoku.threshold(img_blur)

    # Image contours
    # img_cont = sudoku.contour(img_thres)

    # Image visualise
    sudoku.show("Contour", img_thres)





def main():

    if solve_method == "manual":
        brute_force_solve_puzzle(test_puzzle_hard10)

    elif solve_method == "other":
        # Get sudoku matrix from image
        get_puzzle(clean_img)

        # Select solving method and apply to sudoku matrix
        # solve(puzzle_arr)

        # After solution is calculated, output
        # visualise(puzzle_solved)


if __name__ == "__main__":
    main()
