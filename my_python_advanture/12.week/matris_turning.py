




#rotated = list(reversed(list(zip(*original))))# saat yönü tersi
#print(rotated)
#rtor=list(zip(*matris[::-1]))#saat yönünde
#print(rtor)

def mat_rot(matris,rotate):
    if rotate<0:
        rotate=abs(rotate)
        for i in range(rotate):
            rotated = list(reversed(list(zip(*matris))))
            matris=rotated
        return matris
    elif rotate>0:
        for j in range(rotate):
            rtor = list(zip(*matris[::-1]))
            matris=rtor
        return matris
    else:
        return matris

print(mat_rot([
  [1,  2,  3,  4],
  [5,  6,  7,  8],
  [9, 10, 11, 12]
],-4))


def right_rotation(liste, n = 1):
    donusum = {-1 : 3, -2 : 2, -3 : 1, -4 : 4}
    if n < 0:n = donusum[n]
    a = 0
    while a < n:
        liste = list(map(lambda *x : [*x[::-1]], *liste))
        a += 1
    return liste

print(right_rotation([
  [1,  2,  3,  4],
  [5,  6,  7,  8],
  [9, 10, 11, 12]
], -1))



