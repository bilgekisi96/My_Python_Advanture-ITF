

def digitnum(user):
    digit = ""
    for i in range(user):digit +=str(i)
    return len(digit)-1
print(digitnum(2020))

toplam=0

listem=[]
def digit(kul):
    for sayi in range(kul):
        basamak = 1
        while sayi>=10:
            sayi/=10
            basamak+=1
        listem.append(basamak)
    return sum(listem)-1
print(digit(100))
