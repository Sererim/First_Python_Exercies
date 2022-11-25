from COLOR import Color
"""
 Find the position of the point in 2D space
 All possible values of points in specific quadrant of the plane
 Example
       ^
  II   |       I Quadrant
       |
       |       (*) A (5;6)
 ------+--------->
       |
  III  |       IV
       |
       
(*) A with coordinates (5;6) is in the first quadrant
"""

class Plane:
    @staticmethod
    def findquadrant(x, y):
        if x > 0 and y > 0:
            print("Point is in the first quadrant")
        elif x < 0 < y:
            print("Point is in the second quadrant")
        elif x < 0 and y < 0:
            print("Point is in the third quadrant")
        elif x > 0 > y:
            print("Point is in the fourth quadrant")
        else:
            print(f"{Color.WARNING}ERROR{Color.END}")
            return False
        return True

    @staticmethod
    def findallowedvalues(quad):
        allowed = ("I", "1", "II", "2", "III", "3", "IV", "4")
        if quad == allowed[0] or allowed[1]:
            print("X ∈ (0;+∞)\nY ∈ (0;+∞)")
        elif quad == allowed[2] or allowed[3]:
            print("X ∈ (-∞;0)\nY ∈ (0;+∞)")
        elif quad == allowed[4] or allowed[5]:
            print("X ∈ (-∞;0)\nY ∈ (-∞;0)")
        elif quad == allowed[6] or allowed[7]:
            print("X ∈ (0;+∞)\nY ∈ (-∞;0)")
        else:
            print(f"{Color.WARNING}ERROR{Color.END}")
            return False
        return True


def main():
    while True:
        print("Program is running.")
        control = str(input("Enter 1 to find a quadrant of a point.\n"
                            "Enter 2 to find values of x and y coordinates in the quadrant.\n"))
        if control == "1":
            x, y = 0, 0
            x = int(input("Enter X:\n"))
            y = int(input("Enter Y:\n"))
            if not Plane.findquadrant(x, y):
                print(f"{Color.WARNING}ERROR{Color.END}")
                main()
        elif control == "2":
            control = str(input("Enter the quadrant.\nExample I or 1 for the first quadrant.\n"))
            if not Plane.findallowedvalues(control):
                print(f"{Color.WARNING}ERROR{Color.END}")
                main()
        else:
            print(f"{Color.WARNING}ERROR{Color.END}")
            main()
        control = str(input("Enter Y or y to terminate the program.\n"))
        if control == "Y" or control == "y":
            break
        else:
            main()
    return 0


if __name__ == "__main__":
    main()
