# kümeler için kullanılır 1,2,1,0,1.0 gibi içinde 2 eleman bulunu
# süslü parantez kullanarak küme yaparız
# set() ile yaparız iterable ifadeler kullanılmalıdır

colors="red","blue","pink","red"
set_1=set(colors)
print(set_1)

letter="a b c d e f g h j k l".split()
print(letter)
print(set(letter))

a_kume=set("phidelphia")
b_kume=set("dolphin")
print(a_kume.intersection(b_kume))
print(a_kume.union(b_kume))
print(a_kume.difference(b_kume))


