car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "blue",
  "moto": "female"
}
x = ('key1', 'key2', 'key3')
y = 0

# clear() Removes all the elements from the dictionary  >> dict.clear()

cp = car.copy()  # faz uma cópia do dicionário  >> dict.copy()
print(cp)

new_dic = dict.fromkeys(x, y)  # retorna um dict a partir de uma chave/valor >> dict.fromkeys(keys, value)
print(new_dic)

pega = car.get("year")  # retorna o valor de uma chave especifica  >> dict.get(keyname, value)
print(pega)

it_ens = car.items()  # retorna lista dos itens (chave/valor) como tupla  >> dict.items()
print(it_ens)

cha_ves = car.keys()  # retorna lista das chaves  >> dict.keys()
print(cha_ves)

car.pop("year")  # remove o valor de uma chave  >> dict.pop(keyname, defaultvalue)
print(car)
v = car.pop("model")
print(v)
print(car)

car.popitem()  # remove um item de forma randomica  >> dict.popitem()
print(car)

padrao = car.setdefault("brand")  # retorna o valor de uma chave especifica  >> dict.setdefault(keyname, value)
print(padrao)

car.update({"road": "street"})  # atualiza o dicionário  >> dictionary.update(iterable)
print(car)

obj = car.values()  # retorna uma lista de valores  >> dict.values()
print(obj)
