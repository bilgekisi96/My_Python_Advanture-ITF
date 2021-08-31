


cumle="ben bire ODunüm"

def woveler(wowel):
    vevels=["a","e","ı","i","o","ö","u","ü"]
    if wowel.lower() in vevels:
        return True
    else:
        return False
print(list(filter(woveler,cumle)))

def gene(x,y):
    print(x)
    print(y)

dictcc={"x":"david","y":"solomon"}
print(gene(**dictcc))



dicc_couple={"bride":["mary","bella","linda","emma"],
             "groom":["jack","robert","eric","adam"]}

def muruvvet():
  listem = [i for i in dicc_couple.values()]
  return list(zip(listem[0], listem[1]))

print(muruvvet())




dicc_friend={"alfred":44,"thomas":50,"emily":20}
def meaner(**dicc_friend):
    toplam = 0
    for x in dicc_friend.values():
        toplam += x
    print("avarege",toplam/3)
meaner(**dicc_friend)






