import random

lista_a = []
lista_b = []
lista_c = []
operacao = None
ordem = []
opcoes = ["ab", "ac", "ba", "bc", "ca", "cb"]

n = 7
contador = n

lista = []
while contador > 0:
    lista.append(contador)
    lista_a.append(contador)
    contador -= 1
print("lista",lista)

def operacoes(opt):
    opt.lower()
    if opt == "ab":
        lista_b.append(lista_a[-1])
        lista_a.pop()
    elif opt == "ac":
        lista_c.append(lista_a[-1])
        lista_a.pop()
    elif opt == "ba":
        lista_a.append(lista_b[-1])
        lista_b.pop()
    elif opt == "bc":
        lista_c.append(lista_b[-1])
        lista_b.pop()
    elif opt == "ca":
        lista_a.append(lista_c[-1])
        lista_c.pop()
    elif opt == "cb":
        lista_b.append(lista_c[-1])
        lista_c.pop()


def verificar_lista(opt):
    try:
        operacoes(opt)
    except IndexError:
        pass
    item = eval(f"lista_{opt[1]}")
    if len(item) > 1:
        if item[-1] > item[-2]:
            operacoes(opt[1] + opt[0])



while lista_c != lista:
    escolha = random.choice(opcoes)
    try:
        for x in range(n):
            if lista_c[x] == (n - x)  and len(lista_c) < (x + 2):
                while escolha == "ca" or escolha == "cb":
                    escolha = random.choice(opcoes)
    except IndexError:
        pass

    print(lista_a, lista_b, lista_c)

    verificar_lista(escolha)

    ordem.append(escolha)

print("Fim do programa", lista_c)
lista_a = lista
lista_b = []
lista_c = []
print("reset listas", lista_a, lista_b, lista_c)
for opt in ordem:
    verificar_lista(opt)
print("Quantidades de operacoes realizadas:",len(ordem))

print("Validacao do resultado: lista c =>", lista_c)
print("resultado todas listas",lista_a, lista_b, lista_c)
