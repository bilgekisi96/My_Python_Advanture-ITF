import math as mat
import sys as sy
import numpy as np
import time
import statistics as sta

input=[("b",1),("c",2),("x",3),("x",4),("z",0)]
dicct={i:j for j,i in input}
output=[(dicct[k],k) for k in sorted(dicct.keys())]
print(output)

start=time.time()

dizi= [2, 1, 5, 7, 2, 0, 5]
print([sta.median(dizi[:i]) for i in range(1,len(dizi)+1)])
print("my code time",(time.time()-start)*1000)


liste=range(1000)
print(sy.getsizeof(5)*len(liste))


arrayy=np.arange(1000)
print(arrayy.size*arrayy.itemsize)
print(arrayy.nbytes)

arre=np.array([[1,2,3],[3,4,5]])
print(arre.nbytes)
print(arre.dtype)

print(np.zeros((4,4)))
#print(np.concatenate((arre,np.array([[1,4,7]]).T),axis=1))
#print(arre.dot(arre))


print(arre.reshape(3,2).sum(axis=0))




















