


commands=["right 10","right 30","left 40","up 20","down 30"]
dicc = {"right": [], "left": [],"up":[],"down":[]}
for i in commands:
    k=i.split()[0]
    c=int(i.split()[1])
    dicc[k].append(c)
x_coor,y_coor=sum(dicc["right"])-sum(dicc["left"]),sum(dicc["up"])-sum(dicc["down"])
print(x_coor,y_coor)
