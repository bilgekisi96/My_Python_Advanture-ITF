sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]


sayac=0
cizgi=0
print("- - - - - - - - - - - - - - - ")
while sayac<9:
    for k,z in [(0,3),(3,6),(6,9)]:
        for i in sudoku[sayac][k:z]:
            print(i,end=" ")
        print(end="|")
        print(end=" ")
    print(end="\n")
    if cizgi==2 or cizgi==5 or cizgi==8:
        print("- - - - - - - - - - - - - -")
    cizgi+=1
    sayac+=1





"""
for k,p in [(0,3),(3,6),(6,9)]:
    for i in sudoku[:3]:
        for j in i[k:p]:
            print(j,end=" ")
        print(end="|")
        print(end="\n")
    
"""


"""
print("- - - - - - - - - - - - - - - ")
for i in sudoku[:3]:
    print()
    for j in i:
        print(j,end=" ")
print(end="\n")
print("- - - - - - - - - - - - - - - ")
"""

























