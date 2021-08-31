

num=int(input("Lutfen sisteme sayi giriniz:"))
numbers=[sayi for sayi in range(1,num) if num%sayi==0]
if sum(numbers)==num:
    print(f"Aslansın mükemmel sayıyı buldun:{num}")
else:
    print("Malesef bu bir mükemmel sayi değil :(")

