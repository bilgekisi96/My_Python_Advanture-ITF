alan=int(input("please enter area information"))
sayac=1
while (2**sayac)+1<=(alan*alan):
      sayac += 1
print(sayac-1)

number = int(input('Please enter a number: '))
sayac = 0
while sayac < number:
      print(sayac * sayac)
      sayac += 1

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
    print(type(i))