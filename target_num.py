
"""
user=int(input("lutfen sayi giriniz"))
nums = [2, 7, 11, 15]
listem,fin_list=[],[]
for x in nums:
    for y in nums:
        if y!=x:
            listem.append((x,y))
for i,j in listem:
    if (i+j)==user:
        fin_list.append((nums.index(i),nums.index(j)))
print(fin_list[0])

print(chr(89))

"""
"""
sevenBoom=[1, 2, 3,102545475312545465, 4, 5, 6]
j=""
for i in sevenBoom:
    i=str(i)
    j+=i
if "7" in j:print("boom!")
else:print("thre is no seven in the array")

"""

#0 (0)
#1 (2**0)
#2 (2**1)+(2**0)
#3 (2**2)+(2**1)+(2**0)
#4 (2**3)+(2**2)+(2**1)+(2**0)
"""
n=int(input("lütfen sayi giriniz"))
toplam=0
for i in range(n):
    toplam+=2**i
print(toplam)

"""

"""
countBoomerangs = [4, 4, 4, 9, 9, 9, 9]
count=0

for i in range(len(countBoomerangs)-3):
    a,b,c=countBoomerangs[i],countBoomerangs[i+1],countBoomerangs[i+2]
    print(a,b,c)
    if a==c!=b:
        count+=1
print(count)

"""
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    division = no_one / no_two
    print("The result of the division is : ", division)
    break






































