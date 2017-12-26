import math
class Calc:
    def add(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum
    # sum(args)でもおk

    def sub(self,a,b):
        return a - b
    
    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def calc(self, str):
        return eval(str)

    def sqrt(self, num):
        return math.sqrt(2)

