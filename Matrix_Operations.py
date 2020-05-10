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

    def __roots(self, eqn):
        sols = roots(eqn, self.s)
        print("\nRoots of the Characteristic equation is: ")
        [[print("λ = ", key, end="\t\t")for i in range(value)]
         for key, value in sols.items()]
        return sols

    def __Cofactor_Matrix(self, Mat):
        Cf_mat = expand(Mat.cofactor_matrix())
        print("\nCoFactor Matrix: ")
        pprint(Cf_mat.row(0))
        return Cf_mat.row(0)

    def __ModalMatrix(self, Mat, sols):
        mm = Matrix()
        for key, value in sols.items():
            dummy = Matrix()
            while value > 0:
                f = Derivative(Mat, self.s, value-1, evaluate=True)
                dummy.row_insert(value-1, Matrix(f(key)))
                value -= 1
            mm.col_join(dummy)
        pprint(mm)
        return mm

    def main(self):
        A = self.__get_input()
        si_am = self.__si_am(A)
        char_eq = self.__char_eq(si_am)
        roots = self.__roots(char_eq)
        co_fac_row = self.__Cofactor_Matrix(si_am)
        mm = self.__ModalMatrix(co_fac_row, roots)


if __name__ == "__main__":
    mat = Matrix_Operations()
    mat.main()
