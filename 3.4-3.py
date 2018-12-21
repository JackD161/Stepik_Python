with open('dataset2.txt','r') as data:
    lst = data.read().split()

lst_main = []
for i in lst:
    i = i.lower()
    lst_main.append(i)
print (lst_main)
book = {}
for j in lst_main:
    key = lst_main.count(j)
    book[key] = j
print (book)
cnt = (book.keys())
max_cnt = max(cnt)
print (book[max_cnt], max_cnt)