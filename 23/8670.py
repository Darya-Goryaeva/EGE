"""
Исполнитель Увеличитель345 преобразует число, записанное на экране.
У исполнителя три команды, которым присвоены номера:
1. Прибавь 3
2. Прибавь 4
3. Прибавь 5

Первая из них увеличивает число на экране на 3,
вторая увеличивает это число на 4, а третья – на 5.
Программа для исполнителя Увеличитель345 – это последовательность команд.
Сколько есть программ, которые число 22 преобразуют в число 42?
"""

def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 3, y) + f(x + 4, y) + f(x + 5, y)


print(f(22, 42))
