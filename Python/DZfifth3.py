""" Создайте функцию генератор чисел Фибоначчи
"""
n = int(input('Enter number: '))
def fib_gen(n):
    fib = [0] * (n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    yield fib
print(*fib_gen(n))


