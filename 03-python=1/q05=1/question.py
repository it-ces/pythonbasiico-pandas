##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv 
os.chdir("/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q05=1/")
df = open("data.csv", "r")
reader = csv.reader(df, delimiter='\t')
ldf=[]
for row in reader:
    ldf.append(row)
subase = [[e[0], int(e[1])] for e in ldf]
unique = sorted(list(set([e[0] for e in subase])))

lmax=[] 
## Minimun or maximun:
for k in unique:
    max=subase[0][1]
    min=subase[0][1]
    for subas in subase:
        if subas[1] > max and subas[0]==k:
            max = subas[1]
        if subas[1] < min and subas[0]==k:
            min = subas[1]
    lmax.append((k,max,min))
    print(k,max,min, sep=',')    






