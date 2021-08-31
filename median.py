


median=[]
while(len(median)+1<=3):
    number = int(input("enter number for median:"))
    median.append(number)
devide=sum(median)//3
abss=[abs(sub-devide) for sub in median]
print(f"medyan:{median[abss.index(min(abss))]}")
