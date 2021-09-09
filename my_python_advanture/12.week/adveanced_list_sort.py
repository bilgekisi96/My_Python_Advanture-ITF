
def avdlist(sepet):
    dicc={i:[] for i in sepet}
    for j in sepet:dicc[j].append(j)
    return [dicc.values()]
print(avdlist(["b", "a", "b", "a", "c"]))



