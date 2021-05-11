##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima la suma de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    37
##  B    36
##  C    27
##  D    23
##  E    67
##  Name: _c2, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import csv
import numpy as np
df = open('tbl0.tsv')
reader = csv.reader(df, delimiter ='\t')
ls = []
ls = [ row for row in reader]
dat = pd.DataFrame(ls[1:], columns=ls[0])
dat['_c2'] = dat['_c2'].astype(int)
s=dat.groupby('_c1')
s=s['_c2'].agg([np.sum])
serie=pd.Series(s['sum'])
serie.name='_c2'
print(serie)
