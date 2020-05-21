#!/usr/bin/env python
# coding: utf-8

# In[1]:


###remove case sensitivity
#input file is ds.csv

import hashlib


countries = ['India',
'China',
'Pakistan',
'Bangladesh',
'Afghanistan']

events=['Civil unrest',
'Attack',
'Disease outbreak',
'Flood']

months=['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']
#Provinces of Pakistan
provincePak= ['Sindh',
'Punjab',
'Balochistan',
'Khyber Pakhtunkhwa',
'Gilgit Baltistan',
'Azad Kashmir',
'Islamabad']
#Provinces of China:

provinceChina=['Qinghai',
'Sichuan',
'Gansu',
'Heilongjiang',
'Yunnan',
'Hunan',
'Shaanxi',
'Hebei',
'Jilin',
'Hubei',
'Hubei',
'Guizhou',
'Guangdong',
'Jiangxi',
'Henan',
'Shanxi',
'Shandong',
'Liaoning',
'Anhui',
'Fujian',
'Jiangsu',
'Zhejiang',
'Taiwan',
'Hainan',
'Hong Kong',
'Tibet',
'Beijing',
'Xinjiang',
'Suzhou']

provinceIndia =['Andhra Pradesh',
                'Arunachal Pradesh',
                'Assam',
                'Bihar',
                'Chhattisgarh',
                'Goa',
                'Gujarat',
                'Haryana',
                'Himachal Pradesh',
                'Jharkhand',
                'Karnataka',
                'Kerala',
                'Madhya Pradesh',
                'Maharashtra',
                'Manipur',
                'Meghalaya',
                'Mizoram',
                'Nagaland',
                'Odisha',
                'Punjab',##########
                'Rajasthan',
                'Sikkim',
                'Tamil Nadu',
                'Telangana',
                'Tripura',
                'Uttar Pradesh',
                'Uttarakhand',
                'West Bengal',
                'Andaman and Nicobar Islands',
                'Chandigarh',
                'Dadra & Nagar Haveli and Daman & Diu',
                'Delhi',
                'Kashmir',#
                'Lakshadweep',
                'Puducherry',
                'Ladakh']


# In[2]:


dCountries = {}
dEvents = {}
dProvincePak = {}
dProvinceChina = {}
dProvinceIndia = {}
dMonths = {}

for a in countries:
    dCountries[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)
    
for a in months:
    dMonths[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)
    
for a in events:
    dEvents[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)
###LINES CAN BE REDUCED - MERGE LISTS AND ENCODE
for a in provincePak:
    dProvincePak[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)
    
for a in provinceChina:
    dProvinceChina[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)

for a in provinceIndia:
    dProvinceIndia[a] = int(hashlib.sha512(a.encode()).hexdigest()[0:10], 16)
    

#merging dictionaries for province
dProvince = {**dProvincePak, **dProvinceChina, **dProvinceIndia}


# In[4]:


def getEvent(val): 
    for key, value in dEvents.items(): 
         if val == value: 
             return key
def getCountry(val): 
    for key, value in dCountries.items(): 
         if val == value: 
             return key
def getMonth(val): 
    for key, value in dMonths.items(): 
         if val == value: 
             return key
def getProvince(val): 
    for key, value in dProvince.items(): 
         if val == value: 
             return key



import csv
filename = "dataset.xls"#-------------------------INPUT



fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        rows.append(row)



hashRows = []###TO AVOID CASE SENSITIVITY: dictionary should be all lower, country.lower() etc. should be used.
for country, year, month, event, province in rows:
    hashRows.append([ str(dCountries[country]), year, str(dMonths[month]), str(dEvents[event]), str(dProvince[province]) ])



filename2 = "dsHash2.csv"
with open(filename2, 'w') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter=',', lineterminator='\r')
    csvwriter.writerow(fields)
    csvwriter.writerows(hashRows)



csvfile.close()
csvfile2.close()



fields = []
rows2 = []
filename = "dsHash2.csv"
with open(filename, 'r', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        rows2.append(row)


#Now training the model using training data---------------------------------------------------#



import pandas as pd
import numpy as np
df=pd.read_csv("dsHash2.csv")
from sklearn.model_selection import train_test_split



x=df[['Country','Year','Month','Event']]#modify it to provide different set of inputs
y=df['State/Province']#prediction

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0)



#predicting result using decision tree &
#predicting result using KNN, Naive Bayes
from sklearn import datasets 
from sklearn.metrics import confusion_matrix 


#1. Decision Tree -----------------------------
from sklearn.tree import DecisionTreeClassifier
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(x_train, y_train)
#predicting
dtree_predictions = dtree_model.predict(x_test)


# creating a confusion matrix 
cm = confusion_matrix(y_test, dtree_predictions) 




# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 7).fit(x_train, y_train) 
  
# accuracy on X_test 
accuracy = knn.score(x_test, y_test) 
  
# creating a confusion matrix 
knn_predictions = knn.predict(x_test)  
cm = confusion_matrix(y_test, knn_predictions) 



# predicting result using Naive Bayes----------------

# training a Naive Bayes classifier 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB().fit(x_train, y_train) 
gnb_predictions = gnb.predict(x_test)


# accuracy on X_test 
accuracy = gnb.score(x_test, y_test)  
# creating a confusion matrix 
cm = confusion_matrix(y_test, gnb_predictions) 



#predicting eventCAUTION - DO NOT REMOVE!---------------------------------------------------------
#1. DT
'''
def predictDTree(country, year, month, province):
    result = dtree_model.predict([ [dCountries[country], 2020, dMonths[month], dProvince[province] ] ])
    return getEvent(result)

a = predictDTree('India', 2020, 'June', 'Maharashtra')

def predictKNN(country, year, month, province):
    result = knn.predict([ [dCountries[country], 2020, dMonths[month], dProvince[province] ] ])
    return getEvent(result)

b = predictKNN('India', 2020, 'June', 'West Bengal')

def predictGNB(country, year, month, province):
    result = gnb.predict([ [dCountries[country], 2020, dMonths[month], dProvince[province] ] ])
    return getEvent(result)
c = predictGNB('India', 2020, 'June', 'Odisha')
'''
#----------------------------------------------------------------------------------------------------

# In[31]:

#province prediction

def predictDTree(country, year, month, event):
    result = dtree_model.predict([ [dCountries[country], 2020, dMonths[month], dEvents[event] ] ])
    return getProvince(result)

a = predictDTree('India', 2020, 'June', 'Flood')


def predictKNN(country, year, month, event):
    result = knn.predict([ [dCountries[country], 2020, dMonths[month],dEvents[event] ] ])
    return getProvince(result)

b = predictKNN('India', 2020, 'June', 'Attack')


def predictGNB(country, year, month, event):
    result = gnb.predict([ [dCountries[country], 2020, dMonths[month], dEvents[event] ] ])
    return getProvince(result)
c = predictGNB('India', 2020, 'June', 'Civil unrest')

