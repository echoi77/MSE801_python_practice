#week8_Factorial
# Mine
a = [1, 2, 3, 4, 5]
factorials = []

for i in a:
    result = 1
    print(f'current selected number is {i}')
    for x in range(1,i+1):
        result = result * x
    print(f'{i}s factorial is {result}')


# Prof.
number = [1, 2, 3, 4, 5]

factorials = [1 if n == 0 else (f := 1, [f := f * i for i in range(1, n + 1)], f)[-1] for n in number]
print(factorials)

## test


