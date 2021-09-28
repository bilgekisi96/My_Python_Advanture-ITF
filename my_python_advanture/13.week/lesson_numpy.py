import numpy as np

liste=[1,2,3,4,5]
listek=[6,7,8,9,10]
my_list=np.array(liste)
my_listek=np.array(listek)
print(my_list+my_listek)
print(liste+listek)
print(my_list.shape,my_list.size,my_list.ndim)


print(np.ones((3,2),dtype=int)*5)
print(np.full((2,2),10))

shape=np.arange(12)

print(shape.reshape(3,4))
print(shape.max())
print(shape.argmax())


print(np.arange(1,37).shape)


a=np.arange(5)
b=np.array([0,1])
print(np.repeat(b,3))
c=np.array([0,1])
print(b+c)

one=np.ones((1,32),dtype=int)
zero=np.zeros((1,32),dtype=int)
array=np.array([zero,one])
print(np.reshape(array,64,order="F").reshape(8,8))


print()
def checkerboard(n):
    return np.indices(n).sum(axis = 0) % 2
print(checkerboard((8,8)))




asci=np.array(['clarusway','data','science','bootcamp','is','the','best'],dtype=str)
print(np.char.lower(asci),np.char.upper(asci),np.char.swapcase(asci),np.char.title(asci),np.char.capitalize(asci),sep="\n")


python=np.array([['Python','NumPy','Exercises'],
                 ['Python','Pandas','Exercises'],
                 ['Python','Machine learning','Python']])

print(np.char.count(python,"Python"))


import seaborn as sns

sns.get_dataset_names()
df=sns.load_dataset("mpg")
print(df.head())#ilk 5 veri
print(df.shape,df.columns)
print(df.select_dtypes(include=["object"]))
print(df.nunique(axis=0))
#print(df.plot.pie(y=[135,120,23]))
print(df.describe())


####PARAMETERS AND STATİSTİCS


population = np.random.randint(0,100, size=10000)
#np.random.seed(51)#aynı sayıları elde etmek için
sample=np.random.choice(population,100)
#print(sample)
print(population.mean(),sample.mean())


sample_means=[]
for i in range(100):
    samples = np.random.choice(population, 100)
    sample_means.append(samples.mean())
print(np.mean(sample_means))















