import numpy as np
import matplotlib.pyplot as mt

def validation(number):
    punct = [",", "."]
    minus = "-"
    idx= []
    ifminus = False
    if number[0] == minus:
        number = number[1:]
        ifnimus = True
    for i in number:
        if not i.isdecimal() and not i in punct:
            return False, ifminus
        elif i in punct:
            idx.append(number.index(i))

    if len(idx) > 1:
        return False, ifminus
    return True, ifminus


a = input("coefficient a ")
while not validation(a)[0]:
    a = input("coefficient a ")
b = input("coefficient b ")
while not validation(b)[0]:
    a = input("coefficient b ")
c = input("coefficient c ")
while not validation(c)[0]:
    c = input("coefficient c ")

if validation(a)[1]:
    a = float(a) * -1
else:
    a = float(a)
if validation(b)[1]:
    b = float(b) * -1
else:
    b = float(b)
if validation(c)[1]:
    c = float(c) * -1
else:
    c = float(c)

x = np.linspace(-10, 10, 1000)
y1 = a*(x**2) + b*x + c
mt.plot(x, y1)

y2 = np.log2(x)
mt.plot(x, y2)

for i in range(len(x)):
    if round(y1[i], 1) == round(y2[i], 1):
        mt.plot(x[i], y2[i], "ro")

mt.show()
