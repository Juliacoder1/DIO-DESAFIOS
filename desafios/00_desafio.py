cartao_conta = print("cartão inserido com sucesso, escolha uma opção: ")

menu = """

[d] depositar 
[s] sacar
[e] extrato
[q] sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = (input(menu))

    if opcao == "d":
        valor = float(input("insira o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R$ {valor:.2f} depositado com sucesso!")

        else:
            print("operação falhou: o valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou: você não tem saldo suficente")

        elif excedeu_limite:
            print("operação falhou: o valor de saques excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Retire o seu dinheiro na boca do caixa: R$ {valor:.2f}")
            print(f"Você ainda pode realizar {LIMITE_SAQUES -+ numero_saques} saques")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")