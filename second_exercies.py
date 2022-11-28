"""
 not (X or Y or Z) = (not X) and (not Y) and (not Z)
"""


class Logic:
    @staticmethod
    def no(x):
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 8):
            if x[i] == 0:
                out[i] = 1
            else:
                out[i] = 0
        return out

    @staticmethod
    # (not X) and (not Y) and (not Z)
    def right(x, y, z):
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 8):
            if x[i] == y[i] == z[i] == 1:
                out[i] = 1
            else:
                out[i] = 0
        return out

    @staticmethod
    #  not (X or Y or Z)
    def left(x, y, z):
        out = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, 8):
            if x[i] == y[i] == z[i] == 1:
                out[i] = 1
            elif x[i] == 1 or y[i] == 1 or z[i] == 1:
                out[i] = 1
            else:
                out[i] = 0
        return out

    @staticmethod
    def compare(x, y):
        num = 0
        for i in range(0, 8):
            if x[i] == y[i]:
                num += 1
        if num == 8:
            return True
        else:
            return False


def main():
    x = (0, 0, 0, 0, 1, 1, 1, 1)
    y = (0, 0, 1, 1, 0, 0, 1, 1)
    z = (0, 1, 0, 1, 0, 1, 0, 1)
    out1 = [0, 0, 0, 0, 0, 0, 0, 0]
    out2 = [0, 0, 0, 0, 0, 0, 0, 0]
    out3 = [0, 0, 0, 0, 0, 0, 0, 0]
    print(f"\nX = {x}\nY = {y}\nZ = {z}\n")
    # (not X) and (not Y) and (not Z)
    out1 = Logic.no(x)
    out2 = Logic.no(y)
    out3 = Logic.no(z)
    out3 = Logic.right(out1, out2, out3)
    print(f"(not X) and (not Y) and (not Z) = {out3}\n")
    # not (X or Y or Z)
    out2 = Logic.left(x, y, z)
    out2 = Logic.no(out2)
    print(f"not (X or Y or Z) = {out2}\n")
    print(f"not (X or Y or Z) = (not X) and (not Y) and (not Z) ?\n"
          f"{Logic.compare(out2, out3)}")
    return 0


if __name__ == "__main__":
    main()
