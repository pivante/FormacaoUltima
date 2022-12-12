import pandas as pd
import numpy as np
import random as rd

lista = [16, 65, 19, 67, 80, 88, 32, 32, 77, 27]

df = np.array(lista)
print(df)

#Media
df.mean()

#----------------------------------------------------------------------------#
#Mediana

np.median(df, axis=0)

#----------------------------------------------------------------------------#
#Moda

#Criando a Frequencia para cada Elemento
frequencia = {numeros: 0 for numeros in set(df)}
frequencia

#Popular a frequencia checando a quantidade de elementos
for numero in df:
    frequencia[numero] += 1
print(frequencia)

np.unique(df, return_counts=True)

numeros, frequencia = np.unique(df, return_counts=True)
numeros[np.argmax(frequencia)]

#----------------------------------------------------------------------------#
#Lista de 1000 numeros aleatórios

lista_1000 = [rd.randrange(0, 100, 1) for i in range(1000)]
print(lista_1000)

#Media
np.mean(lista_1000)

#Mediana
np.median(lista_1000)

#Quartis
lista_1000

ser = pd.Series(data = lista_1000, index=[ i for i in range(1000)])
ser

type(ser)

ser.describe()

ser = ser.sort_values()

#Primeiro
ser.quantile(q=0.25)

#Segundo
ser.quantile(q=0.5)

#Terceiro
ser.quantile(q=0.75)

#Primeiro Quartil
ser[ser < ser.quantile(.25)].hist()

#Segundo Quartil
ser[ser < ser.quantile(.5)].hist()

#Terceiro Quartil
ser[ser < ser.quantile(.75)].hist()

