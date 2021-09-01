
listem=["()","[]","{}"]
tup=("(",")","{","}","[","]")
res=dict(i for i in enumerate(tup))
print((res))
inpstrz=input("please enter str")
inpstr=list(inpstrz)
print(inpstr)
while True:
    if inpstr[-1]==(res[0] and res[2] and res[4]):
        print("invalid")
        break
    elif inpstr[0]==(res[1] and res[3] and res[5]):
        print("invalid")
        break
    elif (inpstr[0]+inpstr[-1]  in listem):
        print("True")
        break
    elif inpstr[0]!=inpstr[-1]:
        if (inpstr[-2]+inpstr[-1] in listem) and (inpstr[0]+inpstr[1]  in listem):
            print("True")
            break
        else:
            print("invalid")
            break
    elif inpstrz==" ":
        print("invalid")
        break
    else:
        print("true")
        break



















