hipp="hippo runs to us!"
count_list,hipp_list=[],list(hipp)
for i in hipp:count_list.append(hipp.count(i))
dicset=list(zip(hipp_list,count_list))
dicc={x:y for x,y in dicset}
print(dicc)


dcition={"+":lambda x,y:x+y}
print(dcition["+"](1,2))

sayac=10

def repeater(n):
     if n==9:
         return 2
     print(n)
     return n+repeater(n+1)
print(repeater(5))

