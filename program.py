#!/usr/bin/env python3

# Created by: Igor
# Created on: Nov 2021
# This program uses quadratic formula

import math


def quadratic(a, b, c, add):
    # this function calculate x1 and x2

    x_1 = -b / (2 * a)
    x_2 = math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    if add == True:
        return x_1 + x_2
    else:
        return x_1 - x_2


def main():
    # This program uses quadratic formula

    # input
    integer1 = input("Enter a: ")
    integer2 = input("Enter b: ")
    integer3 = input("Enter c: ")
    print("")

    # process
    try:
        a_1 = float(integer1)
        b_1 = float(integer2)
        c_1 = float(integer3)
        d = b_1 ** 2 - 4 * a_1 * c_1
        if d < 0:
            print("There is no answer")
        elif d == 0:
            answer = quadratic(a=a_1, b=b_1, c=c_1, add=True)
            print("If the quadratic equation looks like this:")
            print("{0}x² + {1}x + {2}".format(a_1, b_1, c_1))
            print("Discriminant = {0}".format(d))
            print("x = {0}".format(answer))
        else:
            answer1 = quadratic(add=True, a=a_1, c=c_1, b=b_1)
            answer2 = quadratic(b=b_1, c=c_1, a=a_1, add=False)
            print("If the quadratic equation looks like this:")
            print("{0}x² + {1}x + {2}".format(a_1, b_1, c_1))
            print("Discriminant = {0}".format(d))
            print("x = {0} or {1}".format(answer1, answer2))
    except Exception:
        print("Invalid input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
