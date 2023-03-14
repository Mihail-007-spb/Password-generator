"""Password generator"""

"""Генератор паролей"""


import random


def password():
    st = ''
    n = random.randint(8, 15)
    x = n
    while not x == 0:
        i = random.randint(48, 57)
        g = random.randint(65, 90)
        j = random.randint(97, 122)
        ls = [chr(i), (chr(g)).lower(), (chr(j)).upper()]
        a = (random.randint(0, 2))
        st += str(ls[a])
        x += -1

    print(st)


password()