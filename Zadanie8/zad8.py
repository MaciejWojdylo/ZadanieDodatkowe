import mplcursors
import numpy as np
from matplotlib import pyplot as plt

Temp = []
for i in range(0,41):
    Temp.append(i)
Hot = []
for tmp in Temp:
    if tmp < 15:
        Hot.append(0)
    else:
        if tmp >= 15 and tmp <= 25:
            Hot.append(round((tmp-15)/10,3))
        else:
            Hot.append(1)
Warm = []
for tmp in Temp:
    if tmp >= 15 and tmp <= 25:
        Warm.append(-1*round((tmp-25)/10,3))
    else:
        if tmp >= 7 and tmp < 15:
            Warm.append(round((tmp-7)/8,3))
        else:
            Warm.append(0)
Cold = []
for i in Temp:
    if i < 7:
        Cold.append(1)
    else:
        if i <= 15 and i >= 7:
            Cold.append(1-round((i-7)/8,3))
        else:
            Cold.append(0)
Zaludnienie=[]
for i in range(0,850,50):
    Zaludnienie.append(i)
Crowd=[]
for x in Zaludnienie:
    if x < 100:
        Crowd.append(0)
    else:
        if x>=100 and x<=500:
            Crowd.append(round((x-100)/400,3))
        else:
            Crowd.append(1)
Quiet=[]
for x in Zaludnienie:
    if x < 100:
        Quiet.append(1)
    else:
        if x>=100 and x<=500:
            Quiet.append(round(-(x-500)/400,3))
        else:
            Quiet.append(0)
print("a)")
print("Zmienna lingwistyczna to Temperatura i Zaludnienie")
print("Wartosc zmiennej lingwistycznej to hot cold warm lub quiet crowd")
print("b)")
plt.plot(Temp, Hot, label='Hot', color='red', marker='o')
plt.title("Temperatura Hot")
plt.xlabel("Temperatura")
plt.ylabel("Hot")
plt.legend()
plt.plot(Temp, Cold, label='Cold', color='blue', marker='o')
plt.title("Temperatura Cold")
plt.xlabel("Temperatura")
plt.ylabel("Wartość Gorąca")
plt.legend()
plt.plot(Temp, Warm, label='Warm', color='orange', marker='o')
plt.title("Temperatura Warm")
plt.xlabel("Temperatura")
plt.ylabel("Hot")
plt.legend()
plt.show()
plt.cla()

plt.plot(Zaludnienie,Crowd,label='Crowd',color='blue',marker = 'o')
plt.title("Crowd")
plt.xlabel("Zaludnienie")
plt.ylabel("Wartość głośności")
plt.legend()

plt.plot(Zaludnienie,Quiet,label='Quiet',color='red',marker = 'o')
plt.title("Quiet")
plt.xlabel("Zaludnienie")
plt.ylabel("Wartość głośności")
plt.legend()
line, = plt.plot(Zaludnienie, Crowd, marker='o')
plt.show()

Mamdani_temp = 21
Mamdani_hot = round((21-15)/10,2)
Mamdani_warm = -1* round((21-25)/10,2)
Mamdani_cold = 0
Mamdani_temp_rule1 = max(Mamdani_hot,Mamdani_warm)
Mamdani_temp_rule2 = Mamdani_cold
print(Mamdani_temp_rule1)
closed = 1
max = 0
aproxPeople = 0
for i, j in zip(Zaludnienie, Crowd):
    i_rounded = round(i, 1)
    j_rounded = round(j, 1)
    if i_rounded == Mamdani_temp_rule1 or j_rounded == Mamdani_temp_rule1:
        print(f"Wartość dla Zaludnienia = {i_rounded} to Crowd = {j_rounded}")