
# coding: utf-8

# In[1]:


import re

inputFile = open("/Users/ankit/Desktop/ml.txt","r")
completeText = re.sub(r"[^a-zA-Z0-9]+", ' ', inputFile.read())
numberList = ""
l = len(numberList)
for text in completeText.split(' '):
	try:
		if(text!=""):
			numberList = numberList + re.sub(r"[^0-9]+","",text)
			if(len(numberList)>l):
				numberList += " "
				l = len(numberList)
	except ValueError:
		pass
		#print(text)
print(numberList)

