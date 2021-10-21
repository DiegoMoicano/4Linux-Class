nasc = int(input("Digite o ano do seus nascimento: "))

if nasc <= 1964:
    print("Baby Boomer")
elif 1979 <= nasc >= 1965:
    print("Geração X")
elif 1994 <= nasc >= 1980:
    print("Geração Y")
elif 