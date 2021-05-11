##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv
path ='/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q07=1'
os.chdir(path)
df = open('data.csv') 
reader = csv.reader(df, delimiter='\t')
dfl=[]
for row in reader:
    dfl.append(row)
df_=[[row[0], row[1]] for row in dfl]
unique = sorted(list(set([row[1] for row in df_])))
output=[]
for t in unique:
    aux = []
    for h in df_:
        if h[1]==t:
            aux.append(h[0])
    output.append((t,aux))
for out in output:
    print(out,sep='\n')
