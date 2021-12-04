votos = []
op = 0

print("""
Qual o melhor Sistema Operacional para uso em servidores?
    
As possíveis respostas são:
    
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
7- Sair
        """)

while op != 7:
    op = int(input("Digite a sua escolha: "))
    if op == 1:
        votos.append("Windows Server")
    elif op == 2:
        votos.append("Unix")
    elif op == 3:
        votos.append("Linux")
    elif op == 4:
        votos.append("Netware")
    elif op == 5:
        votos.append("Mac OS")
    elif op == 6:
        votos.append("Outro")


print(votos)

ws = votos.count("Windows Server")
un = votos.count("Unix")
lx = votos.count("Linux")
nt = votos.count("Netware")
mo = votos.count("Mac OS")
ot = votos.count("Outro")

pws = ws / 100
pun = un / 100
plx = lx / 100
pnt = nt / 100
pmo = mo / 100
pot = ot / 100
soma = ws + un + lx + nt + mo + ot

print(f"""
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           {ws}     {pws}%
Unix                     {un}     {pun}%
Linux                    {lx}     {plx}%
Netware                  {nt}     {pnt}%
Mac OS                   {mo}     {pmo}%
Outro                    {ot}     {pot}%
-------------------     -----
Total                    {soma}

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
""")
