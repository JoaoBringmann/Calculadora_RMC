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
    if A.issubset(B) and A != B:
        return True
    else:
        return False

def resultado_conjuntos():
    valores = valores_conjuntos()
    print("União: ", uniao_conjuntos(valores[0], valores[1]))
    print("Intersecção: ", interseccao_conjuntos(valores[0], valores[1]))
    print("Diferença: ", diferenca_conjuntos(valores[0], valores[1]))
    if verificar_subconjunto_proprio(valores[0], valores[1]):
        print("A é um subconjunto próprio de B")
    else:
        print("A não é um subconjunto próprio de B")

def menu():
    while True:
        menu = input("O que deseja fazer?\nConjuntos numéricos\nFunções do segundo grau\nFunções exponenciais\nMatrizes\nSair\n").lower()
        while menu not in ["Conjuntos numéricos", "Funções do segundo grau", "Funções exponenciais","Matrizes","Sair"]:
                print("Desculpe, não entendi. Por favor, digite Conjuntos numéricos, Funções do segundo grau, Funções exponenciais, Matrizes, Sair.")
                menu = input("O que deseja fazer?\nConjuntos numéricos\nFunções do segundo grau\nFunções exponenciais\nMatrizes\nSair\n").lower()
        if menu == "conjuntos numéricos":
            calculo = input("O que você deseja fazer?\nUnião de conjuntos\nIntersecção de conjuntos\nDiferença de conjuntos\nVerificação de subconjunto Próprio\n").lower()
            if calculo == "união de conjuntos":
                resultado_conjuntos()
            elif calculo == "intersecção de conjuntos":
                resultado_conjuntos()
            elif calculo == "diferença de conjuntos":
                resultado_conjuntos()
            elif calculo == "verificação de subconjunto próprio":
                resultado_conjuntos()
            else:
                print("Digite Novamente")

        elif menu == "sair":
            print("Fechando")
            break

menu()