def bol(a,b):
    sifir,say=0,0
    while (a>=sifir):
        sifir+=b
        say+=1
    d=a-sifir+b
    c=say-1
    return c,d
print(bol(3,1))

