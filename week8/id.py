class Calculator:

    def add(self,num1, num2):
        result = num1 + num2
        return result
k = Calculator()

a = k.add(1,2)

print(a)


class Calc:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result = self.result + num
        return self.result

    def sub(self, num):

        self.result = self.result - num
        return self.result

k = Calc()
min = Calc()

print(k.add(3))
print(k.add(5))


print(min.sub(5))
print(min.sub(3))