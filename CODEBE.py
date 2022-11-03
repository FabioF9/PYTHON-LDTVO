import os
path1="I:\\Doc-Technique\\"
path2="L:\\TAMPON\\"
path3="L:\\Projets\\"
file=open("C:\\test\\rapport1.csv","w")
os.chdir(path1)
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir()[11].rsplit('-'),)
for i in range (len(os.listdir())):
    print(os.listdir()[i][0:4] + ';'+ os.listdir()[i][7:])
    file.write (os.listdir()[i][0:4] + ';'+ os.listdir()[i][7:]+"\n")
    # print(os.listdir()[i].rsplit('-'))
    # file.write (os.listdir()[i].rsplit('-')[0]+"\n")
file.close()
file=open("C:\\test\\rapport2.csv","w")
os.chdir(path2)
for i in range (len(os.listdir())):
    print(os.listdir()[i][0:4] + ';'+ os.listdir()[i][7:])
    file.write (os.listdir()[i][0:4] + ';'+ os.listdir()[i][7:]+"\n")
#     print(os.listdir()[i].rsplit('-'))
#     file.write (os.listdir()[i].rsplit('-')[0]+"\n")
file.close()
file=open("C:\\test\\rapport3.csv","w")
os.chdir(path3)
for i in range (len(os.listdir())):
    print(os.listdir()[i][0:4] + ';'+ os.listdir()[i][5:])
    file.write (os.listdir()[i][0:4] + ';'+ os.listdir()[i][5:]+"\n")
#     print(os.listdir()[i].rsplit('-'))
#     file.write (os.listdir()[i].rsplit('-')[0]+"\n")
file.close()
    
