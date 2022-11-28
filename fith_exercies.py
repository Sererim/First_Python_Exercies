from sqrt import Sqrt


class Distance:

    @staticmethod
    def getdistance(x1, y1, x2, y2, s=None):
        s = (x2 - x1)**2
        s += (y2 - y1)**2
        s = Sqrt.root(s)
        return s


def main():
    while True:
        print("Program is running", end="\n")
        get = []
        for i in range(0, 4):
            if i == 0 or i == 1:
                get.append(int(input("Enter coordinates of the point A (x1, y1).\n")))
            elif i == 2 or i == 3:
                get.append(int(input("Enter coordinates of the point B (x2, y2).\n")))
        print(f"Distance between point A ({get[0]}, {get[1]})"
              f" and point B ({get[2], get[3]}) is:\n"
              f"{Distance.getdistance(get[0], get[1] ,get[2] ,get[3])}")
        print("Do you want to terminate the program Y/y ?.")
        control = str(input())
        if control == "Y" or control == "y":
            break
        else:
            main()
    return 0


if __name__ == "__main__":
    main()
