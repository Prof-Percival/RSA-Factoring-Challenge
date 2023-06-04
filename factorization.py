#/usr/bin/env python3
import sys


def primef(number):
    if number <= 3:
        return int(number)
    if number % 2 == 0:
        return 2
    elif number % 3 == 0:
        return 3
    else:
        for i in range(5, int((number)**0.5) + 1, 6):
            if number % i == 0:
                return int(i)
            if number % (i + 2) == 0:
                return primef(number/(i+2))
    return int(number)


print(primef(int(sys.argv[1])))
