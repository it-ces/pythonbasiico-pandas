##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import string 

def fc(letter, lista):
    sum = 0
    for k in lista:
        if letter in k[1]:
            sum = sum + int(k[0])
    return sum
df = open('data.csv')
reader = csv.reader(df, delimiter='\t')
df_ = []
for r in reader:
    df_.append(r)
subset = [[row[1], row[3]] for row in df_]
abc = list(string.ascii_lowercase)
outp=[]
for h in abc:
    aux= fc(h,subset)
    if aux !=0:
        outp.append([h,aux])
for x in outp:
    print(x[0], x[1], sep=',')
