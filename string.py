

print("test is {:<10} end should be perfect".format("text")) # sağa ve sola yaslama metodları

print("test is {:^10} end should be perfect".format("text")) # ortalama stringlerde

print("{:10.5}".format("Perceptron")) # ilk 5 karakterini alıyor

word="happy"
print(list(word)) #arasındaki fark list fonksşiyonunun içine yazması
liste2=list(word)
liste1=[word] #sadece 1 elemanı mevcut

print(liste1)

print(list(liste2))


listem=["josef","jacob","hassan",["adem","havva"]]
listem1=("josef","jacob","hassan",["adem","havva"])

listem1[3].insert(0,"yavuz")
listem1[3].remove(listem1[3][1])
print(listem1)







