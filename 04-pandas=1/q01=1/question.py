##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima la cantidad de registros por cada letra 
##  de la columna _c1 del archivo `data.tsv` usando pandas.
## 
##  Rta/
##  _c1
##  A     8
##  B     7
##  C     5
##  D     6
##  E    14
##  Name: _c0, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import pandas as pd
import os
os.chdir('/home/ces/courses/evaluacion-del-curso-it-trj/04-pandas=1/q01=1')
df = open('data.tsv')
reader = csv.DictReader(df, delimiter='\t')
df_=[]
for r in reader:
    df_.append(r)
dat =pd.DataFrame(df_)
g=pd.DataFrame()
g['_c0']= dat['_c1']
dat = g['_c0'].value_counts().sort_index()
dat.index.name='_c1'
print(dat)

