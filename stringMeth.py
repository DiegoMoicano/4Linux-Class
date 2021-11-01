string1 = "diego moicano pires de azevedo gonçalves"
string2 = "MOIcano34"
string3 = "H\te\tl\tl\to"
string4 = "O binário de {0} é {0:b}"
string5 = "--------MOIcano34------- "
string6 = "diego moicano pires\n de azevedo gonçalves"
string7 = "       MOIcano34     "
string8 = "Hello My Name Is MOICANO"

print(string1.capitalize())   # primeiro caracter em maíusculo
print(string1.casefold())     # tudo minúsculo, mais agressivo que o lower()
print(string2.center(20))     # centraliza usando espaços >> string.center(length, character)
print(string1.count("a"))     # conta os caracteres/plavras >> count(value, start, end)
print(string2.encode())  # codifica strings >> string.encode(encoding=encoding, errors=errors)
print(string1.endswith("s"))    # verifica o fim >> string.endswith(value, start, end)
print(string1.endswith("z"))    # verifica o fim
print(string3.expandtabs(2))   # espaçamento entre tabs  >> string.expandtabs(tabsize)
print(string1.find("j"))     # procura e retorna a primeira posição e -1 não achou >> string.find(value, start, end)
print(string4.format(5))   # formata -- possui vários formatos >> string.format(value1, value2...)
print(string1.index("e"))  # procura e retorna a primeira posição mas não -1 >> string.index(value, start, end)
print(string2.isalnum())  # retorna True se a string for alphanum  >> string.isalnum()
print(string2.isalpha())  # retorna True se a string só chars  >> string.isalpha()
print(string2.isascii())  # retorna True se a string ASCII  >> string.isascii()


# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case

print("-".join(string1))  # converte os elementos de um iterável em uma string >> string.join(iterable)
print(string2.ljust(15, "-"), "punkada")  # alinhar a esquerda >> string.ljust(length, character)
print(string2.lower())  # tudo minúsculo >> string.lower()
print(string5.lstrip("-"))  # remove caracteres à esquerda >> string.lstrip(characters)

# maketrans() Returns a translation table to be used in translations  >> string.maketrans(x, y, z)

print(string1.partition("pires"))  # converte tuplas antes e depois >> string.partition(value)
print(string1.replace("moicano", "punkada"))  # substitiu 1 pelo 2 >> string.replace(oldvalue, newvalue, count)

# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string

print(string1.split())  # converte strings em lista >> string.split(separator, maxsplit)
print(string6.splitlines())  # converte em lista onde encontra \n >> string.splitlines(keeplinebreaks)
print(string1.startswith("diego"))  # True se encontrar a string no início >> string.startswith(value, start, end)
print(string7.strip())  # remove espaços trás e frente  >> string.strip(characters)
print(string8.swapcase())  # inverte os casos string  >> string.swapcase()
print(string1.title())  # coloca a primeira letra em maiúscula >> string.title()

# translate()	Returns a translated string  >> string.translate(table)

print(string1.upper())  # converte tudo em maiúsculo >> string.upper()
print(string2.zfill(20))  # add zeros 0 no início >> string.zfill(len)

# Nota: Todos os métodos de string retornam novos valores. Eles não mudam a string original.
