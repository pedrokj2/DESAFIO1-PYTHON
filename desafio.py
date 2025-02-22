# Missão 1: Restaurando as Regras Escolares

def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


# Missão 2: O Sistema Eleitoral Secreto

def verificar_votaçao(idade):
    if idade >= 16:
        return "Pode votar"
    else:
        return "Não pode votar"


# Missão 3: Recuperando o Sistema de Notas

def Classificar_nota(nota):
    if 90 <= nota <= 100:
        return "Parabens, Você tirou A!"
    elif 80 <= nota <= 90:
        return "Muito bem, Você tirou B!"
    elif 70 <= nota <= 80:
        return "Bom trabalho, Você tirou C!"
    elif 60 <= nota <= 70:
        return "Fique atento, você tirou D!"
    elif 60 <= nota <= 50:
        return "Estudo um pouco mais, você tirou F!"


# Missão 4: Restaurando a Identificação de Números

def verificar_numeros(x, y):
    return x + y


# Missão 5: Recuperando o Cofre de Segurança

def verificar_senha(senha):
    senha_correta = "Python123"
    if senha == senha_correta:
        return "Acesso permitido"
    else:
        return "Acesso negado"


# Missão 6: Reforçando a Segurança e a Contagem do Sistema

def contar_numeros():
    i = 1
    while i <= 10:
        print(i)
        i += 1


# Missão 7: Organizando a Lista de números

def ordenar_lista():
    numeros = [8, 3, 10, 1, 5]
    return sorted(numeros)


# Missão 8: Acessando os Registros de Alunos

def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    return alunos[0], alunos[-1]


# Missão 9: Calculando Dobro de um Número

def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"


# Missão 10: Contando Letras

def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"
