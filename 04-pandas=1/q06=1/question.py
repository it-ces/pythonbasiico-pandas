##
##  Programación con Pandas
##  ===========================================================================
##
##  Agregue una columna con la suma de _c0 y _c2 al archivo `tbl0.tsv`. 
##
##  Rta/
##      _c0 _c1  _c2         _c3  suma
##  0     0   E    1  1999-02-28     1
##  1     1   A    2  1999-10-28     3
##  ...
##  38   38   E    1  1999-09-28    39
##  39   39   E    5  1998-01-26    44
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import os
import csv 
df = open('tbl0.tsv') 
reader = csv.reader(df, delimiter='\t')
ls=[]
ls = [row for row in reader]
df = pd.DataFrame(ls[1:], columns=ls[0])
l =['_c0', '_c2']
for x in l:
    df[x]= df[x].astype(int)
df['suma'] = df['_c0']  + df['_c2']
print(df)


