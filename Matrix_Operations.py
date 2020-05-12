import numpy as np
from sympy import *


class Matrix_Operations:
    def __init__(self):
        """Initializing function
        """
        self.s = symbols("lamda")
        init_printing(pretty_print=True)
        print("\n\nThe following rules must be followed to while entering the values of the matrix:")
        print("=> Add a \",\" after each elemnet in a row.\n=> After each row add a \";\". \n=> Write \"None\" if you don't have the matrix")
        print("Example: 1,2,-3;4,-5,6;-7,8,9")

    def __get_input(self, Name):
        """Gets input from user as a string and generates a matrix.

        Arguments:
            Name {String} -- Its just used to print a name.

        Returns:
            Matrix -- User entered Matrix.
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
        """Creates λ*I - A matrix.

        Arguments:
            Mat_A {Matrix} -- Input A Matrix.

        Returns:
            Matrix -- Lamda*I-A Matrix is returned.
        """
        n, m = Mat_A.shape
        Mat = ((self.s*eye(n)) -
               Mat_A) if n == m else print("Error!: ", ShapeError(NonSquareMatrixError))
        print("\nλI-A matrix:")
        pprint(Mat)
        return Mat

    def __char_eq(self, Mat):
        """Finds the characteristic equation for the input matrix.

        Arguments:
            Mat {Matrix} -- Matrix whose characteristic equation must be converted.

        Returns:
            Equation -- An equation which is the characteristic equation.
        """
        eqn = expand(Mat.det())
        print("\nThe Characteristic equation is: ")
        pprint(eqn)
        return eqn

    def __roots(self, eqn):
        """Returns roots of the input equation.

        Arguments:
            eqn {Equation} -- The equation for which roots must be found.

        Returns:
            Dictionary -- Returns the roots as keys of the dictionary with values being their multiplicity.
        """
        sols = roots(eqn, self.s)
        print("\nRoots of the Characteristic equation is: ")
        [[print("λ = ", key, end="\t\t")for i in range(value)]
         for key, value in sols.items()]
        return sols

    def __Cofactor_Matrix(self, Mat):
        """Returns the CoFactor Matrix(only the first row).

        Arguments:
            Mat {Matrix} -- The Matrix whose Cofactor matrix must be found.

        Returns:
            Matrix -- The 1st row of the cofactor matrix.
        """
        Cf_mat = Mat.cofactor_matrix()
        print("\n\nCoFactor Matrix: ")
        cf = Cf_mat.row(0).T
        pprint(expand(cf))
        return cf

    def __ModalMatrix(self, Mat, sols):
        """Generates the Modal Matrix of the given matrix.

        Arguments:
            Mat {Matrix} -- The Matrix with which Modal Matrix must be found.
            sols {Dicitionary} -- A dictionary with roots as keys and their multiplicity as values.

        Returns:
            Matrix -- Modal matrix is returned.
        """
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
        """Final steps to finish the sum is calculated here.

        Arguments:
            M {Matrix} -- Modal Matrix.
            Amat {Matrix} -- A Matrix.
            Bmat {Matrix} -- B Matrix.
            Cmat {Matrix} -- C Matrix.

        Returns:
            Matrices -- Returns new A,B,C Matrices.
        """
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
        """Main fuction to call other functions.
        """
        A = self.__get_input("A")
        B = self.__get_input("B")
        C = self.__get_input("C")
        si_am = self.__si_am(A)
        char_eq = self.__char_eq(si_am)
        roots = self.__roots(char_eq)
        co_fac_row = self.__Cofactor_Matrix(si_am)
        mm = self.__ModalMatrix(co_fac_row, roots)
        Na, Nb, Nc = self.__finalStep(mm, A, B.T, C)
        cont = input("Do you want to do one more sum? [y]/[n]: ")
        self.main() if cont == "y" else None


if __name__ == "__main__":
    mat = Matrix_Operations()
    mat.main()
