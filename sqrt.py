
class Sqrt:

    @staticmethod
    def modulus(x):
        if x < 0:
            return x * (-1)
        else:
            return x

    @staticmethod
    def root(x, x0=10):
        out = [Sqrt.modulus(x0-x)]
        tick = 0
        while True:
            out.append(0.5*(out[tick] + x/out[tick]))
            tick += 1
            if tick == 25:
                break
        return out[tick]
