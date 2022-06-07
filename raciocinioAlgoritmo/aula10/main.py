def criar_conta(saldo_inicial):
    global saldo
    saldo = saldo_inicial

def imprimir_saldo():
    print("Saldo = ", saldo)

def depositar(novo_saldo):
    global saldo
    saldo += novo_saldo

criar_conta(200)
imprimir_saldo()
depositar(200)
imprimir_saldo()