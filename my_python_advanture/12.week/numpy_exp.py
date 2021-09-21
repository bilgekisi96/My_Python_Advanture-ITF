import numpy as np
import pandas as pd


arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2.shape)
print(arr2[2][:2])
arrr4=np.array([[10,11,12]])
print((arr2+arrr4).shape)
print((arr2+arrr4).sum())
print(np.ones([3,3]))
print(np.eye(3))
print(np.random.rand(3,3))
print(np.full([2,2],10))
print(np.arange(0, 100, 5))
print(np.linspace(0,20,5))
listek=[1,2,3,4]
print(list(map(lambda a:a*3,listek)))




arrt=np.array([[1,2,3,4],[6,7,8,9]])
arrt1=np.array([[2,2,2,2],[3,3,3,3]])
result=0

for i,j in zip([1,2,3,4,5],[2,2,2,2,2]):result+=i*j
print(result)


import urllib.request

urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv',
    'climate.txt')

climate_data=np.genfromtxt("climate.txt",delimiter=",",skip_header=1)
print(climate_data.shape)
weigths=[0.3,0.2,0.5]
yields=np.dot(climate_data,weigths)
print(yields.shape)
climate_results=np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)
print(climate_results)

np.savetxt('climate_results.txt',
           climate_results,
           fmt='%.2f',
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples',
           comments='')

















