# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def check_ip(ip: str):
   if '.' not in ip: return False
   ip_oct = ip.split('.')
   if len(ip_oct) != 4: return False
   for i in ip_oct:
      if not i.isdigit(): return False
   for i in ip_oct:
      if not (0 <= int(i) <= 255): return False
   return True
   

def get_ip():
    ip = input("Enter IP-adress: ")
    if check_ip(ip):
        return ip
    else:
        print("Неправильный IP-адрес")
        return get_ip()


def ip_type(ip):
    ip_oct = ip.split('.')
    if (1 <= int(ip_oct[0]) <= 223): return "unicast"
    elif (224 <= int(ip_oct[0]) <= 239): return "multicast"
    elif ip == "255.255.255.255": return "local broadcast"
    elif ip == "0.0.0.0": return "unassigned"
    else: return "unused"


ip = get_ip()
print(ip_type(ip))
