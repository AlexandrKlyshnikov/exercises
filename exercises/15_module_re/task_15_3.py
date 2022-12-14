# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re

def convert_ios_nat_to_asa(input_file: str, output_file: str):
    
    regex = re.compile("ip nat inside source static tcp (?P<ip>\S+) (?P<int_port>\S+) interface (?P<intf>\S+) (?P<ext_port>\S+)")

    pattern = """
object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service tcp {} {}"""

    with open(input_file) as input, open(output_file, "w") as output:
        result = ""
        for line in input:
            match = regex.search(line)
            if match:
                # result += (pattern.format(match.group("ip", "ip", "int_port", "ext_port")))
                result += (pattern.format(*match.group("ip", "ip", "int_port", "ext_port")))
        output.write(result)

convert_ios_nat_to_asa("/home/user/Code/exercises/exercises/15_module_re/cisco_nat_config.txt", "/home/user/Code/exercises/exercises/15_module_re/OUTPUT.txt")