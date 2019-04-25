#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:30:53 2019

@author: khaled
"""

import pandas as pd
import numpy as np
#dataset_caharge=pd.read_csv("B0005_10_charge.csv")
dataset_discharge=pd.read_csv("New_dataset_LSTM.csv")
selec_battery_dataset=dataset_discharge[(dataset_discharge.Batt_name =="'B0005_14'")|
        (dataset_discharge.Batt_name =="'B0006_16'")|(dataset_discharge.Batt_name =="'B0007_13'")
        |(dataset_discharge.Batt_name =="'B0018_15'")]
selec_battery_dataset.to_csv("Batt_56718.csv")
######################################################
selec_battery_dataset=pd.read_csv("Batt_56718.csv")

#This function read each row form the dataset and finds the current battery when the voltage drop to vol
#These Lists used for creating new dataframe 
l1,l2,l3,l4,l5,l6,l7=[],[],[],[],[],[],[]
def get_list_C_T(dataset, vol):
    cycle=1
    check=True
    current=0
    time=0.0
    sum_discharge=[]
    time_dis=[]
    i=0
    names=dataset['Batt_name'][0]
    for j in range(len(dataset)):
        if names=="'B0005_14'":
            vol=2.7
        elif names=="'B0006_16'":
            vol=2.5
        elif names=="'B0007_13'":
            vol=2.2
        else:
            vol=2.5
        if cycle == dataset['cycle'][j] and names==dataset['Batt_name'][j]:
            if dataset['voltage_battery'][j]>= vol and check:
                current=dataset['current_battery'][j]  
                time=dataset['time'][j]
                #i=i+1
                
            else:
                sum_discharge.append(current)
                time_dis.append(time)
                l1.append(dataset['cycle'][j-1])
                l2.append(dataset['voltage_battery'][j-1])
                l3.append(dataset['time'][j-1])
                l4.append(dataset['temp_battery'][j-1])
                l5.append(names)
                l6.append(dataset['dateTime'][j-1])
                l7.append(dataset['amb_temp'][j-1])
                i=i+1
                #check=False
        else:
            cycle=dataset['cycle'][j]
            names=dataset['Batt_name'][j]
            current=0
            if names != dataset['Batt_name'][j]:
                i=0
    return sum_discharge,time_dis
#########################################################
sum_discharge=[]
time_dis=[]
sum_discharge,time_dis=get_list_C_T(selec_battery_dataset,2.7)
print(len(sum_discharge))

##########################################################
new_dataset=pd.DataFrame()
new_dataset['Batt_name']=l5
new_dataset['cycle']=l1
new_dataset['dateTime']=l6
new_dataset['amb_temp']=l7
new_dataset['voltage_battery']=l2
new_dataset['temp_battery']=l4
new_dataset['current_battery']=sum_discharge
new_dataset['time']=l3
#new_dataset['Capacity_online']=res
#########################################################
initCap=[1.8910523,1.85648742,1.85500452,2.03533759]
# This function do Calculation for Capcaity of all discharge cycle that store in the data
def Cap_Cal(dataset):
    list_Cap=[]
    Cap=[]
    cap=0
    ini_cap=initCap[cap]
    Cap.append(ini_cap)
    j=0
    names=dataset['Batt_name'][0]
    for i in range(len(dataset)):
        if j==0 and names == dataset['Batt_name'][i]:
            list_Cap.append(ini_cap)
            print(ini_cap)
            j=j+1
        elif j!=0 and names == dataset['Batt_name'][i]:
            dt=(dataset['time'][i] -dataset['time'][i-1])
            currents=(dataset['current_battery'][i])#+ sum_discharge[i-1])/2
            Cap_0=list_Cap[i-1]
            list_Cap.append((Cap_0-((currents*dt))/(3600)))
        elif j!=0 and names != dataset['Batt_name'][i] :
            print(i)
            names=dataset['Batt_name'][i]
            cap=cap+1
            ini_cap=initCap[cap]
            list_Cap.append(ini_cap)
   
    return list_Cap
###########################################################################

res=Cap_Cal(new_dataset)

new_dataset['Online_Capacity']=res
new_dataset.to_csv("Coll_Cap_file1.csv")
############testing#############################
test_data=new_dataset[(new_dataset.Batt_name=="'B0018_15'")]
res=test_data['Online_Capacity']
