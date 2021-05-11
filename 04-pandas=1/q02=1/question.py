##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el promedio de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    4.625000
##  B    5.142857
##  C    5.400000
##  D    3.833333
##  E    4.785714
##  Name: _c2, dtype: float64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import pandas as pd
import os
import numpy as np
os.chdir('/home/ces/courses/evaluacion-del-curso-it-trj/04-pandas=1/q02=1')
df = open('tbl0.tsv')
read = csv.reader(df, delimiter='\t')
dfl=[]
for row in read:
    dfl.append(row)
data = pd.DataFrame(dfl ,columns=dfl[0] )
data =data.drop([0])
data['_c2']= data['_c2'].astype(float)
h=data.groupby('_c1')
h=h['_c2'].agg(['mean'])
ind = h.index
serie = pd.Series(h['mean'])
serie.name = '_c2'
print(serie)
