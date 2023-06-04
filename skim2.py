import csv
import copy
import pandas as pd

f = open('skim1.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

skim2 = copy.deepcopy(lista)

for i in range(0, len(lista)):
    for key, value in lista[i].items():

        if key == "Tau_pt":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k < 20:
                    continue
                skim2[i][key].append(k)

        if key == "Tau_eta":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k > 2.4:
                    continue
                skim2[i][key].append(k)

        if key == "Tau_dz":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k > 0.2:
                    continue
                skim2[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSe":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k < 8:  # if k << 8:
                    continue
                skim2[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSmu":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k < 1:  # if k << 1:
                    continue
                skim2[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSjet":
            new = eval(value)
            skim2[i][key] = []
            for k in new:
                if k < 8:  # if k << 8:
                    continue
                skim2[i][key].append(k)


df = pd.DataFrame(skim2)
df.to_csv('skim2.csv', index=False, header=True)