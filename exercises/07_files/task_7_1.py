# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
TEMPLATE = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}"""
"""
O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
"""
FILENAME = "ospf.txt"
with open(FILENAME) as file:
    for line in file:
        items = line[9:-1].replace('[', '').replace(']', '').replace(',', '').split(" ")
        print(TEMPLATE.format(items[0], items[1], items[3], items[4], items[5]))