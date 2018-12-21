  # запрашиваем у пользователя список чисел через пробел и отдельной строкой ещё число
lst = [int(i) for i in input().split()]
x = int(input())

# заведем пустой список для ответов и счетчик
ans = []
cnt = -1
# проверяем присутствие числа х в списке list
if x in lst:
    for i in lst:
        cnt += 1
        if i == x:
            ans.append(cnt)
else:
    print("Отсутствует")

# выводим результат
for j in ans:
    print(j, end=" ")
