
def morfic(a,b):
    first_list=[a.count(a[i]) for i in range(len(a)) if a[i] in a]
    second_list = [b.count(b[j]) for j in range(len(b)) if b[j] in b]
    if first_list==second_list:return True
    else: return False
print(morfic("keste", "yeste"))


def is_isomorphic(s, t):
    s_dicct,t_dicct ={},{}
    if len(s) != len(t):
        return False
    for i in range(len(t)):
        si, ti = s[i], t[i]
        if si not in s_dicct:
            s_dicct[si] = ti
        if ti not in t_dicct:
            t_dicct[ti] = si
        if t_dicct[ti] !=  si or s_dicct[si] != ti:
            return False
    return True




