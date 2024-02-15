menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=====Selecine uma opção:=====

"""

saldo = 0
limite = 500
extrato = ""
n_saques = 0
L_SAQUES = 3
condicao = True

while condicao:

    opcao = input(menu)
   
    if opcao == ("d" or "D"):
        valor = float(input("Informe um valor para deposito: "))
        if (valor > 0):
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor de deposito inválido")

    elif opcao == ("s" or "S"):
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = n_saques >= L_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            n_saques += 1

        else: 
            print("Operação falhou! O Valor informado é inválido.")
    
    elif opcao == ("e" or "E"):
        print("\n=============== Extrato ===============")
        print("Não foram realizadas novimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == ("q" or "Q"):
        condicao = False

    else:
        print("Valor de entrada invalido, tente novamente!")
        
    