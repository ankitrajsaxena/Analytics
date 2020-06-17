#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:11:17 2019

@author: ankit
"""

import re
import sys

def isMonth(text):
	months = ['January','February','March','April','May','June','July','August','September','October','November','December']
	if text in months:
		return True
	return False

def isNum(text):
	try:
		a = int(text)
		return True
	except ValueError:
		num = ['0','1','2','3','4','5','6','7','8','9']
		for i in num:
			if i in text:
				return True
		return False

inputFile = open("ml.txt","r", encoding='cp932', errors='ignore')
#completeText = re.sub(r"[^a-zA-Z0-9,.$]+", ' ', inputFile.read())
completeTextList = [re.sub(r"[^a-zA-Z0-9,.$]+", ' ', i) for i in inputFile.readlines()]

dateList, dollarList, numberList = [], [], []
for c in range(len(completeTextList)):
	textList = completeTextList[c].split(' ')

	i = 0
	while i < len(textList):
		if(isMonth(textList[i])):
			if(textList[i+1].split(',')[1]==''):
				dateList.append(' '.join(textList[i:i+3]))
				i = i+3
				continue
			else:
				dateList.append(' '.join(textList[i:i+2]))
				i = i+2
				continue
		elif('$' in textList[i]):
			dollarList.append(''.join(textList[i]))
		elif(isNum(textList[i])):
			#print(' ',textList[i])
			numberList.append((c+1,re.sub(r"[^0-9,.]",'',textList[i])))
		i = i + 1
print(dateList)
print(dollarList)
print(numberList)

'''
completeText = re.sub(r"[^a-zA-Z0-9]+", ' ', inputFile.read())
numberList = []
for text in completeText.split(' '):
	try:
		numberList.append(int(text))
	except ValueError:
		pass
		#print(text)
print(numberList)
'''
