# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""


import re
from pprint import pprint

def parse_sh_cdp_neighbors(data: str) -> dict:
    ""
    regex = re.compile(r"(?P<device_id>\S+)\s+"
                       r"(?P<local_intf>\S+ \S+)\s+"
                       r"(?P<holdtime>\d+)\s+"
                       r"(?P<capability>(\S ){2,3})\s+"
                       r"(?P<platform>\S+)\s+"
                       r"(?P<port_id>\S+ \S+)")

    sw_name = data.split(">")[0].strip()

    match = regex.finditer(data)
    if match:
        int_dict = dict()
        for m in match:
            int_dict[m.group("local_intf")] = {m.group("device_id"): m.group("port_id")}
        result = {sw_name: int_dict}

    return result

data = """
SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R4           Eth 0/4         150           R S I           2811       Eth 0/0
"""

if __name__ == "__main__":
    pprint(parse_sh_cdp_neighbors(data))