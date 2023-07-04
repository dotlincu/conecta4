import os


def menu():
    print("Selecione uma opção:")
    print("1. Connect 4")
    print("2. Connect 4 com poda alfa-beta")
    print("3. Connect 4 com avaliação de desempenho")
    print("4. Connect 4 com poda alfa-beta e avaliação de desempenho")

    while True:
        opcao = input("Opção selecionada: ")

        if opcao == "1":
            os.system("python connect4.py")
            break
        elif opcao == "2":
            os.system("python connect4-poda-alfa-beta.py")
            break
        elif opcao == "3":
            os.system("python connect4-avaliacao.py")
            break
        elif opcao == "4":
            os.system("python connect4-juncao.py")
            break
        else:
            print("Opção inválida. Por favor, selecione novamente.")


menu()
