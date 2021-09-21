
chess_board=(11,12,13,14,15,16,17,18,
             21,22,23,24,25,26,27,28,
             31,32,33,34,35,36,37,38,
             41,42,43,44,45,46,47,48,
             51,52,53,54,55,56,57,58,
             61,62,63,64,65,66,67,68,
             71,72,73,74,75,76,77,78,
             81,82,83,84,85,86,87,88)
kasar=[]
for phrase in 11,:
    for user in 11,23:
        mun,users,minuser,minuserset,munk,usersk,minuserk,minusersetk=user,user,user,user,user,user,user,user
        fil_move,kale_move=[],[]
        for i in range(8):
            if users in chess_board:
                    fil_move.append(users)
                    users+=11
            if mun in chess_board:
                    fil_move.append(mun)
                    mun-=11
            if minuser in chess_board:
                    fil_move.append(minuser)
                    minuser+=9
            if minuserset in chess_board:
                    fil_move.append(minuserset)
                    minuserset-=9
        for j in range(8):
            if usersk in chess_board:
                    kale_move.append(usersk)
                    usersk+=10
            if munk in chess_board:
                    kale_move.append(munk)
                    munk-=10
            if minuserk in chess_board:
                    kale_move.append(minuserk)
                    minuserk+=1
            if minusersetk in chess_board:
                    kale_move.append(minusersetk)
                    minusersetk-=1
        kume=set(fil_move).union(kale_move)
        kasar.append(kume)
print(kasar)
print(set(chess_board).difference(set(kasar[0].union(kasar[1]))))







