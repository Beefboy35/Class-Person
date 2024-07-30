import math


def accuracy(dx=0.00001):
    def wrapper(x, func):
        try:
            return (func(x + dx) - func(x)) / dx
        except ZeroDivisionError:
            print("Cant divide by zero")
            return 0

    return wrapper


def tangent(x):
    return math.tan(x)


def cotangent(x):
    return 1 / math.tan(x)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


while True:
    print("Enter the value for functions (Enter the number of degrees)")
    z = math.radians(float(input()))
    res = accuracy()(z, sin)
    print(f"The derivative of the sinus is: {round(res, 4)}")

    res = accuracy()(z, cos)
    print(f"The derivative of the cosine is: {round(res, 4)}")

    res = accuracy()(z, tangent)
    print(f"The derivative of the tangent is: {round(res, 4)}")

    res = accuracy()(z, cotangent)
    print(f"The derivative of the cotangent is: {round(res, 4)}")
    print("Thank you for choosing us :)")
