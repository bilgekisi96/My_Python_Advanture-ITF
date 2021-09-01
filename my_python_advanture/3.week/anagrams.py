



farm = ["eat", "tea", "tan", "ate", "nat", "bat","cat","tac"]

setstring=[list(sorted(ptr)) for ptr in farm]
addstring=["".join(atr) for atr in setstring]
dicc={}
for hep in addstring: dicc[hep]=[]
[dicc["".join(sorted(her))].append(her) for her in farm if "".join(sorted(her)) in dicc]
print(dicc)











