# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from curses.ascii import isalnum


def check_ip(ip: str):
   if '.' not in ip: return False
   ip_oct = ip.split('.')
   if len(ip_oct) != 4: return False
   for i in ip_oct:
      if not i.isdigit(): return False
   for i in ip_oct:
      if not (0 <= int(i) <= 255): return False
   return True
   

ip = input("Enter IP-adress: ")

if check_ip(ip):
   ip_oct = ip.split('.')
   if (1 <= int(ip_oct[0]) <= 223): print("unicast")
   elif (224 <= int(ip_oct[0]) <= 239): print("multicast")
   elif ip == "255.255.255.255": print("local broadcast")
   elif ip == "0.0.0.0": print("unassigned")
   else:print("unused")
else:
   print("Неправильный IP-адрес")