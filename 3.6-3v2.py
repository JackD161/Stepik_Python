with open('dataset_3378_3.txt','r') as file_last: # читаем имеющийся первый файл
    url1 = file_last.read().split() # разделяем прочтенный файл от знака переноса строки
def url_get_file(url):
    import requests
    r = requests.get(url)
    print ('Прочитанные данные', r.text)
    req = r.text.split()
    if req[0] == 'We':
        with open('answer_last.txt','w') as ans:
            ans.write(r.text)
        return
    else:
        url_get_file(main_url + req[0])
main_url = 'https://stepic.org/media/attachments/course67/3.6.3/' # заводим константу начала url адреса
url_get_file(url1[0])