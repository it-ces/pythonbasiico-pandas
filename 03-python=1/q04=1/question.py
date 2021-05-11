##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import os
import csv 
os.chdir('/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q04=1')
df = open("data.csv", "r")
reader = csv.reader(df, delimiter='\t')
ldf=[]
for row in reader:
    ldf.append(row)
dates = [e[2] for e in  ldf]
dates = [e.split('-')[1] for e in dates] 
obj = sorted(list(set(dates)))
for x in obj:
    print(x,dates.count(x), sep=',')



