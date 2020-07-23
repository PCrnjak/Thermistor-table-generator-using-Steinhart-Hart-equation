"""
   Author : Petar Crnjak
   Copyright: GNU General Public License v3.0
   Version: 1.0
   Additional Contributions:
   Date: 23.7.2020.

"""

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

#https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
R_series = 51000
table_size = 1024
Vref = 3.3

T1 = 10 
T2 = 36 
T3 = 100 
Rt1 = 186000
Rt2 = 64000
Rt3 = 7000

T1 = T1 + 273.15
T2 = T2 + 273.15
T3 = T3 + 273.15

 #A + B*ln(R1) + C *(ln(R1))**3 = T1
 #A + B*ln(R2) + C *(ln(R2))**3 = T2
 #A + B*ln(R3) + C *(ln(R3))**3 = T3

X = np.array([[1 , np.log(Rt1) , ((np.log(Rt1))**3)] , [1 , np.log(Rt2) , ((np.log(Rt2))**3)] , [1 , np.log(Rt3) , ((np.log(Rt3))**3)]])
Y = np.array([1/T1 , 1/T2 ,1/T3])

coefs = np.linalg.solve(X,Y)

A = coefs[0]
B = coefs[1]
C = coefs[2]

R_table = np.array([])
T_table = np.array([])

for i in range(0,table_size):

    if( i == 0 ):
        sensor = 1
    else:
        sensor = i

    R_table_temp =  ((table_size) * R_series - sensor * R_series ) / sensor 
    T_table_temp = A + B * np.log(R_table_temp) + C * (np.log(R_table_temp))**3
    T_table_temp = 1 / T_table_temp -273.15

    R_table = np.append(R_table , R_table_temp)
    T_table = np.append(T_table , T_table_temp)

    print(T_table[i])
    #print(sensor)

plt.plot(T_table,R_table)
plt.xlabel('Temperature (°C)')
plt.ylabel('Resistance')
plt.title('Temp/Resistance graph')
plt.legend()
plt.show()


T_table = T_table.astype(int)
Last_T = T_table[len(T_table)-1]

T_table = np.delete(T_table, -1)

# Edit YOUR_PATH to path you want to save your file:
# Example: C:\Users\Name\Desktop\my_file_2.csv

# Save array witout last element to csv file
np.savetxt(r'C:\\Users\\Rope_laptop\\Desktop\\my_file_5.txt', T_table, newline = ',',fmt= '%-1.1d')
# Save last element to csv file (this remove last comma)
file = open(r'C:\\Users\\Rope_laptop\\Desktop\\my_file_5.txt','a')
file.write(str(Last_T))
file.close()