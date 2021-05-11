##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv 
import os
os.chdir('/home/ces/courses/evaluacion-del-curso-it-trj/03-python=1/q12=1')
df = open('data.csv')
reader = csv.reader(df, delimiter='\t')
df_=[]
for r in reader:
    df_.append(r)
values = [[r[0],r[4]] for r in df_]
num = [str(x) for x in range(11)]
data=[]
for t in values:
    valores=[]
    for a in t[1]:
        if a in num :
            valores.append(int(a))
    data.append([t[0], sum(valores)])
    
for j in data:
    print(j[0], j[1], sep=',')


















"""
values = [[x[0], (re.findall('[0-9]',x[4]))] for x in df_]
values2=[]
for x in values:
    numbers =[]
    for j in x[1]:
        numbers.append(int(j))
    values2.append([x[0], sum(numbers)])
for j in values2:
    print(j[0], j[1], sep=',')
    print('\n')
"""
