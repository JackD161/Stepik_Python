#Запрашиваем ввод
#a=int(input())
#b=int(input())
#c=int(input())
#d=int(input())

a=1
b=5
c=6
d=10

#Задаем условие выполнения
if a<=10 and b<=10 and c<=10 and d<=10 and a<=b and c<=d:

# Задаем циклы
    #Цикл для пераого диапазона
    for i in range(a,b+1):
        print(i)
        for j in range(c,d+1):
            print (i*j,"\t",end="")
        print ("\n")