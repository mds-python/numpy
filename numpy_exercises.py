import numpy as np


def replace_zeros(A, x):
    """
    Function modifies the array `A` (of any shape) by replacing all zero elements with `x`.
    """
    # Your code here


def centered(A):
    """
    Function returns an array made of the array `A` (of any shape) in such a way that from each
    of its elements it subtracts the arithmetic mean of all elements of `A`. The array `A` itself
    remains unchanged.
    """
    # Your code here


def below_diagonal(A):
    """
    Function, for a square array `A` (any size greater than 1), creates a one-dimensional array whose
    k-th element is the sum of the elements of the k-th column of `A` below the main diagonal.
    """
    # Your code here


def checkboard(n):
    """Function creates (and returns) a square array NumPy with alternating ones and zeros of the size
    given by the invocation argument `n`, in the form:

        >>> checkboard(2)
        array([[ 1.,  0.],
               [ 0.,  1.]])

        >>> checkboard(3)
        array([[ 1.,  0.,  1.],
               [ 0.,  1.,  0.],
               [ 1.,  0.,  1.]])

        >>> checkboard(4)
        array([[ 1.,  0.,  1.,  0.],
               [ 0.,  1.,  0.,  1.],
               [ 1.,  0.,  1.,  0.],
               [ 0.,  1.,  0.,  1.]])

        >>> checkboard(5)
        array([[ 1.,  0.,  1.,  0.,  1.],
               [ 0.,  1.,  0.,  1.,  0.],
               [ 1.,  0.,  1.,  0.,  1.],
               [ 0.,  1.,  0.,  1.,  0.],
               [ 1.,  0.,  1.,  0.,  1.]])
    """
    # Your code here
