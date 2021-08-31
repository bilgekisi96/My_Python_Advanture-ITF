sozluk={}# her bir elemanına item deniyor

#  içerisindeki keyler str ve int olur

#  keyler ve valuelar hangi veri tiplerinde oluşturulabilir

first_dic={1:"bir","iki":2,False:[1,2,3,4]} # bu şekilde kabul ediyor

#  second_dict={[1,2,3,4]:"liste"} # key değeri collaction olarak liste almaz

third_dict={(1,2,3):"liste"} # tuple hash edilebiliyor
# key olarak dic kullanabilirmiyiz

#furth_dic={{1:"bir"}:"bir dic kabul etmiyor"}#  bir dic key olarak oluşmuyor ama  value bir dic olabilir

five_dic={"erkekler":{"ahmeet":35,"mehmet":44,"hasan":55},
          "bayanlar":{"selvi":20,"bahar":30,"ayşe":40}} #2 elemanı var

# indexleme keyler üzerinden yapılır

state_capitals={"arkansas":"littleRock",
                "Colorado":"Denver",
                "california":"Sacramento",
                "georgia":"Atlanta"}

print(state_capitals["Colorado"])

#atama yapılabilir yeni bir key ekleyebiliriz

state_capitals["Virginia"]="richmont"

print(state_capitals)

my_family = {"name1":"Ceaml","name2":"ayten",
             "name3":"yavuuz","name4":"hulya",
             "name5":"fatih","name6":"busra"}

my_family["name7"]="aleyna"
print(my_family)
print(len(my_family))

#  dic fonksiyonundaki değişkenler çalışınca stringe döner

sayilar = {"tek":[list(range(1,11,2))],"çift":[list(range(0,11,2))]}
sayilar1={"tek":[],"çift":[]}


sayilar1["tek"].append(1) #append metodu kullanılabilir
sayilar1["çift"].append(2)

print(sayilar.items())
print(sayilar.keys())
print(sayilar.values())

print(list(sayilar.items()))
print(list(sayilar.values()))


print(list(my_family.items()))
print(list(my_family.keys()))
print(list(my_family.values()))

my_family.update({"name10":"Kemal","guzel_aile":True})
print(my_family)

del my_family["name4"],my_family["name5"] # name 4 ü siler
print(my_family)

# in ifadesi dictionarylerde nasıl yapılır

# sadece keylere bakar in ifadesi yani keylerin arasında arar valueların arasında aramaz

# valueların arasındaki ifadeleri bulmak için my_family.values()

# yapmalıyız böylelikle iterable ifade haline getirmiş oluruz


# iç içe dictionarys nested dictionanryyyy

# valuelar üzerinden gidilir keyler üzerinden gidilmez

school_records={
	'personal_info':{

		 'kid':{'tom':{'class':'intermediate', 'age':10},
		        'sue':{'class':'elemantary', 'age':8}
		       },
		 'teen':{'joseph':{'class':'college', 'age':19},
			      'marry':{'class':'high school', 'age':16}
			    },
		              },
	'grades_info':{

         'kid':{'tom':{'math':88, 'speech':69},
		        'sue':{'math':90, 'speech':81}
			   },
		'teen':{'joseph':{'coding':80, 'math':89},
			    'marry':{'coding':70, 'math':96}
			   },
		              }
}

print(school_records["grades_info"]["teen"]["marry"])


print(list(school_records['personal_info']["teen"]["joseph"].values()))

# valuesları collage ve yas olur

para=1000

para=para*(1.07**7)  # bu döngü mantalitesini açıklar

print(para)

samanlik=["saman","seyran","iğne","inek"]

print(samanlik.index("iğne"))

print("hntelloprint".split("nt"))








