##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import re
df = open('data.csv')
reader  = csv.reader(df, delimiter='\t')
dfl=[]
for r in reader:
    dfl.append(r)
subdata = [[r[0],r[3], r[4]] for r in dfl]
for x in subdata:
    print(x[0],len("".join(re.findall('[^,]', x[1]))) , x[2].count(':'), sep=',')
