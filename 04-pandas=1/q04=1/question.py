##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv
import pandas as pd
import numpy as np
os.listdir()
os.chdir('/home/ces/courses/evaluacion-del-curso-it-trj/04-pandas=1/q04=1')
data = open('tbl1.tsv')
reader = csv.reader(data , delimiter ='\t')
ls = []
for d in reader:
    ls.append(d)
data = pd.DataFrame(ls[1:], columns=ls[0])   
x=list(pd.Series(data._c4.unique()).sort_values())
x = [t.upper() for t in x]
print(x)
