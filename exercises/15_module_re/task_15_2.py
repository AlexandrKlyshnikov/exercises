# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

def parse_sh_ip_int_br(filename):

    regex = re.compile(
        r"(?P<intf>\S+)\s+"
        r"(?P<ip>\S+)\s+"
        r"(?P<ok>\S+)\s+"
        r"(?P<method>\S+)\s+"
        r"(?P<status>up|down|administratively down)\s+"
        r"(?P<protocol>up|down|administratively down)\s+"
    )

    with open(filename) as file:
        result = []
        for line in file:
            match = regex.search(line)
            if match:
                result.append(match.group("intf", "ip", "status", "protocol"))
    
    return result

print(parse_sh_ip_int_br("/home/user/Code/exercises/exercises/15_module_re/sh_ip_int_br.txt"))