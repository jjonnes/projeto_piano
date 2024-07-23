# Função para retornar o nome completo de uma nota musical
def nome(nota):
    # Dicionário que mapeia notas para seus nomes completos
    notas = {
        "A": "Lá",
        "A#": "Lá Sustenido",
        "B": "Si",
        "C": "Dó",
        "C#": "Dó Sustenido",
        "D": "Ré",
        "D#": "Ré Sustenido",
        "E": "Mi",
        "F": "Fá",
        "F#": "Fá Sustenido",
        "G": "Sol",
        "G#": "Sol Sustenido"
    }
    # Retorna o nome da nota correspondente, ou "Nota não reconhecida" se não existir
    return notas.get(nota.upper(), "Nota não reconhecida")

# Função para gerar uma lista de notas musicais e seus equivalentes com sustenido
def campo_notas():
    notas = []

    # Loop para adicionar as notas de A a G e seus equivalentes com sustenido ao final
    for i in range(97, 104):  # 97 é o código ASCII para 'a' e 104 para 'h'
        notas.append(chr(i).upper())  # Adiciona a nota maiúscula
        # Adiciona a nota com sustenido, exceto para 'B' e 'E' que não têm sustenido
        if i != 98 and i != 101:
            notas.append(chr(i).upper() + '#')
    
    return notas

# Função para gerar o campo harmônico a partir de uma nota inicial
def campo_harmonico(nota):
    campo = []
    notas = campo_notas()
    start_index = notas.index(nota.upper())  # Encontra o índice da nota inicial na lista

    # Loop para gerar o campo harmônico com 12 notas
    for i in range(12):
        index = (start_index + i) % len(notas)  # Calcula o índice da nota no campo
        campo.append(notas[index])  # Adiciona a nota ao campo harmônico
    
    return campo

# Função para imprimir uma tabela de acordes com base nos graus musicais especificados
def imprimir_tabela_acordes(graus_indices, nota=None):
    notas = campo_notas()
    # Lista dos graus musicais que serão impressos na tabela
    graus = ["T     ", "2ªb   ", "2ª#   ", "3ªb   ",
             "3ª#   ", "4ªj   ", "4ª^   ", "5ªj   ",
             "6ªb   ", "6ª#   ", "7ªb   ", "7ª#   "]

    # Calcula o comprimento máximo de cada coluna na tabela
    max_length = [len(grau) for grau in graus]

    # Atualiza o comprimento máximo de cada coluna baseado nos graus que serão impressos
    for i in graus_indices:
        max_length[i] = max(len(graus[i]), max_length[i])

    # Imprime a primeira linha com os graus musicais formatados
    header = "|"
    for i in graus_indices:
        header += f" {graus[i]}{' ' * (max_length[i] - len(graus[i]) + 1)} |"
    
    # Determina quais índices de notas serão impressos na tabela
    if nota is None:
        notas_indices = range(12)  # Imprime todas as notas se nenhuma nota específica for fornecida
    else:
        if nota.upper() in notas:
            notas_indices = [notas.index(nota.upper())]  # Encontra o índice da nota específica

    # Lista para armazenar as linhas da tabela
    linhas = []

    # Imprime os acordes para cada linha de notas na tabela
    for j in notas_indices:
        linha = "|"
        for i in graus_indices:
            campo = campo_harmonico(notas[j])  # Obtém o campo harmônico para a nota atual
            linha += f" {campo[i]}{' ' * (max_length[i] - len(campo[i]) + 1)} |"
        linhas.append(f"{linha} \n")

    # Retorna as linhas como uma lista de strings
    return linhas, header

# Função para imprimir a tabela completa de acordes harmônicos
def campo_har_completo():
    graus_indices = list(range(12))  # Índices das colunas 1, 5 e 8 (todos os graus)
    linhas, header = imprimir_tabela_acordes(graus_indices)
    txt = f"Campo harmônico completo \n \n {header} \n" + "".join(linhas)
    return txt

# Função para imprimir a tabela de acordes maiores
def acordes_maiores():
    graus_indices = [0, 4, 7]  # Índices das colunas 1, 5 e 8 para acordes maiores
    linhas, header = imprimir_tabela_acordes(graus_indices)
    txt = f"Acordes maiores \n \n {header} \n" + "".join(linhas)
    return txt

# Função para imprimir a tabela de acordes menores
def acordes_menores():
    graus_indices = [0, 3, 7]  # Índices das colunas 1, 4 e 8 para acordes menores
    linhas, header = imprimir_tabela_acordes(graus_indices)
    txt = f"Acordes menores \n \n {header} \n" + "".join(linhas)
    return txt

# Função para imprimir a tabela de acorde maior para uma nota específica
def acorde_maior(nota):
    graus_indices = [0, 4, 7]  # Índices das colunas 1, 5 e 8 para acorde maior
    linhas, header = imprimir_tabela_acordes(graus_indices, nota)
    txt = f"{nota.upper()} - ({nome(nota)} maior) \n \n {header} \n" + "".join(linhas)
    return txt

# Função para imprimir a tabela de acorde menor para uma nota específica
def acorde_menor(nota):
    graus_indices = [0, 3, 7]  # Índices das colunas 1, 4 e 8 para acorde menor
    linhas, header = imprimir_tabela_acordes(graus_indices, nota)
    txt = f"{nota.upper()}m - ({nome(nota)} menor) \n \n {header} \n" + "".join(linhas)
    return txt


