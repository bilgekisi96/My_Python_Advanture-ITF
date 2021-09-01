

password="Hidden20"

user,passworduser=input("lutfen kullanıcı adını girin:"),input("sifre:")
while not password==passworduser:
    print(f"hello {user} see you later")
    passworduser=input("sifreyi tekrar gir dogru degil:")

print(f"Hello {user} ,The password is :{password}")
