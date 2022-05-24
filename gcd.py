# Program : gcd
# Description : give the gcd of 2 numbers
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0


def gcd(number1: int, number2: int) -> int:
    if number1 < number2:
        temp = number1
        number1 = number2
        number2 = temp

    remain = number1 % number2

    while remain != 0:
        number1 = number2
        number2 = remain
        remain = number1 % number2

    else:
        return number2
