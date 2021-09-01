tic_tac_toe=[
  ["O", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]
for i in tic_tac_toe:
    if i.count("X" or "O")==3:
        print(i[0])
lis=[]
for j in range(len(tic_tac_toe[0])):
    lis=[k[j] for k in tic_tac_toe]

if "X" not in lis:print("O")
elif "O" not in lis:print("X")
else:print()

sayac=0
kiste=[]
for t in range(len(tic_tac_toe)):
    kiste=["O" if tic_tac_toe[t][sayac]!="X" else "X"]
    sayac+=1

if "X" not in kiste:print("O")
elif "O" not in kiste:print("X")
else:print()

artan=0
tekrar=range(len(tic_tac_toe))
for p in tekrar[::-1]:
    piste = ["cevap:O" if tic_tac_toe[p][artan] != "X" else "cevap:X"]
    artan += 1
    print(piste[0])




