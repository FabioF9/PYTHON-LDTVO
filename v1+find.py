import os.path
from os import path
import shutil
from find import recherche 

file= open("C:\\test\\test.csv")
lines=file.read().splitlines()
file.close()
file=open("C:\\test\\log.txt","w")
i=0
root_dir ="C:\\test\\"
pathfileok = ''
for line in lines:
    i=i+1
    liste=line.split(";")
    path="C:\\test\\"
    id=liste[0]
    type=liste[1]
    doc_name=liste[2]
    doc_path=path+liste[3] 
    fileDst = "C:\\testdir\\"
    fileDst =  fileDst + id + '_' + type + '_' + doc_name
    print (i, doc_path)

    if recherche(root_dir,doc_name,pathfileok)[0]:
        # print(recherche(root_dir,doc_name,pathfileok)[1])
        try:
            shutil.copy(doc_path,fileDst)
        except:
           file.write(line+";CPYERR"+"\n") 
    else:
        file.write(line+";NOFOUND"+"\n")
file.close()