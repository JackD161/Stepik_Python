import requests
main_url = 'https://stepic.org/media/attachments/course67/3.6.3/843785.txt' # заводим константу начала url адреса
r = requests.get(main_url)
req = r.text.split()
print (req)
print (req[0])