menu = '''
--------------------MENU--------------------
[1] Depositar

[2] Sacar

[3] Extrato

[4] Sair
--------------------------------------------

=> '''

saldo = 0
limite_por_saque = 500
extrato = ""
saque = 0
numero_saque = 1
LIMITE_SAQUES_DIARIO = 3

while True:

    opcao = input(menu)

    # Operação de Depósito

    if opcao == "1" :
        deposito = float (input("Qual valor deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ +{deposito:.2f}\n"
            
            print ("Depósito realizado com sucesso.")
        
        else:
            print ("O valor informado é invalido, por favor tente novamente.")
    
    # Operação de Saque

    elif opcao == "2":
        
        if saldo > 0:
            saque = float (input("Qual valor deseja sacar: "))
            
            if saque > limite_por_saque:
                
                print ("Limite máximo por saque é de R$ 500. Tente novamente.")
            
            elif numero_saque > LIMITE_SAQUES_DIARIO:
                
                print ("Numero de saques excedido.")

            elif saque > saldo:

                print ("Saldo insuficiente")
     
            elif saque < saldo:
               
                numero_saque +=1
                saldo -= saque
                extrato += f"Saque: R$ -{saque:.2f}\n"
                
                print ("Saque realizado com sucesso.")
                        
        else:
            
            print ("Saldo insuficiente")
            
    # Operação de Extrato 

    elif opcao == "3":
        
        extrato += f"Saldo atual: R$ {saldo:.2f}\n"
        
        print (">>>>>>>> EXIBINDO EXTRATO <<<<<<<< \n")
        print (extrato)
    
    # Opção para sair do sistema

    elif opcao == "4":
       
        print("Obrigado por usar nosso sistema!")
        
        break

    else:
        
        print ("Operação inválida, por favor selecione novamente a operação desajada.")


