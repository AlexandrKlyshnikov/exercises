# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

FILENAME = argv[1]
OUTPUT = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(FILENAME, 'r') as file, open(OUTPUT, 'a') as out_file:

    for line in file:
        if line[0] != '!':
            for i in ignore:
                if i in line:
                    break
            else:
                out_file.write(line)