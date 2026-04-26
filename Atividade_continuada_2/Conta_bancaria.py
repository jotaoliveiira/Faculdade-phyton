VALOR_MINIMO_DEPOSITO = 1.0

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Valor inválido para depósito")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato


def sacar(saldo, valor, extrato):
    if valor <= 0:
        print("Valor inválido para saque")
        return saldo, extrato

    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, extrato

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    print("Saque realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato


def mostrar_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if extrato == "":
        print("Não há movimentações.")
    else:
        print(extrato)

    print(f"Saldo atual: R$ {saldo:.2f}")


saldo = 0.0
extrato = ""
opcao = None

while opcao != "0":
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Valor: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Valor: "))
        saldo, extrato = sacar(saldo, valor, extrato)

    elif opcao == "3":
        mostrar_extrato(saldo, extrato)

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opção inválida")