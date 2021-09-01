

import random,math
gir_list = [1, 2,3]
pumpt=[1,2,3]
fin_list=[]
sayac = math.factorial(len(gir_list))
def question(til,pumpt):
    while til>len(fin_list):
        gir_list = [1, 2, 3]
        random.shuffle(gir_list)
        if gir_list not in fin_list:
            fin_list.append(gir_list)
        else:random.shuffle(gir_list)
    return fin_list
print(question(sayac,pumpt))

