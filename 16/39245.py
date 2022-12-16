"""
Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:

F(0) = 0;
F(n) = F(n / 2), если n > 0 и при этом чётно;
F(n) = 1 + F(n − 1), если n нечётно.

Сколько существует таких чисел n, что 1 ≤ n ≤ 900 и F(n) = 9?
Ответ: 3
"""


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    if n % 2 != 0:
        return 1 + f(n - 1)


count = 0
for i in range(1, 901):
    if f(i) == 9:
        count += 1
print(count)