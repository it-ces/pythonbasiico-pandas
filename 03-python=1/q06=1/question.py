##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
##
##  >>> Escriba su codigo a partir de este punto <<<
import os 
import csv 
df = open('data.csv')
reader = csv.reader(df, delimiter='\t' )
df = []
for line in reader:
    df.append(line)
row3=[x[4] for x in df] 
total=[x.split(',') for x in row3]
empty=[]
for x in total:
    for k in x:
        empty.append(k)
empty = list(set(empty))
let =sorted(list( set([x[0:3] for x in empty])))
dt = {x:[] for x in let}
df= [x.split(':') for x in empty]

for q in let:
    for j in df:
        if q ==j[0]:
            dt[q].extend(j[1])
#dicct.get('key') return the values of the key.
#dt= sorted(dt)
for s in range(len(list(dt.items()))):
   print(list(dt.items())[s][0], min(dt.get(list(dt.items())[s][0])), 
   max(dt.get(list(dt.items())[s][0])) , sep=',')
