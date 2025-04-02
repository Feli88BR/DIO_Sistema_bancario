menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: """

# Variáveis no estado inicial
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor acima do limite permitido.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("============================================")
    
    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
