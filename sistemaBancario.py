print("""
      Bem vindo!
      
      1 - Saque
      2 - Saldo
      3 - Depósito
      4 - Extrato
      0 - Sair
      """)
saldo = 0.0
extrato = ""
limite = 500
saques = 0
LIMITE_SAQUES = 3


while(True):
    opcao = int(input("Selecione a opção desejada: "))
    
    if opcao == 1:
        valor_saque = int(input("Qual valor que você deseja sacar?"))
        
        if saques == LIMITE_SAQUES:
            print("Limite de quatidade de saques excedido.")
        else:        
            if valor_saque > 0:
                
                if valor_saque < saldo:
                    
                    if valor_saque <= limite:
                        saldo = saldo - valor_saque
                        extrato += f"Saque: R$ {valor_saque}.00 \n"
                        saques += 1
                        print("Saque realizado com sucesso!")
                        
                    else:
                        print("Seu valor de saque é maior que o limite disponivel de R$ 500.00") 
                        
                elif valor_saque > saldo:
                    print("Saldo indisponivel para este valor de saque.")
                    
            elif valor_saque <= 0:
                print("Valor de saque inválido, por favor informe um valor acima de zero.")
    
    if opcao == 2:
        print(f"Seu saldo é de: R$ {saldo:.2f}")
        
    if opcao == 3:
        valor_deposito = int(input("Informe o valor que deseja depositar: "))
        
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            print("Depósito feito com sucesso!")
            extrato += f"Depósito: R$ {valor_deposito}.00 \n"
        else:
            print("Valor de depósito inválido, por favor informe um valor acima de zero.")
            
    if opcao == 4:
        print(extrato)
    
    if opcao == 0:
        print("Muito obrigado, tenha um bom dia!")
        break