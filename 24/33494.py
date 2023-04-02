f = open('33494.txt')
# read() - чтение всего файла целиком
line = f.read()
letters = {}
m = 0
sym = ''
for i in range(len(line) - 1):
    if line[i] == 'E':
        # Если символ есть в словаре, то увеличиваем значение на 1
        if line[i + 1] in letters:
            letters[line[i + 1]] += 1
        # Если нет, то добавляем в словарь новый символ со значением 1
        else:
            letters[line[i + 1]] = 1
        if letters[line[i + 1]] > m:
            m = letters[line[i + 1]]
            sym = line[i + 1]
print(sym)
