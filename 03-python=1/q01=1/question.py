##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  >>> Escriba su codigo a partir de este punto <<<
import os
import csv
os.chdir("/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q01=1")
df = open("data.csv", "r")
reader = csv.reader(df, delimiter='\t')
ldf=[]
for row in reader:
    ldf.append(row)
row = [int(row[1]) for row in ldf]
print(sum(row))                  
