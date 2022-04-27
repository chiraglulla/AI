from random import random


gene = input("Enter the gene: ")
probability = float(input("Enter the mutation probability: "))
probability_gene = ""
length = len(gene)

for i in range(length):
    rand = random()
    if rand > probability:
        probability_gene = probability_gene + "1"
    else:
        probability_gene = probability_gene + "0"

mutated_gene = ""
for i in range(length):
    if probability_gene[i] == "1":
        if gene[i] == "1":
            mutated_gene = mutated_gene + "0"
        else:
            mutated_gene = mutated_gene + "1"
    else:
        mutated_gene = mutated_gene + gene[i]

print(f"The gene is {gene}")
print(f"The probability vector generated is {probability_gene}")
print(f"The mutated gene is {mutated_gene}")