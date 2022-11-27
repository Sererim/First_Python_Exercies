from COLOR import Color
from sqrt import Sqrt


class Errors:
    @staticmethod
    def zero(A, B):
        if A[0] == B[0] and A[1] == B[1]:
            print(f"{Color.WARNING}ERROR{Color.END}\n"
                  f"Answer is 0. Did you mistype ?")
            return False


class Distance:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def getdistance(self):
        s = (self.A[1] - self.A[0])**2
        s += (self.B[1] - self.B[0])**2
        return Sqrt.root(s, Sqrt.modulus(self.A[0]))


def main():
    control = ""
    A = []
    B = []
    while True:
        print("Program is running.\n")
        for x in range(0, 2):
            A.append(int(input(f"Enter x{x} for A point.\n")))
        for y in range(0, 2):
            B.append(int(input(f"Enter y{y} for B point.\n")))
        if Errors.zero(A, B):
            main()
        d = Distance(A, B)
        print(f"The distance between points: \n"
              f"A ({A[0]},{A[1]}) and B ({B[0]},{B[1]})\n"
              f"is {d.getdistance()}\n")
        control = str(input("To terminate the program enter Y or y.\n"))
        if control == "Y" or control == "y":
            break
        else:
            main()
    return 0


if __name__ == "__main__":
    main()
