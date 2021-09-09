

list_alp=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
table=[str(i)+str(j) for i in range(1,7) for j in range(1, 7)]
dicc_alp,dicc_digit={k:l for k,l in zip(list_alp,table)},{l:k for k,l in zip(list_alp,table)}

print(dicc_alp)
print(dicc_digit)
def polybius(exp):
    str_final=""
    exp=exp.lower()
    #for der in exp:







polybius("2324  4423154215")