"""
Author: Wouter Tijs
Date: 20 Jan 2022

Challenge to read, interpret and solve sudoku puzzles
https://www.pyimagesearch.com/2020/08/10/opencv-sudoku-solver-and-ocr/
"""

import cv2
import imutils
from matplotlib import pyplot as plt


class SudokuFinder:
    def __init__(self):
        self.puzz = None
        self.puzz_grey = None
        self.puzz_gausblur = None
        self.puzz_contour = None
        self.puzz_thresh = None

    def read_img(self, img):
        self.puzz = cv2.imread(img)
        return self.puzz

    def gaussian(self, img):
        self.puzz_gausblur = cv2.GaussianBlur(img, (9, 9), 0)
        return self.puzz_gausblur

    def black_white(self, img):
        self.puzz_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.puzz_grey

    def show(self, name, img):
        cv2.imshow(str(name), img)
        cv2.waitKey(0)

    def threshold(self, img):
        self.puzz_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 5)
        self.puzz_thresh = cv2.bitwise_not(self.puzz_thresh)
        return self.puzz_thresh

    def contour(self, img):
        self.puzz_contour = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.puzz_contour = imutils.grab_contours(self.puzz_contour)
        self.puzz_contour = sorted(self.puzz_contour, key=cv2.contourArea, reverse=True)
        return self.puzz_contour



