user="2002077"
user_str = ""
user_list, first_list = [],[]
sayac=1
while sayac != len(user):
    first_num = user[:sayac]
    kalan_num = user[sayac:].lstrip("0")
    first_list.append(first_num)
    user_list.append(kalan_num)
    sayac += 1
if user_list[len(user_list)-1] == "": user_list[len(user_list)-1] = "0"
first_list = [int(i) for i in first_list]
user_list = [int(j) for j in user_list]
zipo = zip(first_list,user_list)
zipo = [tuple(sorted(tiro)) for tiro in zipo]
toplam, toplist = 0, []
for a, b in zipo:
    for tito in range(a, b+1):
        toplam += tito
    toplist.append(toplam)
print(toplist)
if int(user) in toplist: print("yeah it is astonishing")
else: print("Thats not astonishing")
