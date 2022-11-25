from COLOR import Color

# Find the position of the point in 2D space
# All possible values of points in specific quadrant of the plane
# Example
#       ^
#  II   |       I Quadrant
#       |
#       |       (*) A (5;6)
# ------+--------->
#       |
#  III  |       IV
#       |
#       
# (*) A with coordinates (5;6) is in the first quadrant 



class Plane:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        pass
    def findquadrant(self):
        if self.X > 0 and self.Y > 0:
            print("Point is in the first quadrant")
        elif self.X < 0 and self.Y > 0:
            print("Point is in the second quadrant")
        elif self.X < 0 and self.Y < 0:
            print("Point is in the third quadrant")
        elif self.X > 0 and self.Y < 0:
            print("Point is in the fourth quadrant")
        else:
            print("")




def main():



if __name__ == "__main__":
    main()