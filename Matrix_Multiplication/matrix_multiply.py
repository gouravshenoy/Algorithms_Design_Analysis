__author__ = 'Gaurav-PC'

import time
import random
import argparse


class MatrixMultiply:
    """
    Class for performing Matrix Multiplication using:
        1. Standard Recursive Matrix Multiplication
        2. Matrix Multiplication using Strassens Algorithm
    """

    def __init__(self):
        return

    """
    Matrix is represented as follows:

    [ 1  2 ]  = [ [1,2], [3,4] ]
    [ 3  4 ]

    """
    @classmethod
    def matrix_generate(cls, size):
        """
        Method generates a square matrix of size NxN
        Here N = size
        :param size:
        :return:
        """
        matrix = []

        for i in range(0, size):
            sub_mat = []
            for j in range(0, size):
                # generate random number
                # add it to sub matrix
                sub_mat.append(random.randint(1,9))

            # add sub matrix to main matrix
            matrix.append(sub_mat)

        return matrix

    """
    Method to sum 2 square matrices:

    [ 1  2 ]  +  [ 5  6 ]  =  [ 6    8 ]
    [ 3  4 ]     [ 7  8 ]     [ 10  12 ]
    """
    @classmethod
    def matrix_add(cls, matrixA, matrixB, subtract=False):
        """
        Method to sum 2 matrices
        :param matrixA:
        :param matrixB:
        :return:
        """
        matrixSum = []

        for i in range(len(matrixA)):
            subMatrixA, subMatrixB = matrixA[i], matrixB[i]
            if subtract is True:
                matrixSum.append([(x-y) for x,y in zip(subMatrixA, subMatrixB)])
            else:
                matrixSum.append([(x+y) for x,y in zip(subMatrixA, subMatrixB)])

        return matrixSum

    """
    Divides as follows:

    [ 1  2 ]  =>  [ 1 ] , [ 2 ] , [ 3 ] , [ 4 ]
    [ 3  4 ]

    """
    @classmethod
    def matrix_divide(cls, matrix):
        """
        Method to divide a N x N matrix into
            four N/2 x N/2 submatrices
        :param matrix:
        :return:
        """
        submatrix_1 = []
        submatrix_2 = []
        submatrix_3 = []
        submatrix_4 = []
        submatrix_size = len(matrix) / 2

        for i in range(len(matrix)):
            if i < submatrix_size:
                submatrix_1.append(matrix[i][:submatrix_size])
                submatrix_2.append(matrix[i][submatrix_size:])
            else:
                submatrix_3.append(matrix[i][:submatrix_size])
                submatrix_4.append(matrix[i][submatrix_size:])

        return submatrix_1, submatrix_2, submatrix_3, submatrix_4

    """
    Combines matrices as follows:

    [ 1 ] , [ 2 ] , [ 3 ] , [ 4 ]  =>  [ 1  2 ]
                                       [ 3  4 ]

    """
    @classmethod
    def matrix_combine(cls, matrixC1, matrixC2, matrixC3, matrixC4):
        """
        Method to combine four N/2 x N/2 matrices into one N x N matrix
        :param matrixC1:
        :param matrixC2:
        :param matrixC3:
        :param matrixC4:
        :return:
        """
        combined_matrix = []
        base_size = len(matrixC1)

        for i in range(base_size * 2):
            if i < base_size:
                sub_matrix = matrixC1[i % base_size] + matrixC2[i % base_size]
            else:
                sub_matrix = matrixC3[i % base_size] + matrixC4[i % base_size]

            combined_matrix.append(sub_matrix)

        return combined_matrix

    """
    Multiplication (Recursive) follows:

    [ 8  1 ] x [ 8  8 ]  =  [ 69  70 ]
    [ 3  4 ]   [ 5  6 ]     [ 44  48 ]

    """
    @classmethod
    def matrix_multiply(cls, matrixA, matrixB):
        """
        Method to multiply 2 N x N matrices (N = 2^k)
            using recursion
        :param matrixA:
        :param matrixB:
        :return:
        """

        if len(matrixA) == 1:
            # base case for recursion, when size = 1x1 matrix
            return [[matrixA[0][0] * matrixB[0][0]]]
        else:
            # divide matrixA into 4 quadrants
            matrix_a11, matrix_a12, matrix_a21, matrix_a22 = cls.matrix_divide(matrixA)

            #divide matrixB into 4 quadrants
            matrix_b11, matrix_b12, matrix_b21, matrix_b22 = cls.matrix_divide(matrixB)

            # recursively multiply & add
            matrix_c11 = cls.matrix_add(cls.matrix_multiply(matrix_a11, matrix_b11),
                                        cls.matrix_multiply(matrix_a12, matrix_b21))

            matrix_c12 = cls.matrix_add(cls.matrix_multiply(matrix_a11, matrix_b12),
                                        cls.matrix_multiply(matrix_a12, matrix_b22))

            matrix_c21 = cls.matrix_add(cls.matrix_multiply(matrix_a21, matrix_b11),
                                        cls.matrix_multiply(matrix_a22, matrix_b21))

            matrix_c22 = cls.matrix_add(cls.matrix_multiply(matrix_a21, matrix_b12),
                                        cls.matrix_multiply(matrix_a22, matrix_b22))

            # combine results
            matrixC = cls.matrix_combine(matrix_c11, matrix_c12, matrix_c21, matrix_c22)

            return matrixC


    """
    Multiplication(Strassens Algo) follows:

    [ 8  1 ] x [ 8  8 ]  =  [ 69  70 ]
    [ 3  4 ]   [ 5  6 ]     [ 44  48 ]

    """
    @classmethod
    def strassens_matrix_multiply(cls, matrixA, matrixB):
        """
        Method to multiply 2 N x N matrices (N = 2^k)
            using strassens algorithm
        :param matrixA:
        :param matrixB:
        :return:
        """

        # divide matrixA into 4 quadrants
        matrix_a11, matrix_a12, matrix_a21, matrix_a22 = cls.matrix_divide(matrixA)

        #divide matrixB into 4 quadrants
        matrix_b11, matrix_b12, matrix_b21, matrix_b22 = cls.matrix_divide(matrixB)

        # (A11 + A22)*(B11 + B22)
        P = cls.matrix_multiply(
            cls.matrix_add(matrix_a11, matrix_a22),
            cls.matrix_add(matrix_b11, matrix_b22)
        )

        # (A21 + A22) * B11
        Q = cls.matrix_multiply(
            cls.matrix_add(matrix_a21, matrix_a22),
            matrix_b11
        )

        # A11 * (B12 - B22)
        R = cls.matrix_multiply(
            matrix_a11,
            cls.matrix_add(matrix_b12, matrix_b22, subtract=True)
        )

        # A22 * (B21 - B11)
        S = cls.matrix_multiply(
            matrix_a22,
            cls.matrix_add(matrix_b21, matrix_b11, subtract=True)
        )

        # (A11 + A12) * B22
        T = cls.matrix_multiply(
            cls.matrix_add(matrix_a11, matrix_a12),
            matrix_b22
        )

        # (A21 - A11) * (B11 + B12)
        U = cls.matrix_multiply(
            cls.matrix_add(matrix_a21, matrix_a11, subtract=True),
            cls.matrix_add(matrix_b11, matrix_b12)
        )

        # (A12 - A22) * (B21 + B22)
        V = cls.matrix_multiply(
            cls.matrix_add(matrix_a12, matrix_a22, subtract=True),
            cls.matrix_add(matrix_b21, matrix_b22)
        )

        # use strassens formula
        matrix_c11 = cls.matrix_add(
            cls.matrix_add(P, V),
            cls.matrix_add(S, T, subtract=True)
        )

        matrix_c21 = cls.matrix_add(Q, S)
        matrix_c12 = cls.matrix_add(R, T)

        matrix_c22 = cls.matrix_add(
            cls.matrix_add(P, U),
            cls.matrix_add(R, Q, subtract=True)
        )

        # combine results
        matrixC = cls.matrix_combine(matrix_c11, matrix_c12, matrix_c21, matrix_c22)

        return matrixC

    """
    Prints Matrix as follows:

           0   1
        0 [69, 70]
        1 [44, 48]

    """
    @classmethod
    def matrix_print(cls, matrix):
        """
        Method to print matrix
        :param matrix:
        :return:
        """
        print '  ',
        for i in range(len(matrix[0])):
              print i, '',
        print
        for i, element in enumerate(matrix):
              print i, ''.join(str(element))

"""
Main method
"""
if __name__ == '__main__':

    # define the arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('SIZE', help='Size of Square Matrix for Multiplication. SIZE = 2^k')
    args = parser.parse_args()

    # read the commandline argument
    mat_size = int(args.SIZE)

    obj = MatrixMultiply()

    # generate random matrix content for mat size
    matrixA = obj.matrix_generate(mat_size)
    matrixB = obj.matrix_generate(mat_size)

    # TEST DATA
    # matrixA = [[8,2], [8,5]]
    # matrixB = [[1,3], [9,2]]

    # matrixA = [[3,2,1,6], [5,4,2,3], [7,1,6,5], [2,9,8,3]]
    # matrixB = [[6,1,3,4], [2,5,6,1], [3,2,4,7], [9,5,6,3]]

    print('Matrix A:')
    obj.matrix_print(matrixA)

    print('\nMatrix B:')
    obj.matrix_print(matrixB)

    start_time = time.time()
    matrixC = obj.matrix_multiply(matrixA, matrixB)
    end_time = time.time()

    print('\nStandard Matrix Multiplication:')
    print("--- %s seconds ---" % (end_time - start_time))

    start_time = time.time()
    strassens_matrixC = obj.strassens_matrix_multiply(matrixA, matrixB)
    end_time = time.time()

    print('\nStrassens Matrix Multiplication:')
    print("--- %s seconds ---" % (end_time - start_time))

    print('\n Standard Matrix Multiplication Result ==>')
    obj.matrix_print(matrixC)

    print('\n Strassens Matrix Multiplication Result ==>')
    obj.matrix_print(strassens_matrixC)

    # a,b,c,d = obj.matrix_divide(matrixA)
    # print('\n a:')
    # print(a)
    # obj.matrix_print(a)
    # print('\n b:')
    # obj.matrix_print(b)
    # print('\n c:')
    # obj.matrix_print(c)
    # print('\n d:')
    # obj.matrix_print(d)

    # matrixA = [[3]]
    # matrixB = [[4]]
    # sumMatrix = obj.matrix_add(matrixA, matrixB)
    #
    # print('\nMatrix Sum:')
    # obj.matrix_print(sumMatrix)

    # m1 = [[1,2,3,4], [9,10,11,12], [17,18,19,20], [25,26,27,28]]
    # m2 = [[5,6,7,8], [13,14,15,16], [21,22,23,24], [29,30,31,32]]
    # m3 = [[33,34,35,36], [41,42,43,44], [49,50,51,52], [57,58,59,60]]
    # m4 = [[37,38,39,40], [45,46,47,48], [53,54,55,56], [61,62,63,64]]
    #
    # combined = obj.matrix_combine(m1, m2, m3, m4)
    #
    # print('\n Combined Matrix:')
    # obj.matrix_print(combined)

