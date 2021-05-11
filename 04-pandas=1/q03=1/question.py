##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el maximo de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    9
##  B    9
##  C    9
##  D    7
##  E    9
##  Name: _c2, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import pandas as pd
import os
import numpy as np
df = open('tbl0.tsv')
read = csv.reader(df, delimiter='\t')
dfl=[]
for row in read:
    dfl.append(row)
data = pd.DataFrame(dfl ,columns=dfl[0] )
data =data.drop([0])
data['_c2']= data['_c2'].astype(int)
h=data.groupby('_c1')
h=h['_c2'].agg(['max'])
ind = h.index
serie = pd.Series(h['max'])
serie.name = '_c2'
print(serie)

