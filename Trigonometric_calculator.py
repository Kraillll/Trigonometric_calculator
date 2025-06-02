import math

def func():
    try:
        print("This is trigonometric calculator")
        print("Aviable functions: cos, sin, tan, ctg, and also arcsin, arccos, arctan, arcctg.")

        print(f"Enter type of function:", end="")
        x = str(input())
        print(f"Enter the measure of the angle:", end="")
        angle = float(input())
        res = None
        if x in ["sin", "cos", "tan", "ctg"]:
            angle = math.radians(angle)
            if (x == "sin"):
                res = math.sin(angle)

            elif (x == "cos"):
                res = math.cos(angle)

            elif (x == "tan"):
                res = math.tan(angle)

            elif (x == "ctg"):
                res = 1 / math.tan(angle)
                
        if x == "arcsin" or x == "arccos" and angle < -1 or angle > 1:
            print("Math ERROR")

        elif (x == "arcsin"):
            res = math.asin(angle)
            if angle < -1 or angle > 1:
                print("Math ERROR")

        elif (x == "arccos"):
            res = math.acos(angle)
            if angle < -1 or angle > 1:
                print("Math ERROR")

        elif (x == "arctan"):
            res = math.atan(angle)

        elif (x == "arcctg"):
            res = 1 / math.atan(angle)

        if res != None:
            print(res)

    except:
        print("Syntax ERROR")

func()
