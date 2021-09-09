dicc={}
dicc[0],dicc[1]=1,2

print(dicc)

word_dicc={}
string="bugün ayrilikten bir önceki session"

for n in string:
    keys=word_dicc.keys()
    if n in word_dicc:
        word_dicc[n]+=1
    else:
        word_dicc[n]=1
print(word_dicc)

dicte={}
lisdicc=[]
veri = ["a", "b", True, (False, 1), {"1" : 2}, [1,2], {"2" : "two"}, {2, "3"}, "c", 23, 0]

solution=[[]]
num_list=[1,2,3]
for index in range(len(num_list)):
    solution=[i+[j] for i in solution for j in set(num_list).difference(set(i))]
    print(solution)



