import os
import uproot as up
import pandas as pd

dataset = up.open("C:\\Users\\Taís Izidoro\\Documents\\UERJ\\IC\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45\\bbH_Za_LLChiChi-RunIISummer20UL16NanoAOD_0.root")
tree = dataset.get("Events")
a = tree.keys()

parsed_events = []
for file in os.listdir(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45"):
    try:
        dataset = up.open(os.path.join(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45", file))
        tree = dataset.get("Events;1")
        objects = a
        events = tree.arrays(objects)

        for event in events:
            event = {k: getattr(event, k) for k in objects}
            parsed_events.append(event)

    except:
        break



lista = parsed_events
df = pd.DataFrame(lista)
df.to_csv('variables.csv', index=False, header=True)