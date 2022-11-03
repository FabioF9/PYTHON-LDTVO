from msvcrt import LK_LOCK
import os
root_dir ="C:\\test\\"
doc_name="esT.csv"
def recherche(root_dir,doc_name,pathfile):
    l_ok = False
    for folder, subfolders, files in os.walk(root_dir):
        if folder != root_dir:
            for f in files:
                if f.upper()==doc_name.upper():
                    # print("File Name" , f)
                    # print(f"Path: ", os.path.join(folder, f))
                    l_ok = True
                    pathfile=os.path.join(folder, f)
                    break
        if l_ok:
            break
    return l_ok,pathfile
pathfileok = ''



# if recherche(root_dir,doc_name,pathfileok)[0]:
#     print(recherche(root_dir,doc_name,pathfileok)[1])
