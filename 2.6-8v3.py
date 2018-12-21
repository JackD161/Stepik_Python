# заведем пустой список
serial = []

# запрашиваем пользователя число n
n = int(input())

# создадим цикл вложенный в цикл заполняющий наш список
for i in range(1, n + 1):
    for j in range(i):
        serial.append(i)

# выводим ответ с помощью цикла от начала до индекса n
for a in range(n):
    print(serial[a], end=" ")
