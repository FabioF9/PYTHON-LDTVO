import os.path
from os import path
import shutil

file= open("I:\\Bal\\FabioFurnari\\extractionSRVDEV.csv")
lines=file.read().splitlines()
file.close()
file=open("I:\\Bal\\FabioFurnari\\log.txt","w")
i=0
for line in lines:
    i=i+1
    liste=line.split(";")
    path="I:\\Gestion-Mat\\"
    id=liste[0]
    type=liste[1]
    doc_name=liste[3]
    doc_link=path+liste[2] 
    fileDst = "I:\\Bal\\FabioFurnari\\www\\doc\\equipment_doc\\photo\\"
    fileDst =  fileDst + id + '_' + type + '_' + doc_name
    print (i, doc_link) 
    
    if os.path.exists(doc_link):
        try:
            shutil.copy(doc_link,fileDst)
        except:
           file.write(line+";CPYERR"+"\n") 
    else:
        file.write(line+";NOFOUND"+"\n")
file.close()
    