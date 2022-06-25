#!/usr/bin/env python
# coding: utf-8

# # Homework 1- Introducción a Python y a Git 
# ## Gabriela Cruz- 8-1008-430 | Programación para ingenieros 2022-2              

# 0: Crear un repositorio y un profile en github 

#  https://github.com/Gabrielazz 

# **Problema #1** Realice un programa que inserte la temperatura en grados celcius y la salida sea la temperatura en grados Kelvin.  Favor conseguir la siguiente salida, p.e. si la entrada es 25°C. 
# ![image.png](attachment:image.png)

# In[3]:


def Celsius_to_Kelvin(C):
    return (C + 273.15)

C= 25
print("Tú temperature en grados Kelvin es de (273.15) = ",
                    Celsius_to_Kelvin(C))


# **Problema #2**  Las estaturas de las siguientes 10 personas son las siguientes dadas en metros en el sistema internacional.
# h1 = 1.5m, h2 = 2.2m, h3 = 1.56m, h4 = 1.78m, h5 = 1.82m, h6 = 1.90m, h7 = 1.66m, h8 = 1.91m, h9 = 1.76m, h10=1.88m
# Calcule la media de los datos si la media esta dada por: 
# ![image.png](attachment:image.png)

# In[21]:


import numpy


# In[23]:


altura=numpy.array ([1.5, 2.2, 1.56, 1.78, 1.82,1.90, 1.66, 1.91, 1.76, 1.88],float)
media= altura.mean ()
print("la media de altura de 10 datos será de:")
print(media)


# **Problema #3** Calcule la desviación estándar de los 10 datos anteriores, si la desviación estándar es: 
# ![image.png](attachment:image.png) ![image-2.png](attachment:image-2.png)

# In[24]:


import statistics


# In[26]:


altura=numpy.array([1.5, 2.2, 1.56, 1.78, 1.82,1.90, 1.66, 1.91, 1.76, 1.88],float)

standar_desviation= statistics.pstdev(altura)

print("La desviacion estandar de la lista es de: " + str(standar_desviation)) 


# In[27]:


# no seguí el metodo dado en el word pero busque una solucion más "fácil" :D 

