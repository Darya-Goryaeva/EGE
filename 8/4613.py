import itertools
# Альтернативный способ (без библиотеки itertools)
"""
str = '012345678'
for i1 in str:
    for i2 in str:
        for i3 in str:
            for i4 in str:
                for i5 in str:
                    line = i1 + i2 + i3 + i4 + i5
                    print(line)
"""

strings = itertools.product('012345678', repeat=5)
count = 0
for line in strings:
    line = ''.join(line)
    if line[0] not in '01357' and line[-1] not in '18' and line.count('3') <= 1:
        count += 1
print(count)


