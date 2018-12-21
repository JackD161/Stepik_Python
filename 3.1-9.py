#list = [int(i) for i in input().split()]
list = [1, 2, 3, 3, 5, 4, 5, 7, 6]
def modify_list(lst):
    l = []
    for i in lst:
        if i%2 == 0:
            l.append(i//2)
    lst.clear()
    for j in l:
        lst.append(j)
print (modify_list(list))
print (list)