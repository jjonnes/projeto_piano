def campo_notas():
    notas = []

    for i in range(97, 104):
        notas.append(chr(i).upper())
        if i != 98 and i != 101:
            notas.append(chr(i).upper() + '#')
    
    return notas

def campo_harmonico(nota):
    campo = []
    notas = campo_notas()
    start_index = notas.index(nota.upper())

    for i in range(12):
        index = (start_index + i) % len(notas)
        campo.append(notas[index])
    
    return campo

def imprimir_tabela_acordes(graus_indices, nota=None):
    notas = campo_notas()
    graus = ["Tônica", "  b2  ", "  2#  ", "  b3  ",
             "  3#  ", "  4j  ", "  4^  ", "  5j  ",
             "  b6  ", "  6#  ", "  b7  ", "  7#  "]

    # Calcula o comprimento máximo de cada coluna
    max_length = [len(grau) for grau in graus]

    for i in graus_indices:
        max_length[i] = max(len(graus[i]), max_length[i])

    # Imprime a primeira linha com os graus musicais
    header = "|"
    for i in graus_indices:
        header += f" {graus[i]}{' ' * (max_length[i] - len(graus[i]) + 1)} |"
    print(header)

    # Determina quais índices de notas imprimir
    if nota is None:
        notas_indices = range(12)
    else:
        notas_indices = [notas.index(nota.upper())]

    # Imprime os acordes para cada linha de notas
    for j in notas_indices:
        linha = "|"
        for i in graus_indices:
            campo = campo_harmonico(notas[j])
            linha += f" {campo[i]}{' ' * (max_length[i] - len(campo[i]) + 1)} |"
        print(linha)


def campo_har_completo():
    graus_indices = list(range(12))  # Índices das colunas 1, 5 e 8
    imprimir_tabela_acordes(graus_indices)

def acorde_maior():
    graus_indices = [0, 4, 7]  # Índices das colunas 1, 5 e 8
    print(f'Acordes maiores \n')
    imprimir_tabela_acordes(graus_indices)

def acorde_menor():
    graus_indices = [0, 3, 7]  # Índices das colunas 1, 4 e 8 para acorde menor
    print(f'Acordes menores \n')
    imprimir_tabela_acordes(graus_indices)

# Chama as funções para exibir as tabelas formatadas conforme desejado
campo_har_completo()
print("\n")
acorde_maior()
print("\n")
acorde_menor()
