VALOR_MINIMO_DEPOSITO = 1.0


def depositar(saldo, valor):
    if valor < VALOR_MINIMO_DEPOSITO:
        print("Valor inválido para depósito")
        return saldo

    saldo += valor
    print("Depósito realizado!")
    return saldo


def sacar(saldo, valor):
    if valor > saldo:
        print("Saldo insuficiente")
        return saldo

    saldo -= valor
    print("Saque realizado!")
    return saldo


def mostrar_extrato(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")



saldo = 0.0
opcao = None

while opcao != "0":
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Valor: "))
        saldo = depositar(saldo, valor)

    elif opcao == "2":
        valor = float(input("Valor: "))
        saldo = sacar(saldo, valor)

    elif opcao == "3":
        mostrar_extrato(saldo)

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida")
