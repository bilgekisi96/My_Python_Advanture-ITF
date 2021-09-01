satir=int(input("satir sayisini giriniz:"))
sutun=int(input("sutun sayisini giriniz:"))
dicc={}
for i in range(satir):
    dicc[i]=[]
    for j in range(sutun):
        dicc[i].append(i*j)
print([k for k in dicc.values()])




