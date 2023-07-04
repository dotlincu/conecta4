import os


def menu():
    print("Selecione uma opção:")
    print("1. connect4.py")
    print("2. connect4-juncao.py")
    print("3. connect4-avaliacao.py")
    print("4. connect4-poda-alfa-beta.py")

    while True:
        opcao = input("Opção selecionada: ")

        if opcao == "1":
            os.system("python connect4.py")
            break
        elif opcao == "2":
            os.system("python connect4-juncao.py")
            break
        elif opcao == "3":
            os.system("python connect4-avaliacao.py")
            break
        elif opcao == "4":
            os.system("python connect4-poda-alfa-beta.py")
            break
        else:
            print("Opção inválida. Por favor, selecione novamente.")


menu()
