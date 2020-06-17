
# coding: utf-8

# In[1]:


mat = [11,21,30,40,50,60,70,80] 
m=2 
n=4 
num = 50 
N = mat.index(num)+1 
print(N)
i = (((N-1))//n)+1 
j = ((N-1)%n)+1 
print (N,i,j)

