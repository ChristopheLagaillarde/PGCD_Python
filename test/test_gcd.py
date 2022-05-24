# Program : test_gcd
# Description : test the function gcd
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from gcd import gcd


def test_gcd():
    assert (gcd(3, 5) == 1), "the program does not work for gcd(3, 5)"


test_gcd()
