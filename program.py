import os.path
from os import path
file= open("I:\Bal\FabioFurnari\ExtractionPhoto.csv")
lines=file.readlines()
file.close()


for line in lines:
    liste=line.split(";")
    id=liste[0]
    type=liste[1]
    doc_name=liste[2]
    # doc_link=(liste[3])
    doc_link='I:\\Gestion-Mat\\'+ (liste[3])
    ndoc_link=doc_link.replace(os.sep,'/')
    a=(os.path.exists(ndoc_link))
    print(a)
    print(ndoc_link)
    


