#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. #Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
from typing import List, Union

my_list = [15, None, -75,'True', True, 9.5]
def my_type (el):
    for el in range ( len ( my_list )):
        print ( type ( my_list [ el ]))
    return
my_type (my_list)
