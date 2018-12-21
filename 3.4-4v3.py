sum_mat = 0 # заводим начальную сумму оценок по математике
sum_fiz = 0 # заводим начальную сумму оценок по физике
sum_rus = 0 # заводим начальную сумму оценок по русскому языку
cnt = 0 # заводим счетчик для цикла
with open('dataset_3363_4.txt','r') as out1: # конструкция чтения из файла
    lst = out1.read().split() # читаем файл построчно и исключаем символы переноса строки \n
for i in lst: # проходим циклом по прочтенным данным
    ls = i.split(';') # читаем построчно и разделяем по знаку ;
    # получаем список из 4-х значений
    # по 0 индексу находится фамилия студента
    # по 1 индексу находится оценка по метематике
    # по 2 индексу находится оценка по физике
    # по 3 индексу находится оценка по русскому языку
    sum_mat += int(ls[1]) # увеличиваем сумму оценок по математике на значение списка по индексу 1
    sum_fiz += int(ls[2]) # увеличиваем сумму оценок по физике на значение списка по индексу 2
    sum_rus += int(ls[3]) # увеличиваем сумму оценок по русскому языку на значение списка по индексу 3
    cnt += 1 # увеличиваем счетчик цикла на 1
    sr_ball = (int(ls[1]) + int(ls[2]) + int(ls[3])) / 3
    with open('answer.txt','a') as balls: # откраваем файл ответа на запись
        balls.write(str(sr_ball)) # записываем средний балл студента
        balls.write('\n') # записываем перенос строки
sr_ball_mat_all = (int(sum_mat)) / cnt # считаем среднию оченку по математике по всем студентам
sr_ball_fiz_all = (int(sum_fiz)) / cnt # считаем срению оченку по физике по всем студентам
sr_ball_rus_all = (int(sum_rus)) / cnt # считаем срению оченку по русскому языку по всем студентам
with open('answer.txt','a') as balls2: # открываем файл ответа на дозапись
    balls2.write(str(sr_ball_mat_all)) # записываем средний балл по математике по всем студентам
    balls2.write(' ') # дописываем пробел
    balls2.write(str(sr_ball_fiz_all)) # записываем средний балл по физике по всем студентам
    balls2.write(' ') # дописываем пробел
    balls2.write(str(sr_ball_rus_all)) # записываем средний балл по русскому языку по всем студентам