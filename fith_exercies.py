from COLOR import Color
from sqrt import Sqrt


class Distance:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def getdistance(self):
        s = (self.A[1] - self.A[0])**2
        s += (self.B[1] - self.B[0])**2
        return Sqrt.root(sum)

def main():
    control = ""
    A = []
    B = []
    while True:
        print("Program is running")
        for x in range(0,2):
            A.append(int(input(f"Enter x{x} for A point")))
        for x in range(0, 2):
            B.append(int(input(f"Enter x{x} for A point")))




if __name__ == "__main__":
    main()
