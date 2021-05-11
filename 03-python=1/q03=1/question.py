##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import os
df = open("data.csv", "r")
reader = csv.reader(df, delimiter='\t')
ldf=[]
for row in reader:
    ldf.append(row)
pairs = [[row[0],int(row[1])] for row in ldf]
row=[row[0] for row in ldf]
lisum=[]
unique = set(row)
for value in unique:
    sum = 0
    for pair in pairs:
        if pair[0] == value:
            sum = sum + pair[1]
    lisum.append((value,sum))
lisum=(sorted(lisum, key = lambda x: x[0]))
for x,y in lisum:
    print(F"{x},{y}")
