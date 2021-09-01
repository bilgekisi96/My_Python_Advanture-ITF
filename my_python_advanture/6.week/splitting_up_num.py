def splitting_up(user_num):
    user_num=str(user_num)
    listem=[]
    ust,iteg_num,sayac=len(user_num),int(user_num),0
    if iteg_num<0:
        iteg_num = str(iteg_num)
        while 0<ust-1:
            num=int(iteg_num[ust-1])
            listem.append((-1)*num*(10**sayac))
            sayac +=1
            ust-=1
        return listem[::-1]
    else:
        for i in user_num:
            i=int(i)
            listem.append(i*(10**(ust-1)))
            ust-=1
        return listem
print(splitting_up(-125))
print(splitting_up(255))


