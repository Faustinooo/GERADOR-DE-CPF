import random as r
def contacpf(a = ""):

    contador = 10
    saida = 0
    for i in a:
        troca = int(i)
        total = contador * troca
        saida += total
        contador -= 1
    conta = (saida * 10) % 11
    return conta
def contacpf2(a = ""):
    contador = 11
    saida = 0
    for i in a:
        troca = int(i)
        total = contador * troca
        saida += total
        contador -= 1
    conta = (saida * 10) % 11
    return conta

def gerador(a = 1):
    lista = []
    for i in range(1):
        c = ""
        for i in range(9):
            a = r.randint(0, 9)
            b = str(a)
            c += b
        e = contacpf(c)
        if int(e) > 9:
            e = 0
        d = c + str(e)
        g = contacpf2(d)
        if int(g) > 9:
            g = 0
        f = d + str(g)
        contador = 1
        for i in f:
            lista.append(i)
            if contador == 3 or contador == 6:
                lista.append(".")
            if contador == 9:
                lista.append("-")
            contador += 1
    fim = ""
    for i in lista:
        fim += i
    return fim
def linha(a = 0):
    print(f"\033[1;{a}m-=\033[m" * 20)
def cabeçalho(a = "TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")
def texto(a = "TEXTO"):
    linha(32)
    cabeçalho(a)
    linha(31)
texto("GERADOR DE CPF")
print()
print(gerador(1).center(40))
print()
linha()
