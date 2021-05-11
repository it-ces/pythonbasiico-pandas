##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
import pandas as pd
df = open('tbl0.tsv')
reader = csv.reader(df, delimiter='\t')
base=[row for row in reader]
data = pd.DataFrame(base[1:], columns= base[0])
unique=data['_c1'].unique()
dat= [[data.loc[x,'_c1'], data.loc[x,'_c2']] for x in data.index]
tab=[]
for i in sorted( list(unique)):
    lis=[]
    for x in dat:
        if x[0]==i:
            lis.append(str(x[1]))
    tab.append([i, sorted(lis)])
table =pd.DataFrame(tab , columns=['_c0','lista']) 
table['lista'] = [':'.join(map(str,j)) for j in table['lista']]
print(table[['_c0','lista']])
