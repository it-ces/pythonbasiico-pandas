##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
dat = pd.read_csv('tbl1.tsv', sep='\t')
uniq = list( dat['_c0'].unique())
pairs =[[dat.loc[x,'_c0'], dat.loc[x,'_c4']] for x in dat.index]
base=[]
for i in uniq:
    vector=[]
    for x in pairs:
        if x[0] == i:
            vector.append(x[1])
    base.append([i, sorted(vector)])
table=pd.DataFrame(base, columns=['_c0','lista'])
table['lista']=[",".join(map(str , j)) for j in table['lista']]
print(table[['_c0','lista']])  

        
