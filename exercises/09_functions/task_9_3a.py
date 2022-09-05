# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

filename = "/home/user/Code/exercises/exercises/09_functions/config_sw2.txt"

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        acs = {}
        trn = {}
        for line in file:
            if "interface" in line:
                key = line.split()[-1]
            if "switchport access vlan" in line:
                acs[key] = int(line.split()[-1])
            if "switchport trunk allowed vlan" in line:
                trn[key] = [*map(int, line.split()[-1].split(','))]
            if "duplex auto" in line:
                try:
                    trn[key]
                except(KeyError):
                    try:
                        acs[key]
                    except(KeyError):
                        acs[key] = 1
    return acs, trn

print(get_int_vlan_map(filename))