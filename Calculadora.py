import matplotlib.pyplot as plt
import numpy as np

#-----Funções dos conjuntos-----#

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

#-----Fim Funções dos conjuntos-----#

#-----Funções do Segundo Grau-----#

def valores_funcao():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    while True:
        try:
            b = float(input("Digite o valor de b: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    while True:
        try:
            c = float(input("Digite o valor de c: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    return a, b, c

def calc_delta(a, b, c):
    return (b**2) - (4*a*c)

def calc_baskara(a, b, c):
    calc_delta_value = calc_delta(a, b, c)
    if calc_delta_value < 0:
        print("Não existe raiz real")
    else:
        x1 = (((-1)*b) + (calc_delta_value**0.5))/(2*a)
        x2 = (((-1)*b) - (calc_delta_value**0.5))/(2*a)
        if x1 == x2:
            print("Existe apenas uma raiz real: ", x1)
        else:
            print("Existem duas raízes reais: ", x1, "e", x2)

def função_em_x_pedido(a, b, c):
    x = float(input("Digite o valor de x: "))
    return (a*x**2) + (b*x) + c

def calcular_vertice(a, b, c):
    if a == 0:
        print("Não é uma função do segundo grau")
    else:
        calc_delta_value = calc_delta(a, b, c)
        xv = ((-1)*b)/(2*a)
        yv = (-(b**2) + calc_delta_value)/(4*a)
        print("O vértice da função é, Maximo: ", xv, "e Minimo: ", yv)

def segundo_grau_grafico(a,b,c):
    x = np.linspace(-100, 100, 1000)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()

def resultado_funcao(calculo, a, b, c):
    if calculo == "1":
        calc_baskara(a, b, c)
    elif calculo == "2":
        print("O valor da função em x é: ", função_em_x_pedido(a, b, c))
    elif calculo == "3":
        calcular_vertice(a, b, c)
    elif calculo == "4":
        segundo_grau_grafico(a, b, c)
    else:
        print("Digite novamente..")

#-----Fim Funções do Segundo Grau-----#

#-----Funções exponenciais-----#

def valores_exponenciais():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    while True:
        try:
            b = float(input("Digite o valor de b: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    return a, b

def crescente_decrescente(a):
    if a > 1:
        print("A função é crescente")
    elif a > 0 and a < 1:
        print("A função é decrescente")

def calc_funcao_x(a,b):
    while True:
        try:
            x = float(input("Digite o valor de x: "))
            break
        except ValueError:
            print("Erro: deve ser um número. Tente novamente!")
    return (a*(b**x))

def exponencial_grafico(a,b):
    x = np.linspace(-100,100,1000)
    y = a*b**x
    plt.plot(x, y)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.axvline(x=0, color="k")
    plt.show()

def resultado_exponencial(calculo,a,b):
    if calculo == "1":
        crescente_decrescente(a)
    elif calculo == "2":
        print("O valor da função em x é: ", calc_funcao_x(a, b))
    elif calculo == "3":
        exponencial_grafico(a, b)
    else:
        print("Digite novamente..")

#-----Fim Funções exponenciais-----#

#-----Funções das Matrizes-----#

# Função para imprimir uma matriz

def gerarmatriz(num_linhas, num_colunas):
    matriz = []
    for l in range(num_linhas):
                linha = []
                for c in range(num_colunas):
                    elemento = int(input(f"Informe o elemento,{l}{c}: "))
                    linha.append(elemento)
                matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

# Função para verificar se uma matriz é quadrada
def eh_matriz_quadrada(matriz):
    return len(matriz) == len(matriz[0])

# Função para calcular o determinante de uma matriz 2x2
def calcular_determinante_2x2(matriz):
    if len(matriz) != 2 or len(matriz[0]) != 2:   #Verifica linha e coluna se é 2x2
        return None
    a, b = matriz[0]
    c, d = matriz[1]
    return a * d - b * c

# Função para calcular o determinante de uma matriz 3x3
def calcular_determinante_3x3(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        return None
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

# Função para multiplicar duas matrizes
def multiplicar_matrizes(matriz1, matriz2):
    numero_linhas1 = len(matriz1)
    numero_colunas1 = len(matriz1[0])

    numero_linhas2 = len(matriz2)
    numero_colunas2 = len(matriz2[0])
    
    # Verifica se o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz
    if numero_colunas1 != numero_linhas2:
        print("Multiplicação não possível")
    else:
        resultado = []
    for i in range(numero_linhas1):
        linha_resultado = []
        for j in range(numero_colunas2):
            elemento = 0
            for k in range(numero_colunas1):
                elemento += matriz1[i][k] * matriz2[k][j]
            linha_resultado.append(elemento)
        resultado.append(linha_resultado)
    return resultado

def calcular_transposta(matriz):
    transposta = []
    for j in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        transposta.append(linha)
    return transposta

def resultado_matriz(calculo, matriz):
    if calculo == "1":
        if matriz is not None and eh_matriz_quadrada(matriz):
            if len(matriz) == 2:
                print("Determinante da matriz: ", calcular_determinante_2x2(matriz))
            elif len(matriz) == 3:
                print("Determinante da matriz: ", calcular_determinante_3x3(matriz))
            else:
                print("Matriz não quadrada")
        else:
            print("Matriz não quadrada ou nenhuma matriz fornecida")
    elif calculo == "2":
        if matriz is not None:
            matriz2 = gerarmatriz(int(input("Informe o número de linhas da segunda matriz: ")), int(input("Informe o número de colunas da segunda matriz: ")))
            if matriz2 is not None:
                resultado = multiplicar_matrizes(matriz, matriz2)
                if resultado is not None:
                    print("Matriz resultante:")
                    for linha in resultado:
                        print("[", end="")
                        for elemento in linha:
                            print(elemento, end=",")
                        print("]")
            else:
                print("Nenhuma matriz fornecida para a segunda matriz")
        else:
            print("Nenhuma matriz fornecida")
    elif calculo == "3":
        if matriz is not None:
            transposta = calcular_transposta(matriz)
            print("Transposta:")
            for linha in transposta:
                print("[", end="")
                for elemento in linha:
                    print(elemento, end=",")
                print("]")
        else:
            print("Nenhuma matriz fornecida")



#-----Fim Funções das Matrizes-----#

#-----Menu-----#

def menu():
    while True:
        menu = input("O que deseja fazer?\n1) Conjuntos numéricos\n2) Funções do segundo grau\n3) Funções exponenciais\n4) Matrizes\n5) Sair\n")
        if menu == "5":
            print("Fechando...")
            break
        elif menu == "1":
            while True:
                min_menu = int(input("Digite 0 para voltar ou 1 para continuar: "))
                if min_menu == 0:
                    print("Voltando...")
                    continue
                elif min_menu == 1:
                    valores = valores_conjuntos()
                    calculo = input("O que você deseja fazer?\n1) União de conjuntos\n2) Intersecção de conjuntos\n3) Diferença de conjuntos\n4) Verificação de subconjunto Próprio\n")
                    resultado_conjuntos(calculo, valores[0], valores[1])
                    break
                else:
                    print("Digite Novamente")
        elif menu == "2":
            while True:
                min_menu = int(input("Digite 0 para voltar ou 1 para continuar: "))
                if min_menu == 0:
                    print("Voltando...")
                    continue
                elif min_menu == 1:
                    valores = valores_funcao()
                    calculo = input("O que você deseja fazer?\n1) Calcular raízes\n2) Calcular valor da função em x\n3) Calcular vértice\n4) Ver Grafico")
                    resultado_funcao(calculo, valores[0], valores[1], valores[2])
                    break
                else:
                    print("Digite Novamente")
        elif menu =="3":
            while True:
                min_menu = int(input("Digite 0 para voltar ou 1 para continuar: "))
                if min_menu == 0:
                    print("Voltando...")
                    continue
                elif min_menu == 1:
                    valores = valores_exponenciais()
                    calculo = input("O que você deseja fazer?\n1) Verificar se a função é crescente ou decrescente\n2) Calcular a função em x\n3) Ver Grafico")
                    resultado_exponencial(calculo, valores[0], valores[1])
                    break
                else:
                    print("Digite Novamente")

        elif menu == "4":
            while True:
                min_menu = int(input("Digite 0 para voltar ou 1 para continuar: "))
                if min_menu == 0:
                    print("Voltando...")
                    continue
                elif min_menu == 1:
                    linhas = int(input("Informe o numero de linhas da matriz"))
                    colunas = int(input("Informe o numero de colunas da matriz"))
                    matriz = gerarmatriz(linhas,colunas)
                    imprimir_matriz(matriz)
                    calculo = input("O que você deseja fazer?\n1) Determinante\n2) Multiplicação de Matriz\n3) Matriz Tranposta")
                    resultado_matriz(calculo,matriz)
                    break
                else: 
                    print("Digite Novamente")

        else:
            print("Desculpe, não entendi.")

#-----Fim Menu-----#

menu()