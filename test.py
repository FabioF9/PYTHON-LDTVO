# chaine="bonjour test"
# if "bonjour" in chaine:
#     print ('True')
# fullstring = "StackAbuse"
# substring = "tack"
fullstring="\\serveur\\Donnees-LDTVO\\AccessROVJET\\2-Part_drawing\\0427_A11_DE001 (P00-215-52).pdf;0427_A11_DE001 (P00-215-52).pdf"
substring="2-Part_drawing\\"
try:
    fullstring.index(substring)
except ValueError:
    print("Not found!")
else:
    print(fullstring.index(substring))
    print(fullstring[fullstring.index(substring):])