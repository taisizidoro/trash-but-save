import csv
import pandas as pd

f = open('../branches-analysis.csv', 'r')
reader = csv.DictReader(f)
lista2 = list(reader)

skim1 = []
for i in range(0,len(lista2)):
    for key, value in lista2[i].items():
        if key == "nTau":
            if value == "2":
                skim1.append(lista2[i])


df = pd.DataFrame(skim1)
df.to_csv('skim1.csv', index=False, header=True)
print(skim1)
