class Matriz:
    def __init__(self, linhas, colunas, elementos):
        self.linhas = linhas
        self.colunas = colunas
        self.elementos = elementos

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in linha]) for linha in self.elementos])

    def __add__(self, outra_matriz):
        if isinstance(outra_matriz, Matriz):
            if self.linhas == outra_matriz.linhas and self.colunas == outra_matriz.colunas:
                elementos_soma = [[self.elementos[i][j] + outra_matriz.elementos[i][j] for j in range(self.colunas)]
                                  for i in range(self.linhas)]
                return Matriz(self.linhas, self.colunas, elementos_soma)
            else:
                raise ValueError("As matrizes devem ter o mesmo número de linhas e colunas.")
        else:
            raise ValueError("A soma deve ser realizada com outra matriz.")

    def __sub__(self, outra_matriz):
        if isinstance(outra_matriz, Matriz):
            if self.linhas == outra_matriz.linhas and self.colunas == outra_matriz.colunas:
                elementos_sub = [[self.elementos[i][j] - outra_matriz.elementos[i][j] for j in range(self.colunas)]
                                 for i in range(self.linhas)]
                return Matriz(self.linhas, self.colunas, elementos_sub)
            else:
                raise ValueError("As matrizes devem ter o mesmo número de linhas e colunas.")
        else:
            raise ValueError("A subtração deve ser realizada com outra matriz.")

    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            elementos_mul = [[self.elementos[i][j] * escalar for j in range(self.colunas)]
                             for i in range(self.linhas)]
            return Matriz(self.linhas, self.colunas, elementos_mul)
        else:
            raise ValueError("A multiplicação por escalar deve ser realizada com um número real.")

    def __matmul__(self, outra_matriz):
        if isinstance(outra_matriz, Matriz):
            if self.colunas == outra_matriz.linhas:
                elementos_mul_mat = [[sum(self.elementos[i][k] * outra_matriz.elementos[k][j]
                                          for k in range(self.colunas))
                                       for j in range(outra_matriz.colunas)]
                                      for i in range(self.linhas)]
                return Matriz(self.linhas, outra_matriz.colunas, elementos_mul_mat)
            else:
                raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        else:
            raise ValueError("A multiplicação matricial deve ser realizada com outra matriz.")

    def transposta(self):
        elementos_transposta = [[self.elementos[j][i] for j in range(self.linhas)]
                                for i in range(self.colunas)]
        return Matriz(self.colunas, self.linhas, elementos_transposta)

    def traco(self):
        if self.linhas == self.colunas:
            traco = sum(self.elementos[i][i] for i in range(self.linhas))
            return traco
        else:
            raise ValueError("O traço só pode ser calculado para matrizes quadradas.")


class MatrizQuadrada(Matriz):
    def determinante(self):
        if self.linhas == self.colunas:
            # Implemente o cálculo do determinante para matrizes quadradas
            if self.linhas == 1:
                return self.elementos[0][0]
            elif self.linhas == 2:
                return self.elementos[0][0] * self.elementos[1][1] - self.elementos[0][1] * self.elementos[1][0]
            else:
                determinante = 0
                for i in range(self.linhas):
                    cofator = (-1) ** i * self.elementos[0][i] * self.submatriz(0, i).determinante()
                    determinante += cofator
                return determinante
        else:
            raise ValueError("O determinante só pode ser calculado para matrizes quadradas.")

    def submatriz(self, i, j):
        sub_elementos = [row[:j] + row[j + 1:] for row in (self.elementos[:i] + self.elementos[i + 1:])]
        return Matriz(len(sub_elementos), len(sub_elementos[0]), sub_elementos)


class MatrizTriangularInferior(Matriz):
    def determinante(self):
        if self.linhas == self.colunas:
            determinante = 1
            for i in range(self.linhas):
                determinante *= self.elementos[i][i]
            return determinante
        else:
            raise ValueError("O determinante só pode ser calculado para matrizes triangulares.")


class MatrizTriangularSuperior(Matriz):
    def determinante(self):
        if self.linhas == self.colunas:
            determinante = 1
            for i in range(self.linhas):
                determinante *= self.elementos[i][i]
            return determinante
        else:
            raise ValueError("O determinante só pode ser calculado para matrizes triangulares.")


class MatrizDiagonal(Matriz):
    def __add__(self, outra_matriz):
        if isinstance(outra_matriz, MatrizDiagonal):
            if self.linhas == outra_matriz.linhas and self.colunas == outra_matriz.colunas:
                elementos_soma = [self.elementos[i] + outra_matriz.elementos[i] for i in range(self.linhas)]
                return MatrizDiagonal(self.linhas, elementos_soma)
            else:
                raise ValueError("As matrizes diagonais devem ter o mesmo número de linhas e colunas.")
        else:
            return super().__add__(outra_matriz)

    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            elementos_mul = [elemento * escalar for elemento in self.elementos]
            return MatrizDiagonal(self.linhas, elementos_mul)
        else:
            raise ValueError("A multiplicação por escalar deve ser realizada com um número real.")


class CalculadoraMatricial:
    def __init__(self):
        self.lista_matrizes = [
            Matriz(2, 2, [[1, 2], [3, 4]]),
            Matriz(3, 3, [[2, 0, 0], [0, 3, 0], [0, 0, 4]])
        ]

    def imprimir_matriz(self, indice=None):
        if indice is None:
            for i, matriz in enumerate(self.lista_matrizes):
                print(f"Matriz {i}:")
                print(matriz)
        else:
            if 0 <= indice < len(self.lista_matrizes):
                print(f"Matriz {indice}:")
                print(self.lista_matrizes[indice])
            else:
                print("Índice inválido!")

    def inserir_matriz_teclado(self):
        linhas = int(input("Digite o número de linhas: "))
        colunas = int(input("Digite o número de colunas: "))
        elementos = []
        for i in range(linhas):
            linha = [float(x) for x in input(f"Digite os elementos da linha {i + 1} separados por espaço: ").split()]
            if len(linha) != colunas:
                raise ValueError(f"A linha {i + 1} deve conter {colunas} elementos.")
            elementos.append(linha)
        self.lista_matrizes.append(Matriz(linhas, colunas, elementos))
        print("Matriz inserida com sucesso!")

    def inserir_matriz_identidade(self, n):
        elementos = [[0] * n for _ in range(n)]
        for i in range(n):
            elementos[i][i] = 1
        self.lista_matrizes.append(MatrizQuadrada(n, n, elementos))
        print("Matriz identidade inserida com sucesso!")

    def alterar_remover_matriz(self):
        opcao = input("Deseja [a]lterar ou [r]emover uma matriz? ").lower()
        if opcao == 'a':
            indice = int(input("Digite o índice da matriz que deseja alterar: "))
            if 0 <= indice < len(self.lista_matrizes):
                self.lista_matrizes[indice] = self.inserir_matriz_teclado()
                print("Matriz alterada com sucesso!")
            else:
                print("Índice inválido!")
        elif opcao == 'r':
            indice = int(input("Digite o índice da matriz que deseja remover: "))
            if 0 <= indice < len(self.lista_matrizes):
                del self.lista_matrizes[indice]
                print("Matriz removida com sucesso!")
            else:
                print("Índice inválido!")
        else:
            print("Opção inválida!")

    def apresentar_lista(self):
        for i, matriz in enumerate(self.lista_matrizes):
            print(f"Matriz {i}: {matriz.linhas}x{matriz.colunas}")

    def gravar_backup(self, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            for matriz in self.lista_matrizes:
                file.write(f"{matriz.linhas} {matriz.colunas}\n")
                for linha in matriz.elementos:
                    file.write(' '.join(map(str, linha)) + '\n')
                file.write('\n')
        print(f"Backup salvo com sucesso no arquivo '{nome_arquivo}'!")

    def ler_outra_lista(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                linhas = file.readlines()
                i = 0
                while i < len(linhas):
                    linhas_matriz = linhas[i:i + int(linhas[i]) + 1]
                    linhas_matriz = [linha.strip().split() for linha in linhas_matriz[1:]]
                    linhas_matriz = [[float(elem) for elem in linha] for linha in linhas_matriz]
                    linhas, colunas = len(linhas_matriz), len(linhas_matriz[0])
                    self.lista_matrizes.append(Matriz(linhas, colunas, linhas_matriz))
                    i += linhas + 1
            print(f"Lista de matrizes do arquivo '{nome_arquivo}' carregada com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")

    def zerar_lista(self):
        self.lista_matrizes = []
        print("Lista de matrizes zerada com sucesso!")

    def soma_matricial(self, indice_a, indice_b):
        try:
            if 0 <= indice_a < len(self.lista_matrizes) and 0 <= indice_b < len(self.lista_matrizes):
                matriz_a = self.lista_matrizes[indice_a]
                matriz_b = self.lista_matrizes[indice_b]
                if matriz_a.linhas == matriz_b.linhas and matriz_a.colunas == matriz_b.colunas:
                    elementos_soma = [
                        [matriz_a.elementos[i][j] + matriz_b.elementos[i][j]
                         for j in range(matriz_a.colunas)] for i in range(matriz_a.linhas)
                    ]
                    resultado = Matriz(matriz_a.linhas, matriz_a.colunas, elementos_soma)
                    self.lista_matrizes.append(resultado)
                    print("Soma matricial realizada com sucesso!")
                    print("Resultado:")
                    for linha in resultado.elementos:
                        print(linha)
                else:
                    print("As matrizes devem ter o mesmo número de linhas e colunas.")
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao realizar a soma matricial: {e}")

    def multiplicacao_matricial(self, indice_a, indice_b):
        try:
            if 0 <= indice_a < len(self.lista_matrizes) and 0 <= indice_b < len(self.lista_matrizes):
                matriz_a = self.lista_matrizes[indice_a]
                matriz_b = self.lista_matrizes[indice_b]
                if matriz_a.colunas == matriz_b.linhas:
                    elementos_mult = [
                        [sum(matriz_a.elementos[i][k] * matriz_b.elementos[k][j]
                              for k in range(matriz_a.colunas))
                         for j in range(matriz_b.colunas)]
                        for i in range(matriz_a.linhas)
                    ]
                    resultado = Matriz(matriz_a.linhas, matriz_b.colunas, elementos_mult)
                    self.lista_matrizes.append(resultado)
                    print("Multiplicação matricial realizada com sucesso!")
                    print("Resultado:")
                    for linha in resultado.elementos:
                        print(linha)
                else:
                    print("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.")
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao realizar a multiplicação matricial: {e}")

    def multiplicacao_escalar(self, escalar, indice_matriz):
        try:
            if 0 <= indice_matriz < len(self.lista_matrizes):
                matriz = self.lista_matrizes[indice_matriz]
                elementos_mul = [
                    [elemento * escalar for elemento in linha] for linha in matriz.elementos
                ]
                resultado = Matriz(matriz.linhas, matriz.colunas, elementos_mul)
                self.lista_matrizes.append(resultado)
                print("Multiplicação por escalar realizada com sucesso!")
                print("Resultado:")
                for linha in resultado.elementos:
                    print(linha)
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao realizar a multiplicação por escalar: {e}")

    def transposicao(self, indice_matriz):
        try:
            if 0 <= indice_matriz < len(self.lista_matrizes):
                matriz = self.lista_matrizes[indice_matriz]
                elementos_transpostos = [
                    [matriz.elementos[j][i] for j in range(matriz.linhas)] for i in range(matriz.colunas)
                ]
                resultado = Matriz(matriz.colunas, matriz.linhas, elementos_transpostos)
                self.lista_matrizes.append(resultado)
                print("Transposição realizada com sucesso!")
                print("Resultado:")
                for linha in resultado.elementos:
                    print(linha)
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao realizar a transposição: {e}")

    def calcular_traco(self, indice_matriz):
        try:
            if 0 <= indice_matriz < len(self.lista_matrizes):
                matriz = self.lista_matrizes[indice_matriz]
                if matriz.linhas == matriz.colunas:
                    traco = sum(matriz.elementos[i][i] for i in range(matriz.linhas))
                    print(f"O traço da matriz é: {traco}")
                else:
                    print("A matriz não é quadrada, o traço não pode ser calculado.")
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao calcular o traço: {e}")

    def calcular_determinante(self, indice_matriz):
        try:
            if 0 <= indice_matriz < len(self.lista_matrizes):
                matriz = self.lista_matrizes[indice_matriz]
                if matriz.linhas == matriz.colunas:
                    determinante = 1
                    for i in range(matriz.linhas):
                        determinante *= matriz.elementos[i][i]
                    print(f"O determinante da matriz é: {determinante}")
                else:
                    print("A matriz não é quadrada, o determinante não pode ser calculado.")
            else:
                print("Índice de matriz inválido!")
        except Exception as e:
            print(f"Erro ao calcular o determinante: {e}")



def exibir_menu():
    calculadora = CalculadoraMatricial()

    while True:
        print("\n------ MENU ------")
        print("1. Imprimir Matriz")
        print("2. Inserir Matriz do Teclado")
        print("3. Inserir Matriz Identidade")
        print("4. Alterar ou Remover Matriz")
        print("5. Apresentar Lista de Matrizes")
        print("6. Gravar Backup")
        print("7. Ler Outra Lista")
        print("8. Zerar Lista de Matrizes")
        print("9. Soma Matricial")
        print("10. Subtração Matricial")
        print("11. Multiplicação por Escalar")
        print("12. Multiplicação Matricial")
        print("13. Transposição")
        print("14. Calcular Traço (Matriz Quadrada)")
        print("15. Calcular Determinante (Matriz Triangular)")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            indice = int(input("Digite o índice da matriz a ser impressa: "))
            calculadora.imprimir_matriz(indice)
        elif escolha == "2":
            calculadora.inserir_matriz_teclado()
        elif escolha == "3":
            n = int(input("Digite a ordem da matriz identidade: "))
            calculadora.inserir_matriz_identidade(n)
        elif escolha == "4":
            calculadora.alterar_remover_matriz()
        elif escolha == "5":
            calculadora.apresentar_lista()
        elif escolha == "6":
            nome_arquivo = input("Digite o nome para o backup: ")
            calculadora.gravar_backup(nome_arquivo)
        elif escolha == "7":
            nome_arquivo = input("Digite o nome do arquivo para leitura: ")
            calculadora.ler_outra_lista(nome_arquivo)
        elif escolha == "8":
            calculadora.zerar_lista()
        elif escolha == "9":
            a = int(input("Digite o índice da primeira matriz: "))
            b = int(input("Digite o índice da segunda matriz: "))
            calculadora.soma_matricial(a, b)
        elif escolha == "10":
            a = int(input("Digite o índice da primeira matriz: "))
            b = int(input("Digite o índice da segunda matriz: "))
            calculadora.subtracao_matricial(a, b)
        elif escolha == "11":
            escalar = float(input("Digite o escalar a ser multiplicado: "))
            matriz = int(input("Digite o índice da matriz: "))
            calculadora.multiplicacao_escalar(escalar, matriz)
        elif escolha == "12":
            a = int(input("Digite o índice da primeira matriz: "))
            b = int(input("Digite o índice da segunda matriz: "))
            calculadora.multiplicacao_matricial(a, b)
        elif escolha == "13":
            matriz = int(input("Digite o índice da matriz a ser transposta: "))
            calculadora.transposicao(matriz)
        elif escolha == "14":
            matriz = int(input("Digite o índice da matriz quadrada para calcular o traço: "))
            calculadora.calcular_traco(matriz)
        elif escolha == "15":
            matriz = int(input("Digite o índice da matriz triangular para calcular o determinante: "))
            calculadora.calcular_determinante(matriz)
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")


exibir_menu()
