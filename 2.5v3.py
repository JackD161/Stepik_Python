# заведем пустой список
d=[]
s=[]
# заполним список с помощью list comprehension
d=[int(i) for i in input().split()]
#print ("Введено","\t",d)

# отсортируем список методом sort
d.sort()
#print ("Отсортировано","\t",d)

# зададим цикл который пройдет по всмему введенному списку
for i in d:
# посчитаем количество одинаковых значений итерируемого списка
    cnt=d.count(i)
# если одинаковых значений больше 1 то проверяю есть ли это значение в списке s, если нет то заносим его в список s
    if cnt>1:
        if i not in s:
            s.append(i)


# задаем цикл для вывода данных
for f in s:
    print (f, end=" ")