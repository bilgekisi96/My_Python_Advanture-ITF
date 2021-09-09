
def avdlist(sepet):
    sepette=list(sorted(sepet))[::-1]
    dicc={i:[] for i in sepette}
    for j in sepet:dicc[j].append(j)
    return [dicc.values()]
print(avdlist([5,4,4,5,8,9]))



