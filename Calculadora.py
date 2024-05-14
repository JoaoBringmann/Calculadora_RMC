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
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
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

def resultado_funcao(calculo, a, b, c):
    if calculo == "1":
        calc_baskara(a, b, c)
    elif calculo == "2":
        print("O valor da função em x é: ", função_em_x_pedido(a, b, c))
    elif calculo == "3":
        calcular_vertice(a, b, c)


#-----Fim Funções do Segundo Grau-----#

def menu():
    while True:
        menu = input("O que deseja fazer?\n1) Conjuntos numéricos\n2) Funções do segundo grau\n3) Funções exponenciais\n4) Matrizes\n5) Sair\n")
        if menu == "5":
            print("Fechando...")
            break
        elif menu == "1":
            valores = valores_conjuntos()
            calculo = input("O que você deseja fazer?\n1) União de conjuntos\n2) Intersecção de conjuntos\n3) Diferença de conjuntos\n4) Verificação de subconjunto Próprio\n")
            resultado_conjuntos(calculo, valores[0], valores[1])
        elif menu == "2":
            valores = valores_funcao()
            calculo = input("O que você deseja fazer?\n1) Calcular raízes\n2) Calcular valor da função em x\n3) Calcular vértice\n")
            resultado_funcao(calculo, valores[0], valores[1], valores[2])
        else:
            print("Desculpe, não entendi. Por favor, digite: \n1) Conjuntos numéricos\n2)Funções do segundo grau\n3) Funções exponenciais\n4) Matrizes\n5) Sair\n")

menu()