numero_de_linhas = 20  # DEFINIMOS A MATRIZ PRINCIPAL COM 20 LINHAS
numero_de_colunas = 20  # DEFINIMOS A MATRIZ PRINCIPAL COM 20 COLUNAS
matriz = [0] * numero_de_linhas
contador_de_acertos_porta_aviao = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UM PORTA AVIÃO
contador_de_acertos_fragata = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UMA FRAGATA
contador_de_acertos_cruzador = 0  # DECLARAÇÃO DE VARIAVÉL PARA QUANDO O JOGADOR 2 ACERTAR UM CRUZADOR
cont = 0  # DEFINIMOS O CONTADOR PARA RODAR O JOGO
porta_aviao_1 = 11  # DEFINIÇÃO DA PRIMEIRA PORTA AVIÃO
porta_aviao_2 = 12  # DEFINIÇÃO DO SEGUNDO PORTA-AVIÃO
porta_aviao_3 = 13  # DEFINIÇÃO DO TERCEIRO PORTA-AVIÃO
cruzador_1 = 21  # DEFINIÇÃO DO PRIMEIRO CRUZADOR
cruzador_2 = 22  # DEFINIÇÃO DO SEGUNDO CRUZADOR
cruzador_3 = 23  # DEFINIÇÃO DO TERCEIRO CRUZADOR
cruzador_4 = 24  # DEFINIÇÃO DO TERCEIRO CRUZADOR
fragata_1 = 31  # DEFINIÇÃO DO PRIMEIRA FRAGATA
fragata_2 = 32  # DEFINIÃO DA SEGUNDA FRAGATA
fragata_3 = 33  # DEFINIÇÃO DA TERCEIRA FRAGATA
fragata_4 = 34  # DEFINIÇÃO DA QUARTA FRAGATA
fragata_5 = 35  # DEFINIÇÃO DA QUINTA FRAGATA
for linha in range(numero_de_linhas):  # PARA CRIAR AS COLUNAS DA MATRIZ
    matriz[linha] = [0] * numero_de_colunas
def inserir_coordenadas_porta_aviao():
    for cont in range(3):  # USO DE UM LOOP PARA O USUÁRIO ESCOLHER AS 4 COORDENADAS
        cont = cont + 1
        linha = int(input("DIGITE UMA LINHA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))
        coluna = int(input("DIGITE UMA COLUNA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))

def inserir_coordenadas_cruzador():
    for cont in range(1):  # USO DE UM LOOP PARA O USUÁRIO ESCOLHER AS 4 COORDENADAS
        cont = cont + 1
        linha = int(input("DIGITE UMA LINHA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))
        coluna = int(input("DIGITE UMA COLUNA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))
def inserir_coordenadas_fragata():
    for cont in range(1):  # USO DE UM LOOP PARA O USUÁRIO ESCOLHER AS 4 COORDENADAS
        cont = cont + 1
        linha = int(input("DIGITE UMA LINHA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))
        coluna = int(input("DIGITE UMA COLUNA PARA ESCONDER UMA PARTE DESTE VEÍCULO MILITAR:"))
def jogador_1_escolha():  # CRIAÇÃO DE UMA FUNÇÃOO PARA O JOGADOR_1 ESCONDER OS VEÍCULOS MILITAR
    print("--------------------------------------------------")
    print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
    print("----------------------------")
    print("DISPONIBILIDADE DE VEÍCULOS MILITARES:")
    print("3xPORTA AVIÃO")
    print("4XCRUZADOR")
    print("5xFRAGATA")
    def escondendo_porta_aviao():
        def Menu_porta_aviao():  # UMA FUNÇAO PARA APARECER UM MINI MENU SEMPRE QUE o JOGADOR SELECIONAR ESCOLHER ESCONDER UM PORTA AVIÃO
            for cont in range(1):
                print("----------------------------")
                print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
                print("----------------------------")
                print("1°PORTA-AVIÃO=11")
                print("2°PORTA-AVIÃO=12")
                print("3°PORTA-AVIÃO=13")
                print("----------------------------")
        Menu_porta_aviao()
        print("----------------------------")
        print("ESCONDENDO 0 1°PORTA-AVIÃO")
        def inserindo_um_porta_aviao():
            inserir_coordenadas_porta_aviao()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = porta_aviao_1
        inserindo_um_porta_aviao()
        print("----------------------------")
        print("ESCONDENDO 0 2°PORTA-AVIÃO:")
        def inserindo_segundo_porta_aviao():
            inserir_coordenadas_porta_aviao()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = porta_aviao_2
        inserindo_segundo_porta_aviao()
        print("----------------------------")
        print("ESCONDENDO 0 3°PORTA-AVIÃO:")
        def inserindo_terceiro_porta_aviao():
            inserir_coordenadas_porta_aviao()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = porta_aviao_3
        inserindo_terceiro_porta_aviao()
        print("----------------------------")
    escondendo_porta_aviao()
    def escondendo_cruzador():
        def Main_menu_cruzador():  # UMA FUNÇAO PARA APARECER UM MINI MENU QUANDO O JOGADOR ESCOLHER A OPÇÃO DE CRUZADOR
            for cont in range(1):
                print("----------------------------")
                print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
                print("----------------------------")
                print("1°CRUZADOR=21")
                print("2°CRUZADOR=22")
                print("3°CRUZADOR=23")
                print("4°CRUZADOR=24")
                print("----------------------------")
        Main_menu_cruzador()
        print("----------------------------")
        print("ESCONDENDO 0 1°CRUZADOR")
        def inserido_um_cruzador():
            inserir_coordenadas_cruzador()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = cruzador_1
        inserido_um_cruzador()
        print("----------------------------")
        print("ESCONDENDO 0 2°CRUZADOR")
        def inserido_dois_cruzador():
            inserir_coordenadas_cruzador()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = cruzador_2
        inserido_dois_cruzador()
        print("----------------------------")
        print("ESCONDENDO 0 3°CRUZADOR")
        def inserido_tres_cruzador():
            inserir_coordenadas_cruzador()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = cruzador_3
        inserido_tres_cruzador()
        print("----------------------------")
        print("ESCONDENDO 0 4°CRUZADOR")
        def inserido_quatro_cruzador():
            inserir_coordenadas_cruzador()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = cruzador_4
        inserido_quatro_cruzador()
    escondendo_cruzador()
    def escondendo_fragata():
        def Main_menu_fragata():  # UMA FUNÇÃO PARA APARECER UM MINI MENU QUANDO O USUÁRIO FOR ESCOLHER A OPÇÃO DE FRAGATA
            for cont in range(1):
                print("----------------------------")
                print("ESCOLHA EM QUAL POSIÇÃO,VOCÊ QUER ESCONDER ESSE VEICULO MILITAR:")
                print("----------------------------")
                print("1°FRAGATA=31")
                print("2°FRAGATA=32")
                print("3°FRAGATA=33")
                print("4°FRAGATA=34")
                print("5°FRAGATA=35")
                print("----------------------------")
        Main_menu_fragata()
        print("----------------------------")
        print("ESCONDENDO A 1°FRAGATA")
        def escondendo_uma_fragata():  # UMA FUNÇÃO PARA QUE FAZ O JOGADOR ESCONDER AS FRAGATAS
            inserir_coordenadas_fragata()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = fragata_1
        escondendo_uma_fragata()
        print("----------------------------")
        print("ESCONDENDO A 2°FRAGATA")
        def escondendo_duas_fragata():  # UMA FUNÇÃO PARA QUE FAZ O JOGADOR ESCONDER AS FRAGATAS
            inserir_coordenadas_fragata()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = fragata_2
        escondendo_duas_fragata()
        print("----------------------------")
        print("ESCONDENDO A 3°FRAGATA")
        def escondendo_tres_fragata():  # UMA FUNÇÃO PARA QUE FAZ O JOGADOR ESCONDER AS FRAGATAS
            inserir_coordenadas_fragata()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = fragata_3
        escondendo_tres_fragata()
        print("----------------------------")
        print("ESCONDENDO A 4°FRAGATA")
        def escondendo_quatro_fragata():  # UMA FUNÇÃO PARA QUE FAZ O JOGADOR ESCONDER AS FRAGATAS
            inserir_coordenadas_fragata()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = fragata_4
        escondendo_quatro_fragata()
        print("----------------------------")
        print("ESCONDENDO A 5°FRAGATA")
        def escondendo_cinco_fragata():  # UMA FUNÇÃO PARA QUE FAZ O JOGADOR ESCONDER AS FRAGATAS
            inserir_coordenadas_fragata()
            for linha in range(numero_de_linhas):
                for coluna in range(numero_de_colunas):
                    matriz[linha][coluna] = fragata_5
        escondendo_cinco_fragata()
    escondendo_fragata()

    def imprirmir_mapa(matriz):  # UMA FUNÇÃO PARA IMPRIRMIR UM MAPA
        print(matriz)
    imprirmir_mapa(matriz)
jogador_1_escolha()
