import urllib.request
import os


def download_arquivo(url):
    urllib.request.urlretrieve(url, "./arquivo.csv")
    arquivo = open('./arquivo.csv')
    os.remove("./arquivo.csv")
    return arquivo


def busca_dados():
    arquivo = download_arquivo("https://drive.usercontent.google.com/download?id=15IimaHTCUsH8NtG-rgtLMBF2Pt9N5WsD&export=download&authuser=0")
    lines = arquivo.readlines()
    array_ids = []
    dados = {}

    for line in (line.replace("\n", "").split(",") for line in lines):
        if not dados:
            for id in line:
                array_ids.append(id)
                dados[id] = []
        else:
            for index in range(len(dados)):
                dados[array_ids[index]].append(line[index])
    return dados


def media(lista):
    soma = 0
    for item in lista:
        soma += float(item)
    media = soma / len(lista)
    return media


def percentual_por_repeticao(lista):
    possibilidade = {}
    total_repeticoes = 0
    for item in lista:
        if item not in possibilidade:
            possibilidade[item] = 1
            total_repeticoes += 1
        else:
            possibilidade[item] += 1
            total_repeticoes += 1
    for key, value in possibilidade.items():
        possibilidade[key] = f"{value / total_repeticoes * 100}%"
    
    return possibilidade


def filtro_com_base(valor_para_filtrar, lista1, lista2):
    lista_final = []
    for index in range(len(lista1)):
        if valor_para_filtrar == lista1[index]:
            lista_final.append(lista2[index])
    return lista_final


def maior(lista):
    numero = None
    for item in lista:
        item = float(item)
        if numero == None:
            numero = item
        elif numero < item:
            numero = item
    return numero


def menor(lista):
    numero = None
    for item in lista:
        item = float(item)
        if numero == None:
            numero = item
        elif numero > item:
            numero = item
    return numero


def desvio_padrao(lista):
    med = media(lista)

    somatorio = 0

    for item in lista:
        item = float(item)
        somatorio += (item - med) ** 2
    pre_result = somatorio / len(lista)
    result = pre_result ** (1 / 2)
    return result


def apresenta_resultados():
    dados = busca_dados()
    if dados:
        print("---Percentual:---")
        porcentagens = percentual_por_repeticao(dados["Sexo"])
        for key, value in porcentagens.items():
            print(f"    {key}: {value}")

        print("\n---Médias:---")
        print("\nPeso:")
        peso_m = filtro_com_base("M", dados["Sexo"], dados["Peso"])
        peso_f = filtro_com_base("F", dados["Sexo"], dados["Peso"])
        print(f"    Macho: {media(peso_m):.2f}")
        print(f"    Fêmea: {media(peso_f):.2f}")

        print("\nIdade:")
        idade_m = filtro_com_base("M", dados["Sexo"], dados["Idade"])
        idade_f = filtro_com_base("F", dados["Sexo"], dados["Idade"])
        print(f"    Macho: {media(idade_m):.2f}")
        print(f"    Fêmea: {media(idade_f):.2f}")

        print("\n---Desvio-Padrão:---")
        print("\nPeso:")
        print(f"    Macho: {desvio_padrao(peso_m):.2f}")
        print(f"    Fêmea: {desvio_padrao(peso_f):.2f}")
        print(f"    Todos: {desvio_padrao(dados['Peso']):.2f}")

        print("\nIdade:")
        print(f"    Macho: {desvio_padrao(idade_m):.2f}")
        print(f"    Fêmea: {desvio_padrao(idade_f):.2f}")
        print(f"    Todos: {desvio_padrao(dados['Idade']):.2f}")

        print("\n---Valores-Máximos-e-Mínimos:---")
        print("\nPeso:")
        print("----Máximo")
        print(f"    Macho: {maior(peso_m):.2f}")
        print(f"    Fêmea: {maior(peso_f):.2f}")
        print("----Mínimo")
        print(f"    Macho: {menor(peso_m):.2f}")
        print(f"    Fêmea: {menor(peso_f):.2f}")

        print("\nIdade:")
        print("----Máximo")
        print(f"    Macho: {maior(idade_m):.2f}")
        print(f"    Fêmea: {maior(idade_f):.2f}")
        print("----Mínimo")
        print(f"    Macho: {menor(idade_m):.2f}")
        print(f"    Fêmea: {menor(idade_f):.2f}")
    else:
        print("Não foi possível obter os dados.")


# Exemplo de chamada da função
apresenta_resultados()
