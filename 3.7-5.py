book = {}  # заведем словарь ддя занесения данных о номере класса, количестве учеников и их росте в журнал
with open('dataset_3380_5.txt', 'r') as data:  # открываем файл формата TSV на чстение
    r = data.read().split()  # прочитанные строки разделяем по знаку табуляции
    cnt = 0  # заведем начальный индекс для отсчета цикла
    while cnt < len(r):  # заведем цикл счетчиком которого будет ключ для словаря
        if r[cnt] not in book:  # проверяем отсутствие ключа в словаре
            book[r[cnt]] = [1, int(
                r[cnt + 2])]  # если ключ отсутствует то заведем его со списком из счетчика учеников и их роста
        else:  # если ключ присутствует в словаре
            book[r[cnt]][0] += 1  # увеличиваем в списке счетчик учеников на 1
            book[r[cnt]][1] += int(r[cnt + 2])  # увеличиваем с списке рост учеников
        cnt += 3  # делаем шаг циклу 3 для того чтоб из списка следующим оператором сосчитался опять номер класса учеников
klass = 1  # задаем номер начала цикла который выведет из словаря все данные по всем классам
while klass <= 11:  # выполняем цикл пока его счетчик меньше или равен 11
    if str(klass) not in book:  # проверяем наличие данных о номере класса в журнале
        print(klass, '-')  # если их нет то выводим номер класса и прочерк
    else:  # если данные есть товыводим номер класса и средний рост
        print(klass,
              book[str(klass)][1] / book[str(klass)][0])  # полученный от деления общего роста на количество учеников
    klass += 1  # увеличиваем счетчик цикла на 1
