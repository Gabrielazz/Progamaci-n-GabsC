#!/usr/bin/env python
# coding: utf-8

# # Laboratorio 2 - lista, arreglos y Numpy 
# ## Gabriela Cruz 8-1008-430 | programación para ingenieros 2022-2 

# In[3]:


import numpy as np
import time as t


# **Problema #1** Crear un arreglo con las siguientes especificaciones
# 
# 5x2x3
# numeros consecutivos de 2 a 60 (incluyendo el número 60)
# pasos de 2 
# 

# In[77]:


x=np.array([2, 4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60]).reshape((5,2,3))
print(x) 


# **Problema #2** Crear un arreglo 5x6
# El arreglo debe contener enteros consecutivos desde 1 hasta 30 (incluyendo el 30)
# Luego seleccione solo los numeros impares en el arreglo
# NOTA: No se acepta la creación del arreglo como np.array([1,2,3...30] 

# In[90]:


x=np.arange(1, 31).reshape((5,6))
print(x)
# respuesta esperada 1 


# In[9]:


list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
i= 0 

while(i < len(list1)):
      
    
    if list1[i] % 2 != 0:
        print(list1[i], end = " ")
      
    
    i += 1
    
 # respuesta esperada 2   


# **Problema #3** Utilice broadcasting en numpy para crear un arreglo como se especifica:
# 
# Arreglo 4x8
# col1 = llena de 1s, col2 = llena de 2s ... col8 = llena de 8s. 

# In[13]:


import numpy as np


# In[16]:


x=np.zeros((4, 8))
print(x)


# In[15]:


x, y = np.mgrid [1:5, 1:9]
y

