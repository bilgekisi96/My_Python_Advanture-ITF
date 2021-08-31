import googletrans
from googletrans import Translator
translator = Translator()
translation = translator.translate("Data science is best",dest="tr")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

x=["1","2","3"]
y=["USA","JAPAN","SPAİN"]

result=[i+j for i in y for j in x]
print(result)