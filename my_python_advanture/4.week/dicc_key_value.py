
soz={"pl":"elma","ps":"Armut","pm":"Kayısı","p":"seftali"}
def dicchange(**ktwo):
    dicc={k:t for t,k in ktwo.items()}# bu ifade ile key ve value degerlerini degiştirebilirsin
    return dicc

print(dicchange(**soz))





def gene(x, y):  # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")

dict_gene = {'y': "Marry", 'x': "Fred"}
gene(**dict_gene)  # we call the function by a single argument(variable)