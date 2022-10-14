#1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

from random import randint

def fill (count):
    lst = []
    for i in range (count):
        lst.append (randint(1,100))
    return lst

def out (lst:list):
    ls=[lst[i] for i in range (1,len(lst)) if lst[i]>lst[i-1] ]
    return ls

count = int (input ('input count'))
lst = fill(count)
print (lst)
print (out(lst))
