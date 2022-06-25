#!/usr/bin/env python
# coding: utf-8

# # Laboratorio 1- básico de python 
# ## Gabriela Cruz 8-1008-430 | programación para ingenieros 2022-2
# Aplicando matematicas en python :D 

# **Problema #1** 
# Suponga que tiene 100 dólares, los cuales ud invierte y adquiere un 10% anual de retorno. Añada el código y calcule el interes compuesto para 7 años de inversión bancaria e imprima el resultado. 

# In[1]:


# Calculando el interes compuesto


# In[1]:


Inversión=100 
Años=7 
InteresAnual=10 
interesCompuesto= 100*(1+0.1)**7
print("tu interes compuesto luego de 7 años será de: ") 
print(interesCompuesto)


# **Problema #2** Cree una variable llamada 'ahorros' con el valor 100
# 
# Imprima la variable 

# In[2]:


Ahorros=100 
print(Ahorros)


# **Problema #3** En vez de calcular con los valores actuales ud puede utilizar variables.
# 
# Siga los siguientes pasos para realizarlo de manera con variables. 

# In[3]:


ahorro=int(100)
mult_anual=float(1.1)
result=ahorro*(mult_anual)**7
print(result)


# **Problema #4** Crear una nueva variable llamada 'desc' de tipo 'string' que contenca la palabra 'cadena de texto' Crear un nuevo booleano llamado 'profit' que tenga asignado el valor True. 

# In[4]:


desc=str("cadena de texto")
print(desc)
profit=bool(True)
print(bool(profit))


# **Problema #5** Calcule el producto de los ahorros y el multiplicador, almacene el resultado en la palabra año. 

# In[5]:


ahorros = 100
mult = float (1.1)
desc = 'interes compuesto'
año1 = ahorro*(mult)
print(año1)
print(type(año1))
dobledesc= desc + desc 
print(dobledesc)


# **Problema #6** Arregle la cadena para imprimir. 

# In[7]:


ahorros = 100
resultado = 100*1.1**7 
print("Empezamos con")
print(100) 
print("y ahora tenemos")
print(float(194.87171000000012))
print("Que bien!")


# In[6]:


pi_string = "3.1415926"
print(type(pi_string))

pi_float= float(pi_string)
print(pi_float)
print(type(pi_float))

