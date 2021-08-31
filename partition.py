

dicc={}
liste = [1, 'a', 2, 'b', 1, 'c', 2, 1, 'a', 'c', 2, 1, 2, 2, 1, 'a', 'b', 'a', 'b', 1, 2, 'c', 'c']
for char in liste:dicc[char]=[]
dickeys=[chardic for chardic in dicc.keys()]
sayac=0
while sayac<len(liste):
       if liste[sayac] in dickeys:
           dicc[liste[sayac]].append(liste[sayac])
       sayac +=1
print(dicc.values())


liste = [1, 'a', 2, 'b', 1, 'c', 2, 1, 'a', 'c', 2, 1, 2, 2, 1, 'a', 'b', 'a', 'b', 1, 2, 'c', 'c']
listim, setim = [] , set()
for i in liste:
    if i not in setim:
        listim.append(list(str(i))*liste.count(i))
        setim.add(i)
print(listim)
