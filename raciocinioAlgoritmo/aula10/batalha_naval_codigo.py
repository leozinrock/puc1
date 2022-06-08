numero_de_linhas = 20  # DEFINIMOS A MATRIZ PRINCIPAL COM 20 LINHAS
numero_de_colunas = 20
leganda_horizontal="    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20"
leganda_vertical= ["A", "B", "C", "D", "E", "F","G", "H", "I","J", "B", "C","A", "B", "C","A", "B", "C","A", "B"]
cont=0
def criar_matriz():
    matriz = ["#"] * numero_de_linhas
    for linha in range(numero_de_linhas):
       matriz[linha]=["#"]*numero_de_colunas
    return matriz

def imprimir_matriz(matriz):
    linha_matriz = ""
    print(leganda_horizontal)
    for linha in range(numero_de_linhas):
        linha_matriz += leganda_vertical[linha] + "   "
        for coluna in range(numero_de_colunas):
            linha_matriz+=matriz[linha][coluna]
            linha_matriz+= "  "
        print(linha_matriz)
        linha_matriz = ""

def menu():
    print("--------------------------------------------------")
    print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
    print("----------------------------")
    print("DISPONIBILIDADE DE VEÍCULOS MILITARES:")
    print("3xPORTA AVIÃO")
    print("4XCRUZADOR")
    print("5xFRAGATA")
    print("----------------------------")
    print("ESCOLHA UM VEICULO MILITAR:")
    print("1-PORTA-AVIÃO")
    print("2-CRUZADOR")
    print("3-FRAGATA")
    print("----------------------------")
    opcao = int(input("ESCOLHA O VEÍCULO DESEJADO PARA INSERIR:"))
menu()
def escolhendo_posicoes():
    linha=int(input("ESCOLHA UMA LINHA:"))
    coluna = int(input("ESCOLHA UMA COLUNA:"))
def escolha_porta_aviao(opcao,matriz):
    if opcao==1:
        for cont in range(3.):
            cont=cont+1
            posicao()
    matriz[linha][coluna] = "PA"


matriz_1=criar_matriz()
matriz_1[0][10]= "N"
imprimir_matriz(matriz_1)
posicao=escolhendo_posicoes()
escolha_porta_aviao(posicao,matriz_1)
