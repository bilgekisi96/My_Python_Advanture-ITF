import os

print(os.listdir())


file=open("rumi.txt","r",encoding="UTF-8")
print(file.readline())
print(file.readline())
file.close()