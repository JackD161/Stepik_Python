with open('dataset_3378_2.txt','r') as file:
    path_from_file = file.read()
import requests
print (path_from_file)
r = requests.get(path_from_file)
rt = r.text.splitlines()
print (rt)
print (len(rt))
with open('requests_answer.txt','w') as ans:
    ans.write(r.text)