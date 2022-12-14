# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = []
with open("/home/user/Code/exercises/exercises/07_files/CAM_table.txt", 'r') as file:
    for line in file:
        if "Gi" in line:
            split = line.split()
            result.append([int(split[0]), split[1], split[3]])

vlan = int(input("Enter VLAN number:"))

for line in sorted(result):
    if line[0] == vlan:
        print("{:<9}{:<20}{:<10}".format(line[0], line[1], line[2]))