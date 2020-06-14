#!/usr/bin/env python
# coding: utf-8

# In[35]:


def Hashtag(string):
    x = string.split()
    y = len(x)
    
    if y > 0 :
        z = ''.join([x.capitalize() for x in x])
        word = '#'+z
        print(word)
    elif len (x) > 140 : # ini masih ambigu ka, 
        return False 
        
    else :
        print(False)
    


# In[39]:


Hashtag(" Hello there how are you doing ")


# In[57]:


def create_phone_number(number):
    x = "".join(map(str, number[0:3]))
    y = "".join(map(str, number[3:6]))
    z = "".join(map(str, number[6:10]))
    
    return '({}) {}-{}'.format(x, y, z)


# In[58]:


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# In[66]:


#1. lakukan sort untuk memudahkan dalam ganjil genap karena kanan kiri beda



list = [5, 3, 2, 8, 1, 4]
def sort_odd_even(num):


# In[75]:


x = [5, 3, 2, 8, 1, 4]
def sort_odd_even(x):
    E_list = []
    O_list = []
    
    for i in x:
        if i%2 == 0:
            E_list.append(i)
        else:
            O_list.append(i)
    E_list.sort(), O_list.sort()
    E_list.extend(O_list)
    return E_list

print (sort_odd_even(x))


# In[ ]:




