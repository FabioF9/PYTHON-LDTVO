from pathlib import Path
import os.path
from os import path
file= open("I:\Bal\FabioFurnari\est.csv")
lines=file.readlines()
file.close()


for line in lines:
    liste=line.split(";")
    id=liste[0]
    type=liste[1]
    doc_name=liste[2]
    doc_link=(liste[3])
    path=Path('I:\\','Gestion-Mat',doc_link)
    a=os.path.exists(path)
    print(a)
    print(path)