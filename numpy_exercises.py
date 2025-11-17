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

    
    try:
        n = int(n) # converting to integer for safety

    # if it's not an integer, flag an error
    except (ValueError, Exception):
        print(f'Oops! Either value "{n}" can\'t be converted to an integer or we have a bigger problem')
        
        return


    # let's create the array we'll modify. It'll be a "zeros" array
    the_array = np.zeros((n, n))

    # now we'll loop through how many rows/columns the array has
    for x in range(n):

        # we'll access the array row by row:
        # if the row is an odd one (e.g: row 1, 3, 5, 7), replace every value in the row with a "1"
        if x % 2 == 1:
            
            the_array[x, :] = np.ones(n) # here we replace all values in the row with "1" if it's an odd one

            the_array[x, ::2] = 0 # then we replace every column 2 columns in that row with a "0"

        # if the row is an even one, replace every 2 columns with a "1", directly

        elif x % 2 == 0:

            the_array[x, ::2] = 1

        # else just get out of this function
        else:

            return

    # print the modified array
    print(the_array)

    