import requests
r = requests.get('http://pharmaciya.ru')
print (r.text)