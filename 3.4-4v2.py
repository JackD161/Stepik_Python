with open('dataset_3363_4.txt', 'r') as data:  # читпем файл
    lst = data.read().split()  # разбивает прочтенный файл на строки по символу \n

print(lst)  # выводим прочтенные данные для визуальной проверки

book = {}  # заводим словарь book, в котором ключ это фамилия студента, а значение - средний балл по 3 предметам
book2 = {}  # заводим словарь book2, в котором ключ это фамилия слудента, а значение это список оценок по 3 предметам - математике, физике и русскому языку

for i in lst:  # проходим циклом по прочтенным строкам
    ls = i.split(';')  # разделяем прочтенную строку по символу ;
    rez = (int(ls[1]) + int(ls[2]) + int(ls[3])) / 3  # считаем средний балл студента
    book[ls[0]] = rez  # заносим в словарь средний балл с ключом фамилии студента
    balls = [ls[1], ls[2], ls[3]]  # заводим пустой список оценок
    book2[ls[0]] = balls  # заносим в словарь список оценок по ключу фамилии студента

print(book)  # выводим данные словаря book для визуальной проверки
print(book2)  # выводим данные словаря book2 для визуальной проверки
print('*' * 150)  # отчерчиваем границу

with open('answer.txt','w') as data2: # открываем файл ответа на запись
    for m in book:  # проходим циклом по словарю book для вывода его значений
        print(book[m])  # выводим значения
        data2.write(str(book[m])) # приводим ответ к строковому формату и пишем эту строку в файл
        data2.write('\n') # добавляем перенос строки

sum_mat = 0  # задаем начальную сумму баллов по математике
sum_fiz = 0  # задаем начальную сумму баллов по физике
sum_rus = 0  # задаем начальную сумму баллов по русскому языку

for h in book2:  # проходим циклом по словарю book2
    sum_mat += int(book2[h][0])  # увеличиваем сумму по математике на значение первого элемента в списке по итерируемому ключу словаря book2
    sum_fiz += int(book2[h][1])  # увеличиваем сумму по физике на значение второго элемента в списке по итерируемому ключу словаря book2
    sum_rus += int(book2[h][2])  # увеличиваем сумму по русскому языку на значение третьего элемента в списке по итерируемому ключу словаря book2
print(sum_mat / len(book2), sum_fiz / len(book2), sum_rus / len(book2))  # выводим через пробел суммы по математике, физике и русскому языку деленные на общий делитель
with open('answer.txt','a') as data3: # открываем файл на запись в конец файла
    data3.write(str(sum_mat/len(book2))) # делим сумму балов по математике на количество студентов, приводим к строковому формату и пишем в файл
    data3.write(' ') # дописываем пробел
    data3.write(str(sum_fiz/len(book2))) # делим сумму балов по физике на количество студентов, приводим к строковому формату и пишем в файл
    data3.write(' ') # дописываем пробел
    data3.write(str(sum_rus/len(book2))) # делим сумму балов по русскому языку на количество студентов, приводим к строковому формату и пишем в файл