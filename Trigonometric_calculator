import math

def func():
    print("This is trigonometric calculator")
    print("Aviable functions: cos, sin, tan, and also arcsin, arccos, arctan.")

    print(f"Enter type of function:", end="")
    x = str(input())
    print(f"Enter the measure of the angle:", end="")
    angle = float(input())
    if x in ["sin", "cos", "tan"]:
        angle = math.radians(angle)
        if (x == "sin"):
            res = math.sin(angle)
            print(res)

        elif (x == "cos"):
            res = math.cos(angle)
            print(res)

        elif (x == "tan"):
            res = math.tan(angle)
            print(res)

        else:
            print("Syntax ERROR")

    elif (x == "arcsin"):
        res = math.asin(angle)
        print(res)
        if (angle < -1, angle > 1):
            print("Math ERROR")

    elif (x == "arccos"):
        res = math.acos(angle)
        print(res)
        if (angle < -1, angle > 1):
            print("Math ERROR")

    elif (x == "arctan"):
        res = math.atan(angle)

    else:
        print("Syntax ERROR")

func()
