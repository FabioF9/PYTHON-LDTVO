import os.path
from os import path
import shutil

file= open("C:\\test2\\eclasseur2.csv")
lines=file.read().splitlines()
file.close()
file=open("C:\\test2\\log.txt","w")
i=0
path1="1-General_assembly\\"
path2="2-Part_drawing\\"
path3="3-Documentation\\"
fileDst = "C:\\testdir\\"
fileDst1= "C:\\testdir\\1\\"
fileDst2= "C:\\testdir\\2\\"
fileDst3= "C:\\testdir\\3\\"
for line in lines:
    i=i+1
    liste=line.split(";")
    path="I:\\AccessROVJET\\"
    id=liste[0]
    code=liste[1]
    ref=liste[2]
    doc_link=path+liste[3] 
    doc_name=liste[4]
    is_drawing=liste[5]
    fileDstv =  fileDst + ref + '_' + code +".pdf"
    fileDstf =  fileDst + code + ".pdf"
    fileDstv1 =  fileDst1 + ref + '_' + code +".pdf"
    fileDstv2 =  fileDst2 + ref + '_' + code +".pdf"
    fileDstv3 =  fileDst3 + ref + '_' + code +".pdf"
    fileDstf1 =  fileDst1 + code + ".pdf"
    fileDstf2 =  fileDst2 + code + ".pdf"
    fileDstf3 =  fileDst3 + code + ".pdf"
    print (i, doc_link) 
 
    if path1 in doc_link:
        substr1=doc_link[doc_link.index(path1):]
        if is_drawing=="VRAI":
            try:
                shutil.copy(path+substr1,fileDstv1)
            except:
                file.write(line+";CPYERR"+"\n")
        if is_drawing=="FAUX":
            try:
                shutil.copy(substr1,fileDstf1)
            except:
                file.write(line+";CPYERR"+"\n")
    elif path2 in doc_link:
        substr2=path+doc_link[doc_link.index(path2):]
        if is_drawing=="VRAI":
            try:
                shutil.copy(substr2,fileDstv2)
            except:
                file.write(line+";CPYERR"+"\n")
        if is_drawing=="FAUX":
            try:
                shutil.copy(substr2,fileDstf2)
            except:
                file.write(line+";CPYERR"+"\n")
    elif path3 in doc_link:
        substr3=path+doc_link[doc_link.index(path3):]
        print(substr3)
        if is_drawing=="VRAI":
            try:
                shutil.copy(substr3,fileDstv3)
            except:
                file.write(line+";CPYERR"+"\n")
        if is_drawing=="FAUX":
            try:
                shutil.copy(substr3,fileDstf3)
            except:
                file.write(line+";CPYERR"+"\n")
    else:
        file.write(line+";NOFOUND"+"\n")
file.close()