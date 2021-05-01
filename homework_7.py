import time
import datetime
import os

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
    1 : ['   ███   ', '         ', '   ███   ', '         ', '         '],
    2 : ['   ███   ', '         ', '   ███   ', '         ', '         '],
    3 : ['         ', '   ███   ', '         ', '   ███   ', '         '],
    4 : ['         ', '   ███   ', '         ', '   ███   ', '         '],
    5 : ['         ', '         ', '   ███   ', '         ', '   ███   '],
    6 : ['         ', '         ', '   ███   ', '         ', '   ███   '],
    7 : ['         ', '   ███   ', '         ', '   ███   ', '         '],
    8 : ['         ', '   ███   ', '         ', '   ███   ', '         '],
}

def my_generator():
    for n in range(1,10):
        yield(n)

ert = my_generator()
while True:
    time_now = str(datetime.datetime.now(tz=None).strftime("%H%M%S"))
    h1 = num.get(int(time_now[0]))
    h2 = num.get(int(time_now[1]))
    m1 = num.get(int(time_now[2]))
    m2 = num.get(int(time_now[3]))
    s1 = num.get(int(time_now[4]))
    s2 = num.get(int(time_now[5]))

    g = next(ert)
    if g > 8:
        ert = my_generator()
        g = next(ert)

    del_list = delimiter.get(int(g))

    i = 0    
    while i <= 4:
        lin_s = h1[i] + h2[i] + del_list[i] + m1[i] + m2[i] + del_list[i] + s1[i] + s2[i]
        print(lin_s)
        i += 1
    time.sleep(0.4)
    os.system('cls')