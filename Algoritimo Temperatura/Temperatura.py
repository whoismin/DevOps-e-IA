
# DADOS DO USUÁRIO


# Solicita o nome do usuário que irá utilizar o sistema
nome = input("Digite seu nome: ")

# Usuário escolhe o gênero para personalizar as sugestões de roupa
print("\nSelecione seu gênero:")
print("1 - Feminino")
print("2 - Masculino")

genero_opcao = int(input("Opção: "))

# Converte a opção escolhida em texto
if genero_opcao == 1:
    genero = "feminino"
else:
    genero = "masculino"



# ESCOLHA DO TIPO DE CÁLCULO


# Usuário escolhe se deseja analisar o clima anual ou apenas de um dia
print("\nComo deseja calcular a temperatura?")
print("1 - Média anual da cidade")
print("2 - Média do dia")

opcao = int(input("Opção: "))



# FUNÇÃO DE CLASSIFICAÇÃO DO CLIMA


# Esta função recebe a temperatura média e classifica o clima
def classificar_clima(media):

    if media <= 10:
        return "Muito frio"
    elif media <= 18:
        return "Frio"
    elif media <= 25:
        return "Ameno"
    else:
        return "Quente"



# FUNÇÃO DE SUGESTÃO DE ROUPAS


# Esta função utiliza a temperatura média e o gênero
# para recomendar roupas adequadas ao clima
def sugestao_roupa(media, genero):

    if genero == "feminino":

        if media <= 10:
            return "Casaco pesado, bota e cachecol"
        elif media <= 18:
            return "Casaco ou moletom e calça"
        elif media <= 25:
            return "Blusa leve e calça ou saia"
        else:
            return "Vestido leve ou shorts e camiseta"

    else:  # masculino

        if media <= 10:
            return "Casaco pesado, calça e cachecol"
        elif media <= 18:
            return "Moletom ou jaqueta"
        elif media <= 25:
            return "Camiseta e calça leve"
        else:
            return "Shorts e camiseta"



# PROCESSAMENTO - MÉDIA ANUAL


if opcao == 1:

    # Pergunta quantas cidades serão analisadas
    quantidade_cidades = int(input("\nQuantas cidades deseja analisar? "))

    cidades = []
    medias = []

    # Lista com os meses do ano
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # Loop para cadastrar as cidades
    for i in range(quantidade_cidades):

        cidade = input(f"\nDigite o nome da cidade {i+1}: ")
        temperaturas = []

        print(f"\nDigite as temperaturas médias mensais de {cidade}:")

        # Loop que percorre todos os meses e coleta as temperaturas
        for mes in meses:
            temp = float(input(f"{mes}: "))
            temperaturas.append(temp)

        # Calcula a média anual da cidade
        media = sum(temperaturas) / len(temperaturas)

        # Guarda os dados em listas
        cidades.append(cidade)
        medias.append(media)


   
    # RELATÓRIO FINAL

    print("\n========== RELATÓRIO CLIMÁTICO ==========")
    print(f"Usuário: {nome}")

    # Loop para exibir o relatório de cada cidade
    for i in range(quantidade_cidades):

        cidade = cidades[i]
        media = medias[i]

        # Chama as funções de classificação e sugestão
        clima = classificar_clima(media)
        roupa = sugestao_roupa(media, genero)

        print(f"\nCidade: {cidade}")
        print(f"Média anual de temperatura: {media:.2f} °C")
        print(f"Classificação do clima: {clima}")
        print(f"Sugestão de roupa: {roupa}")

    print("\n=========================================")


# PROCESSAMENTO - MÉDIA DO DIA

elif opcao == 2:

    print("\nDigite os dados da temperatura do dia")

    # Usuário informa a temperatura máxima e mínima
    temp_max = float(input("Temperatura máxima: "))
    temp_min = float(input("Temperatura mínima: "))

    # Cálculo da média do dia
    media = (temp_max + temp_min) / 2

    # Classificação do clima e sugestão de roupa
    clima = classificar_clima(media)
    roupa = sugestao_roupa(media, genero)

    # Relatório final
    print("\n========== RELATÓRIO DO DIA ==========")
    print(f"Usuário: {nome}")
    print(f"Temperatura média do dia: {media:.2f} °C")
    print(f"Classificação do clima: {clima}")
    print(f"Sugestão de roupa: {roupa}")
    print("======================================")