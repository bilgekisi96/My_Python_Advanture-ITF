

def repeater(n):
     return lambda x:print(x,n)

repeat_5=repeater(":(")

repeat_5("hello")
def repeater(num):
    return max(num,key=num.count),num.count(max(num,key=num.count))

print(repeater([1,2,3,4,5,5,5]))

equebrim=lambda x,y,z :[x,y,z].count((max([x,y,z],key=[x,y,z].count))) if  [x,y,z].count((max([x,y,z],key=[x,y,z].count)))>1 else 0
print(equebrim(1,4,4))

equebrima=lambda *arg :list(arg).count((max(list(arg),key=list(arg).count))) if  list(arg).count((max(list(arg),key=list(arg).count)))>1 else 0
print(equebrima(1,2,4,2))


#https://app.peardeck.com/presenter/tnypevayr/projector
import math
print(dir(math))
print(math.pi,math.log(1000,10),math.factorial(4))
#degişkenler ve fonksşyonlar import edilebilir
from math import pi,factorial,log10
print(factorial(5))
print(pi)
#punctiation kullanalım
import string
print(string.punctuation)#tüm noktalama işeratlerini verir
print(string.digits)
print(string.ascii_letters)

#datetime önemli
import datetime
print(datetime.date.today())
print(datetime.datetime.now())
birth=datetime.date(571,4,22)
vefat=datetime.date(632,6,8)
gun=datetime.date.toordinal(vefat)-datetime.date.toordinal(birth)
print(gun)


