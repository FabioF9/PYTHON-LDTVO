import os.path
from os import path
import shutil

file= open("C:\\Users\\julia\\Downloads\\LDTVO\\DOC-20221118T074801Z-001\\DOC\\eclasseur.csv")
lines=file.read().splitlines()
file.close()
file=open("C:\\Users\\julia\\Downloads\\LDTVO\\DOC-20221118T074801Z-001\\DOC\\log.txt","w")
i=0
path1="4-Tests_and_certificates\\"
for line in lines:
    i=i+1
    liste=line.split(";")
    path="C:\\Users\\julia\\Downloads\\LDTVO\\DOC-20221118T074801Z-001\\DOC\\"
    id=liste[0]
    code=liste[1]
    doc_link=path+liste[2] 
    doc_name=liste[3]
    numrov=liste[4]
    fileDst = "C:\\Users\\julia\\Downloads\\LDTVO\\dir\\"
    fileDst =  fileDst + "CT" + '_' + code + '_'+ numrov +".pdf"
    print (i, doc_link) 
 
    if path1 in doc_link:
        substr1=doc_link[doc_link.index(path1):]
        try:
            shutil.copy(path+substr1,fileDst)
        except:
            file.write(line+";CPYERR"+"\n")
    else:
        file.write(line+";NOFOUND"+"\n")
file.close()