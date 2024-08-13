import math


class Derivative:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.000001, *args, **kwargs):
        try:
            return (self.__fn(x + dx) - self.__fn(x)) / dx
        except ZeroDivisionError:
            print("Cant divide by zero")
            return 0


def tangent(x):
    return math.tan(x)


tn = Derivative(tangent)


def cotangent(x):
    return 1 / math.tan(x)


ctg = Derivative(cotangent)


def sin(x):
    return math.sin(x)


sin = Derivative(sin)


def cos(x):
    return math.cos(x)


cos = Derivative(cos)

while True:
    print("Enter the value for functions (Enter the number of degrees)")
    z = math.radians(float(input()))

    res = sin(z)
    print(f"The derivative of the sinus of {round(math.degrees(z))} degrees is: {round(res, 4)}")

    res = cos(z)
    print(f"The derivative of the cosine of {round(math.degrees(z))} degrees is: {round(res, 4)}")

    res = tn(z)
    print(f"The derivative of the tangent of {round(math.degrees(z))} degrees is: {round(res, 4)}")

    res = ctg(z)
    print(f"The derivative of the cotangent of {round(math.degrees(z))} degrees is: {round(res, 4)}")
    print("Thank you for choosing us :)")
