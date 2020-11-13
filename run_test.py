# coding: utf-8

import sys
import os
import re

import unittest

import numpy as np

import numpy_exercises as exercise


A = np.array([[ 0, -5,  6, -2, -7,  4],
              [-1,  1, -3,  3,  4,  5],
              [ 8,  6,  8,  1,  8, -2],
              [ 5,  7,  0, -6, -4,  2],
              [-4, -6, -7,  0,  2, -1],
              [-7,  2,  8, -5,  1,  4]])


class TestReplaceZeros(unittest.TestCase):
    def setUp(self):
        self.A = A

    def test_replace_zeros(self):
        res = np.array([[10, -5,  6, -2, -7,  4],
                        [-1,  1, -3,  3,  4,  5],
                        [ 8,  6,  8,  1,  8, -2],
                        [ 5,  7, 10, -6, -4,  2],
                        [-4, -6, -7, 10,  2, -1],
                        [-7,  2,  8, -5,  1,  4]])
        exercise.replace_zeros(self.A, 10)
        np.testing.assert_equal(A, res)


class TestCenter(unittest.TestCase):
    def setUp(self):
        self.A = A.copy()

    def test_center(self):
        res = A - np.average(A.ravel())
        np.testing.assert_allclose(exercise.centered(self.A), res)

    def test_A_unchanged(self):
        exercise.centered(A)
        np.testing.assert_equal(A, self.A)


class TestBelowDiagonal(unittest.TestCase):

    def setUp(self):
        self.A = A.copy()

    def test_below_diagonal(self):
        a = A.copy()
        j, i = np.meshgrid(range(a.shape[0]), range(a.shape[1]))
        a[j >= i] = 0.
        np.testing.assert_allclose(exercise.below_diagonal(self.A), sum(a, 0))


class TestCheckboard(unittest.TestCase):
    def test_checkboard_odd(self):
        np.testing.assert_equal(exercise.checkboard(5),
                                np.array([[ 1.,  0.,  1.,  0.,  1.],
                                          [ 0.,  1.,  0.,  1.,  0.],
                                          [ 1.,  0.,  1.,  0.,  1.],
                                          [ 0.,  1.,  0.,  1.,  0.],
                                          [ 1.,  0.,  1.,  0.,  1.]]))

    def test_checkboard_even(self):
        np.testing.assert_equal(exercise.checkboard(4),
                                np.array([[ 1.,  0.,  1.,  0.],
                                          [ 0.,  1.,  0.,  1.],
                                          [ 1.,  0.,  1.,  0.],
                                          [ 0.,  1.,  0.,  1.]]))

if __name__ == '__main__':
    unittest.main()