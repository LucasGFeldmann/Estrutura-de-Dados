# Atividades

1. Criar um set

```py
def ex01():
    sets = {0,1,2,3,4,5,6,7,8,9}
    arr = [0,1,2,3,4,5,6,7,8,9]


    print(sets, arr)

    sets.pop()
    arr.pop()

    sets.pop()
    arr.pop()

    try:
        sets.pop(0)
        arr.pop(0)
    except:
        print("erro pop")

    print(sets, arr)

```

2. Criar uma list


3. Testar as caracteristicas e diferenças com código


4. Criar um Dict


5. Montar um cadastro básico de pessoas: Nome, Idade e Altura

```py
def insert(dados={}):
    email = input("Digite uma sequencia de letras: ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite a sua altura: "))
    dados[email] = {
        "nome": nome,
        "idade": idade,
        "altura": altura
    }

    return dados

def delete(dados, key):
    old = dados[key]
    del dados[key]
    return old

def search(dados, name):
    for account in dados:
        print(account)
        #if account["nome"] == name:
        #    return account
        
def main():
    db = {}
    close = False
    while close != True:
        print()
        print(db)
        print()
        print("insert, delete, search, close")
        opt = input("Digite o que voce quer: ")
        match opt:
            case "insert":
                insert(db)
            case "delete":
                delete(db, input("Digite email para deletar: "))
            case "search":
                search(db, input("Digite o nome que deseja buscar: "))
            case "close":
                close = True
    
#main()
```

6. Hash

```py
def verify(x):
    x = ord(x)
    if x > 96:
        return x -96
    else:
        return x -64

def hash(valor):
    lista = ""
    for index in range(0,len(valor),2):
        try:
            lista += f"{verify(valor[index]) + verify(valor[index+1])}"
        except:
            lista += f"{verify(valor[index])}"
    print(lista)

ls = ['casa','casarao','casacosta','casamento','casa gramada','casamento bonito','uzbequistao']

for x in ls:
    hash(x)
```

7. JSON


8. REST


9.  Fazer uma consulta a uma API REST com uma estrutura JSON.

