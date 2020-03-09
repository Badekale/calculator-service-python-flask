#!/usr/bin/env python
import math

class Calculator:
    def __init__(self):
        pass

    def add(self, arg1, arg2):
        return float(arg1) + float(arg2)

    def subtract(self, arg1, arg2):
        return float(arg1) - float(arg2)

    def multiply(self, arg1, arg2):
        return float(arg1) * float(arg2)

    def divide(self, arg1, arg2):
        return float(arg1) / (arg2)

    def sqrt(self, arg1):
        return math.sqrt(float(arg1))

    def cbrt(self, arg1):
        return round(float(arg1)**(1.0/3))

    def exp(self, arg1, arg2):
        return float(arg1) ** float(arg2)

    def factorial(self, arg1):
       if arg1 == 1:
          return arg1
       else:
          return float(arg1)*self.factorial(float(arg1)-1)
