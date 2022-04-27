from random import random
from math import floor

from numpy import outer

gene1 = input("Enter the 1st gene: ")
gene2 = input("Enter the 2nd gene: ")

if len(gene1) != len(gene2):
    print("Length should be the same")
    exit(1)

length = len(gene1) #or gene2 as both are same
k = floor(random() * length)
k = k - 1

print(f"The crossover point selected is {k}")
output1 = ""
output2 = ""

for i in range(k+1):
    # print(i)
    output1 = output1 + gene1[i]
    output2 = output2 + gene2[i]

for i in range(k+1, length):
    # print(i)
    output1 = output1 + gene2[i]
    output2 = output2 + gene1[i]

print(f"Output 1 is {output1}")
print(f"Output 2 is {output2}")
