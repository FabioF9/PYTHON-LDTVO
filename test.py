import re
import os
path1="I:\\Doc-Technique\\"
path2="L:\\TAMPON\\"
path3="L:\\Projets\\"

str = "Hey, Copines is a good song; I like that song"

# print(re.split('; |, |\*|\n', str))
os.chdir(path3)
for i in range (len(os.listdir())):
    print(re.split('; |, |\\*|\n',os.listdir()[3]))