from up_directory import  my_package_1,my_package_2
from up_directory.my_package_1 import my_module_1,my_module_2
from up_directory.my_package_2 import my_module_3,my_module_4
from up_directory.my_package_1.my_module_2 import divide
print(dir(my_package_1))

print(my_module_2.divide(10,5))
print(my_module_1.addition(5,10))

print(divide(10,5))

n=876509755433

print((list(str(n))[::-1]))
carpim=1
n=int(input("sayi gir"))
for i in  range(1,n+1):carpim*=i
print(carpim)
carpan=1


ops={"+":lambda x,y:x+y}
print(ops["+"](3, 5))
dicc={"a":1,"b":2}
print({x : y for x,y in dicc.items()})
