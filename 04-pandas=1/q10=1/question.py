##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
df = pd.read_csv('tbl2.tsv', sep='\t')
uniq=df['_c0'].unique()
df['lista'] = [str(df.loc[x,'_c5a'])+':'+str(df.loc[x,'_c5b']) for x in df.index]
serie=df.groupby('_c0')['lista'].apply(lambda x : ",".join(sorted(map(str, x))))
df2 = pd.DataFrame(serie)
df2.reset_index(inplace=True)
print(df2)
