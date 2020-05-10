import numpy as np
from sympy import *


class Matrix_Operations:
    def __init__(self):
        self.s = symbols("λ")
        init_printing(pretty_print=True)

    def __get_input(self):
        """Gets input from user as a string and generates a matrix.

        Returns:
            Matrix -- Sympy Matrix
        """
        print("\n\nThe following rules must be followed to while entering the values of the matrix:")
        print("=> Add a \",\" after each elemnet in a row.\n=> After each row add a \";\".")
        print("Example: 1,2,-3;4,-5,6;-7,8,9")
        str = input("Enter the matrix here: ")
        push = []
        for row in str.split(";"):
            dummy = []
            for number in row.split(","):
                try:
                    number = int(number)
                except:
                    number = float(number)
                dummy.append(number)
            push.append(dummy)
        Mat = Matrix(push)
        return Mat

    def __si_am(self, Mat_A):
        n, m = Mat_A.shape
        Mat = ((self.s*eye(n)) -
               Mat_A) if n == m else print("Error!: ", ShapeError(NonSquareMatrixError))
        print("λI-A matrix:")
        pprint(Mat)
        return Mat

    def __char_eq(self, Mat):
        eqn = expand(Mat.det())
        print("\nThe Characteristic equation is: ")
        print(eqn)
        return eqn

    def main(self):
        A = self.__get_input()
        si_am = self.__si_am(A)
        char_eq = self.__char_eq(si_am)
        # roots
        # co


if __name__ == "__main__":
    mat = Matrix_Operations()
    mat.main()
