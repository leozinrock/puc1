def criar_conta(saldo_inicial):
    global saldo
    saldo = saldo_inicial

def imprimir_saldo():
    print("Saldo = ", saldo)

def depositar(novo_valor):
    global saldo
    saldo += novo_valor

criar_conta(200)
imprimir_saldo()
depositar(200)
imprimir_saldo()