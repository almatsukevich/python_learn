import time
import datetime
import os
import random

import colorama
from colorama import Fore, Back, Style
colorama.init()

def color_print(lin_s, color):
    if color == 1:
        print(Fore.RED + lin_s)
    if color == 2:
        print(Fore.BLUE + lin_s)
    if color == 3:
        print(Fore.GREEN + lin_s)
    if color == 4:
        print(Fore.YELLOW + lin_s)
    if color == 5:
       print(Fore.WHITE + lin_s)

def my_generator():
    for n in range(1,10):
        yield(n)

def func_delimiter(del_pos):
    g = next(del_pos)
    if g > 8:
        del_pos = my_generator()
        g = next(del_pos)
    return delimiter.get(g), del_pos

num = {
    0 : [' ███████ ', ' ██   ██ ', ' ██   ██ ', ' ██   ██ ', ' ███████ '],
    1 : ['  ████   ', '    ██   ', '    ██   ', '    ██   ', ' ███████ '],
    2 : [' ███████ ', '      ██ ', ' ███████ ', ' ██      ', ' ███████ '],
    3 : [' ███████ ', '      ██ ', ' ███████ ', '      ██ ', ' ███████ '],
    4 : [' ██   ██ ', ' ██   ██ ', ' ███████ ', '      ██ ', '      ██ '],
    5 : [' ███████ ', ' ██      ', ' ███████ ', '      ██ ', ' ███████ '],
    6 : [' ███████ ', ' ██      ', ' ███████ ', ' ██   ██ ', ' ███████ '],
    7 : [' ███████ ', '      ██ ', '      ██ ', '      ██ ', '      ██ '],
    8 : [' ███████ ', ' ██   ██ ', ' ███████ ', ' ██   ██ ', ' ███████ '],
    9 : [' ███████ ', ' ██   ██ ', ' ███████ ', '      ██ ', ' ███████ '],
}

delimiter = {
    1 : ['   ███   ', '         ', '         ', '         ', '         '],
    2 : ['         ', '   ███   ', '         ', '         ', '         '],
    3 : ['         ', '         ', '   ███   ', '         ', '         '],
    4 : ['         ', '         ', '         ', '   ███   ', '         '],
    5 : ['         ', '         ', '         ', '         ', '   ███   '],
    6 : ['         ', '         ', '         ', '   ███   ', '         '],
    7 : ['         ', '         ', '   ███   ', '         ', '         '],
    8 : ['         ', '   ███   ', '         ', '         ', '         '],
}

del_position = my_generator()
while True:
    time_now = str(datetime.datetime.now(tz=None).strftime("%H%M%S"))
    h1 = num.get(int(time_now[0]))
    h2 = num.get(int(time_now[1]))
    m1 = num.get(int(time_now[2]))
    m2 = num.get(int(time_now[3]))
    s1 = num.get(int(time_now[4]))
    s2 = num.get(int(time_now[5]))

    del_list, del_position = func_delimiter(del_position)
    color = random.randint(1, 5)

    i = 0    
    while i <= 4:
        lin_s = h1[i] + h2[i] + del_list[i] + m1[i] + m2[i] + del_list[i] + \
            s1[i] + s2[i]
       # print(Fore.RED + lin_s)
        color_print(lin_s, color)
        i += 1
    time.sleep(0.3)
    os.system('cls')