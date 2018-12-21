list = [1, 2, 3, 3, 5, 4, 5, 7, 6]

def modify_list(l):
    ls = []
    for i in l:
        if i%2 == 0:
            ls.append(i//2)
    l.clear()
    for j in ls:
        l.append(j)

print (modify_list(list))
print (list)