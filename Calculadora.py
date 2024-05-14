def valores_conjuntos():
    A = set(input("Digite os elementos do conjunto A (separados por espaço): ").split())
    B = set(input("Digite os elementos do conjunto B (separados por espaço): ").split())
    return A, B

def uniao_conjuntos(A, B):
    return A.union(B)

def interseccao_conjuntos(A, B):
    return A.intersection(B)

def diferenca_conjuntos(A, B):
    return A.difference(B)

def verificar_subconjunto_proprio(A, B):
    if A.issubset(B) and A!= B:
        return True
    else:
        return False

def resultado_conjuntos(calculo, A, B):
    if calculo == "1":
        print("União: ", uniao_conjuntos(A, B))
    elif calculo == "2":
        print("Intersecção: ", interseccao_conjuntos(A, B))
    elif calculo == "3":
        print("Diferença: ", diferenca_conjuntos(A, B))
    elif calculo == "4":
        if verificar_subconjunto_proprio(A, B):
            print("A é um subconjunto próprio de B")
        else:
            print("A não é um subconjunto próprio de B")

def menu():
    while True:
        menu = input("O que deseja fazer?\n1) Conjuntos numéricos\n2)Funções do segundo grau\n3) Funções exponenciais\n4) Matrizes\n5) Sair\n")
        if menu == "5":
            print("Fechando...")
            break
        elif menu == "1":
            valores = valores_conjuntos()
            calculo = input("O que você deseja fazer?\n1) União de conjuntos\n2) Intersecção de conjuntos\n3) Diferença de conjuntos\n4) Verificação de subconjunto Próprio\n")
            resultado_conjuntos(calculo, valores[0], valores[1])
        else:
            print("Desculpe, não entendi. Por favor, digite: \n1) Conjuntos numéricos\n2)Funções do segundo grau\n3) Funções exponenciais\n4) Matrizes\n5) Sair\n")

menu()