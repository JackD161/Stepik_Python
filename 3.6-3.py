with open('dataset_3378_3.txt','r') as file_last: # читаем имеющийся первый файл
    url1 = file_last.read().split() # разделяем прочтенный файл от знака переноса строки
print (url1[0]) # выводим для проверки полученный адрес
import requests # импортируем библиотеку для работы с запросами к web
url_main = 'https://stepic.org/media/attachments/course67/3.6.3/' # заводим константу начала url адреса
r = requests.get(url1[0]) # делаем запрос в web по адресу полученному из первого файла
url2 = url_main + r.text # формируем url из константы начала url и имени файла полученного в результате запроса
r2 = requests.get(url2) # делаем запрос по полученному адресу url2
print (url2) # выводим для проверки адрес url2
url3 = url_main + r2.text # формируем следующий адрес для запроса из константы и имени файла полученного от предыдущего запроса
r3 = requests.get(url3)
print (url3) # выводим третий адрес для проверки
url4 = url_main + r3.text # формируем четвертый url
r4 = requests.get(url4) # делаем запрос по полученному url
print (url4) # выводим четвертый url для проверки
l = r4.text.split()
print (l)