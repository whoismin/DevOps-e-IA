# ============================
# DADOS
# ============================

quantidade_cidades = int(input("Quantas cidades deseja analisar? "))

cidades = []
medias = []

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]


for i in range(quantidade_cidades):

    cidade = input(f"\nDigite o nome da cidade {i+1}: ")
    temperaturas = []

    print(f"\nDigite as temperaturas médias mensais de {cidade}:")

    for mes in meses:
        temp = float(input(f"{mes}: "))
        temperaturas.append(temp)

    # ============================
    # INFORMAÇÃO
    # ============================

    media = sum(temperaturas) / len(temperaturas)

    cidades.append(cidade)
    medias.append(media)


# ============================
# CONHECIMENTO
# ============================

def classificar_clima(media):

    if media <= 10:
        return "Muito frio"
    elif media <= 18:
        return "Frio"
    elif media <= 25:
        return "Ameno"
    else:
        return "Quente"


# ============================
# DECISÃO
# ============================

def sugestao_roupa(media):

    if media <= 10:
        return "Casaco pesado, luvas e cachecol"
    elif media <= 18:
        return "Casaco ou moletom"
    elif media <= 25:
        return "Camiseta e calça leve"
    else:
        return "Roupas leves (shorts e camiseta)"


# ============================
# RELATÓRIO
# ============================

print("\n========== RELATÓRIO CLIMÁTICO ==========")

for i in range(quantidade_cidades):

    cidade = cidades[i]
    media = medias[i]

    clima = classificar_clima(media)
    roupa = sugestao_roupa(media)

    print(f"\nCidade: {cidade}")
    print(f"Média anual de temperatura: {media:.2f} °C")
    print(f"Classificação do clima: {clima}")
    print(f"Sugestão de roupa: {roupa}")

print("\n=========================================")