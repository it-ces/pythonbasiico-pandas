##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv
df = open('data.csv')
reader = csv.reader(df, delimiter ='\t')
dfl=[]
for r in reader:
    dfl.append(r)
i = [k[4] for k in dfl]
il=[]
for m in i:
    for i in m.split(','):
        il.append(i)
unique = sorted(list(set(il))) 
unique2=[x[0:3] for x in il]
unique3 =sorted(list(set(unique2)))
for d in unique3:
    print(d, unique2.count(d),sep=',')
