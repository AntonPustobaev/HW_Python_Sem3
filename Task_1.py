#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


n = 5
mylist = ['Good', '25/17', 'lich', '5', '29', 'uhhh']

def find_number(n, list):
    return str(n) in list

print(find_number(n, mylist))