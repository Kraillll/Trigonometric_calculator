import math

def func():
    try:
        print("This is trigonometric calculator")
        print("Aviable functions: sin, cos, tan, ctg, and also arcsin, arccos, arctan, arcctg.")

        print(f"Enter type of function:", end="")
        x = str(input())
        if x in ["sin", "cos", "tan", "ctg"]:
            print(f"Enter the measure of the angle:", end="")

        else:
            print(f"Enter the function value: ", end="")

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
                res = math.tan(1 / angle)

            if res != None:
                print(res)

        if x in ["arcsin", "arccos"] and not (-1 <= angle <= 1):
            print("Math ERROR")
            return

        elif (x == "arcsin"):
            res = math.asin(angle)

        elif (x == "arccos"):
            res = math.acos(angle)

        elif (x == "arctan"):
            res = math.atan(angle)

        elif (x == "arcctg"):
            res = math.atan(1 / angle)

        if x in ["arcsin", "arccos", "arctan", "arcctg"] and (res != None):
            res = math.degrees(res)
            print(res)

    except Exception as e:
        print("Syntax ERROR:", e)


func()
