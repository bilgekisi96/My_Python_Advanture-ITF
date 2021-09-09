import string
list_alp=list(string.ascii_lowercase)+[" ","!","."]
list_olp=list(string.ascii_lowercase[13:])+list(string.ascii_lowercase[:13])+[" ","!","."]
first_rot={i:j for i,j in zip(list_alp,list_olp)}
def rot_13(string):
    org,exploit=string,""
    for i in range(len(org)):
        if org[i].isupper():exploit+=first_rot[org[i].lower()].upper()
        else:exploit+=first_rot[org[i]]
    return exploit
print(rot_13("This is an encrypted message!"))





