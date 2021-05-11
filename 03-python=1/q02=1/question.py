##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv
df = open("data.csv", "r")
reader = csv.reader(df, delimiter='\t')
ldf=[]
for row in reader:
    ldf.append(row)
row1= [row[0] for row in ldf]
uniq=sorted(list(set(row1))) 
for x in uniq:
    print(f'{x},{row1.count(x)}')
