lista = ["diego", "moicano"]
frutas = ["banana", "uva", "pera"]

lista.append("punkada")  # add elemento a lista  >> list.append(elmnt)
print(lista)

# clear()  Removes all the elements from the list  >> list.clear()

copia = lista.copy()  # copia a lista  >> list.copy()
print(copia)

conta = lista.count("diego")  # conta elementos da lista  >> list.count(value)
print(conta)

extende = lista.extend(frutas)  # add lista ou valores no final  >> list.extend(iterable)
print(lista)

pos = lista.index("punkada")  # mostra a posição  >> list.index(elmnt)
print(pos)

frutas.insert(1, "melancia")  # add elemento  >> list.insert(pos, elmnt)
print(frutas)

frutas.pop()  # remove último elemento ou na posição  >> list.pop(pos)
print(frutas)

frutas.remove("uva")  # remove um elemento especificado >> list.remove(elmnt)
print(frutas)

lista.reverse()  # inverte a ordem da lista  >> list.reverse()
print(lista)

lista.sort()  # ordena a lista  >> list.sort(reverse=True|False, key=myFunc)
print(lista)
