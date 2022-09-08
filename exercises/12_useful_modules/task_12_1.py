# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_list: list):

    reachable = []
    unreachable = []

    for ip in ip_list:
        reply = subprocess.run(['ping', '-c', '1', '-n', ip])
        if reply.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


ip_list = ["192.168.1.1", "192.168.1.2", "8.8.8.8", "1.1.1.1", "15.185.140.22"]

print(ping_ip_addresses(ip_list))