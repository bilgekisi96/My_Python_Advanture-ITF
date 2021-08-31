items=10,20
x,y=items

a,_,b,_=(10,20,30,40) #place holder izin veriyor

p,t,*k=(10,20,35,45,55,60,70)
print(k) #10 ve 20 bilgisini p ve t ye atar ve hemen ardından geri kalan veriyi liste şeklinde k ya atar

h,t,*c,j=(10,25,60,85,94,61,16,14) # h t j verileni en baştan ve sondan alır aradakileri c ye atar
print(c) # gibi gibi

liste=[10,20,30,45]



char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

user=input("please enter input").upper()
number,user1=len(user),list(user)
morselist=[char_to_dots[user1[num]] for num in range(number)]
print(*morselist)
























