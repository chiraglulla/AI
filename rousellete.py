# from msilib.schema import tables
from random import random


fw = list()
fws = input().split(",")
# print(fws)
for f in fws:
    fw.append(int(f))

total_fw = 0
for f in fw:
    total_fw = total_fw + f

percent_fw = list()
for f in fw:
    percent_fw.append(round(f/total_fw, 3))

temp = 0
for p in percent_fw:
    temp = temp + p

for i in range(100):
    rand = random()

    print("------------------------------------------------------")
    print(rand)
    summ = 0
    found = False
    while True:
        for j in range(len(percent_fw)):
            if summ + percent_fw[j] > rand:
                found = True
                print(f"{fw[j]} is the winner")
                break
            summ = summ + percent_fw[j]

        if found:
            break
        
