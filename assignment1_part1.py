#!/usr/bin/env python
# -*- coding: utf-8 -*-

def listDivide(numbers, divide=2):
    elements = 0
    for n in numbers:
        if n % divide == 0:
            elements += 1
    return elements

class ListDivideException(Exception):
    pass

def testListDivide():
    try:
        if listDivide([1, 2, 3, 4, 5]) != 2:
            raise ListDivideException
        if listDivide([2,4,6,8,10]) != 5:
            raise ListDivideException
        if listDivide([30, 54, 63,98, 100], divide=10) != 2:
            raise ListDivideException
        if listDivide([]) != 0:
            raise ListDivideException
        if listDivide([1,2,3,4,5], 1) != 5:
            raise ListDivideException
    except ListDivideException:
        print("Not divisible")

if __name__ == "__main__":
    testListDivide()