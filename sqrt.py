
class Sqrt:

    @staticmethod
    def root(x, x0=10):
        out = [x0]
        tick = 0
        while True:
            out.append(0.5*(out[tick] + x/out[tick]))
            tick += 1
            if tick == 10:
                break
        return out[tick]
