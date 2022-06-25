#!/usr/bin/env python
# coding: utf-8

# # Tarea 2-  Listas, Arreglos 2D y Numpy 
# ## Gabriela Cruz 8-1008-430 | programación para ingenieros 2022-2 

# **Problema #1** Cree un arreglo numpy con los valores inferiores de la Tarea 1 para adquirir por medio la paquetería numpy el calculo de la media.
# h1 = 1.5m, h2 = 2.2m, h3 = 1.56m, h4 = 1.78m, h5 = 1.82m, h6 = 1.90m, h7 = 1.66m, h8 = 1.91m, h9 = 1.76m, h10=1.88m
# Calcule la media de los datos si la media esta dada por
#                                                     ![image.png](attachment:image.png)
#                                                     
#   ![image-2.png](attachment:image-2.png)                                                   

# In[1]:


import numpy as np 
import statistics 


# In[3]:


altura=np.array ([1.5, 2.2, 1.56, 1.78, 1.82,1.90, 1.66, 1.91, 1.76, 1.88],float)
media= altura.mean ()
print("la media de altura de 10 datos será de:")
print(media) 


# **Problema #2** Calcule la desviación estándar de los 10 datos anteriores, si la desviación estándar es: 
#                                               ![image.png](attachment:image.png) 
#         ![image-2.png](attachment:image-2.png) 

# In[3]:


altura=np.array([1.5, 2.2, 1.56, 1.78, 1.82,1.90, 1.66, 1.91, 1.76, 1.88],float)

standar_desviation= statistics.pstdev(altura)

print("La desviacion estandar de la lista es de: " + str(standar_desviation)) 


# **Problema #3** Dataset =  [0.56744433976086,  0.6871979493457484, 0.8463706897561651, 0.31110389619407564, 0.23511891089708503, 0.6577102252485975, 0.6648803069356928, 0.49989209380778477, 0.023793000481246773, 0.8777416618364761, 0.45262683262543646, 0.6430419554811486, 0.06347145550399458, 0.10628535246898096, 0.13551828266629173, 0.7030802149078524, 0.8656176079542628, 0.3939640454664668, 0.5144582885753547, 0.6255032779041944]
# 
# Aplique los siguientes calculos
# •	La totalidad de datos
# •	La media
# •	La mediana
# •	La desviación estándar
# Reordene el arreglo en 5 filas y 4 columnas y aplique lo siguiente
# •	La media para la segunda columna
# •	La mediana para la tercera fila de datos
# •	La desviación estándar para los datos de la fila 3 a 5 y las columnas 1 a 3
# 

# In[35]:


#La totalidad de los datos 
# la media 
#desviación estándar
#mediana 

mn = np.mean(dataset)
st = np.std(dataset)
su = np.sum(dataset)
print(f'Media: {mn}\nDesv Est: {mi}\nTotal: {su}')

median= np.median(dataset)
print("tu mediana es de: ", (median))


# In[7]:


#reordene el arreglo en 5 filas y 4 columnas 
dataset= np.array([0.56744433976086,  0.6871979493457484, 0.8463706897561651, 0.31110389619407564, 0.23511891089708503, 0.6577102252485975, 0.6648803069356928, 0.49989209380778477, 0.023793000481246773, 0.8777416618364761, 0.45262683262543646, 0.6430419554811486, 0.06347145550399458, 0.10628535246898096, 0.13551828266629173, 0.7030802149078524, 0.8656176079542628, 0.3939640454664668, 0.5144582885753547, 0.6255032779041944
]).reshape((5,4))
print(dataset)


# In[36]:


#Media para la segunda columna 
media2= ([0.68719795, 0.65771023, 0.87774166, 0.10628535, 0.39396405]) 

mn = np.mean(media2)
print(mn)


# In[37]:


#Media para la tercera fila de datos 

media3= ([0.023793,0.87774166, 0.45262683,0.64304196])

mn= np.mean(media3)
print(mn)


# In[40]:


# La desviación estándar para los datos de la fila 3 a 5 
 
desv1= ([0.023793,0.87774166, 0.45262683,0.64304196, 0.06347146, 0.10628535, 0.13551828, 0.70308021, 0.86561761, 0.39396405, 0.51445829, 0.62550328])
st1= np.std(desv1)

print(st1)


# In[44]:


#Desviación estándar de las columnas 1 a 3 

desv2=([0.56744434,0.23511891, 0.023793, 0.06347146, 0.86561761, 0.68719795, 0.65771023, 0.87774166, 0.10628535, 0.39396405,0.84637069, 0.66488031, 0.45262683, 0.13551828, 0.51445829])

standar_desviation= statistics.pstdev(desv2)

print(standar_desviation)

