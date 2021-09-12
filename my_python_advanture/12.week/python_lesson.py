with open("fishes.txt","r") as file:
    fish=file.readlines()

fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open("my_file.txt","w") as f:
    for i in fruits:
        f.write(i+"\n")
with open("my_file.txt","r") as f:
    print(f.read())
fruitss = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open("my_file.txt","w") as ff:
    ff.writelines(fruitss)
with open("my_file.txt","r") as ff:
    print(ff.read())
import csv

with open("fruits.csv","r",newline="",encoding="utf-8") as scs:
    csv_rows=csv.reader(scs)
    for j in csv_rows:
        print(j)

import pandas as pd
df=pd.read_csv("titanic.csv")
print(df)
bayanlar=df[df["Sex"]=="female"]
print(bayanlar.to_csv("titanic_female.csv",index=False))

