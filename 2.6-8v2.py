# инициализируем список
list = []
ls = ""
# запрашиваем число n
n = int(input())
# создаем цикл для генерации последовательности
for i in range(1, n + 1):
    list.append(i * str(i))

print(list)