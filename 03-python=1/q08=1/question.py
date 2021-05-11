##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv
path ='/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q07=1'
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
    output.append((t, sorted(list(set(aux)))))
for out in output:
      print(out,sep='\n')

