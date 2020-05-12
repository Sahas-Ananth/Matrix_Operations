import numpy as np
from sympy import *

# 0,1,0;0,0,1;-6,-11,-6


class Matrix_Operations:
    def __init__(self):
        self.s = symbols("lamda")
        init_printing(pretty_print=True)
        print("\n\nThe following rules must be followed to while entering the values of the matrix:")
        print("=> Add a \",\" after each elemnet in a row.\n=> After each row add a \";\". \n=> Write \"None\" if you don't have the matrix")
        print("Example: 1,2,-3;4,-5,6;-7,8,9")

    def __get_input(self, Name):
        """Gets input from user as a string and generates a matrix.

        Returns:
            Matrix -- Sympy Matrix
        """
        print("\n\nNow, you are about to enter %s Matrix" % Name)
        str = input("Enter the matrix here: ")
        push = []
        if str == "None":
            pass
        else:
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
        print("\nThe %s Matrix you have entered is: " % Name)
        pprint(Mat)
        return Mat

    def __si_am(self, Mat_A):
        n, m = Mat_A.shape
        Mat = ((self.s*eye(n)) -
               Mat_A) if n == m else print("Error!: ", ShapeError(NonSquareMatrixError))
        print("\nλI-A matrix:")
        pprint(Mat)
        return Mat

    def __char_eq(self, Mat):
        eqn = expand(Mat.det())
        print("\nThe Characteristic equation is: ")
        pprint(eqn)
        return eqn

    def __roots(self, eqn):
        sols = roots(eqn, self.s)
        print("\nRoots of the Characteristic equation is: ")
        [[print("λ = ", key, end="\t\t")for i in range(value)]
         for key, value in sols.items()]
        return sols

    def __Cofactor_Matrix(self, Mat):
        Cf_mat = Mat.cofactor_matrix()
        print("\n\nCoFactor Matrix: ")
        cf = Cf_mat.row(0).T
        pprint(expand(cf))
        return cf

    def __ModalMatrix(self, Mat, sols):
        mm = Matrix()
        for key, value in sols.items():
            dummy = Matrix()
            while value > 0:
                di = Derivative(Mat, self.s, value-1, evaluate=True)
                f = lambdify(self.s, di, "numpy")
                dummy = dummy.col_insert(
                    value-1, Matrix((f(key)/np.gcd.reduce(f(key)))))
                value -= 1
            mm = mm.row_join(dummy)
        print("\nModal Matrix:")
        pprint(mm)
        print("\n Inverse Modal Matrix:")
        pprint(mm**-1)
        return mm

    def __finalStep(self, M, Amat, Bmat, Cmat):
        A_bar = (M**-1)*Amat*M
        B_bar = (M**-1)*Bmat
        C_bar = Cmat*M
        print("\nNew A Matrix:")
        pprint(A_bar)
        print("\nNew B Matrix:")
        pprint(B_bar)
        print("\nNew C Matrix:")
        pprint(C_bar)
        return A_bar, B_bar, C_bar

    def main(self):
        A = self.__get_input("A")
        B = self.__get_input("B")
        C = self.__get_input("C")
        # D = self.__get_input("D")
        si_am = self.__si_am(A)
        char_eq = self.__char_eq(si_am)
        roots = self.__roots(char_eq)
        co_fac_row = self.__Cofactor_Matrix(si_am)
        mm = self.__ModalMatrix(co_fac_row, roots)
        Na, Nb, Nc = self.__finalStep(mm, A, B.T, C)


if __name__ == "__main__":
    mat = Matrix_Operations()
    mat.main()
