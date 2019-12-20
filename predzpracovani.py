with open('hodc.m', 'r+',encoding="utf-8") as fr: #otevře soubor pro čtení, s kódováním vhodným pro české znaky
    lines = fr.readlines()   #uloží otevřený soubor do proměnné lines
a = 0
for line in lines:
    a = a + 1   #počítá počet řádků kódu
    line = line.replace(" ", "")   #odstraní bílé znaky
    temp = line.find("%")   #najde index se značkou pro komentář
    line = line.replace(line[temp:], "")  #odstraní značku pro koment a vše za ní
    print(line)
print(lines)
