#!/usr/bin/env python
# coding: utf-8

# # Bootcamp : Python'a Giriş
# ## 2.2. Python Temeller
# ### Bileşik Faiz Hesaplama

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


faiz = input('Dönemsel Faiz Oranı : ')
anapara = input('Anapara :') 
dönemsayısı=input('Dönem Sayısı :')


# In[8]:


anaparaf = float(anapara)
faizf= float(faiz)/100
kazanc = anaparaf * (1 + faizf)**int(dönemsayısı) - anaparaf

cıktı = 'Hafta başında 1000 dolarlık bitcoin aldığımızda günde ortalama %{} kazançla,bir hafta sonunda {:.2f} dolar kazanırdık.'
print (cıktı.format(faiz,kazanc))


# ### Yatırım Hesaplayıcı

# In[5]:


yatırımaracı=input('Yatırım Aracı:')
faiz = input('Dönemsel Faiz Oranı : ')
anapara = input('Anapara :') 
dönemsayısı=input('Dönem Sayısı (Gün/Ay/Yıl) :')
anaparaf = float(anapara)
faizf= float(faiz)/100
kazanc = anaparaf * (1 + faizf)**int(dönemsayısı) - anaparaf


cıktı = '{} dolarlık {} aldığımızda dönemlik ortalama yüzde %{} kazançla,{} dönem(gün/ay/yıl) sonunda {:.2f} dolar  kazanırdık.'
print (cıktı.format(anaparaf,yatırımaracı,faiz,dönemsayısı,kazanc))

