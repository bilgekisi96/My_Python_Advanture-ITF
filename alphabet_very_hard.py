def revalph(text):
    alphabet=list("abcdefghijklmnopqrstuvwxyz")
    alphabet_big=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    rev_alphabet=alphabet[::-1]
    rev_big_alp=alphabet_big[::-1]
    dicc=dict(zip(alphabet+alphabet_big+list("123456789"),rev_alphabet+rev_big_alp+list("123456789")))
    for i in text:
           if i==" ":
               dicc[i]=" "
           print(dicc[i], end="")
    return
revalph("Sdkvmlsv45")












