#Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def fill (n):
    lst=[]
    for i in range(n+1):
        lst.append (i)
   
    return lst

def out (lst:list):
    ls=[lst[i] for i in range (len(lst)) if lst[i]%20==0 or lst[i]%21==0]
    return ls

n= int (input ('input a number'))
lst = fill(n)
print (lst)
print (out(lst))
