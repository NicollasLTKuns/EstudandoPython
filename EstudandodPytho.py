lista  = []
iniciar = input("deseja iniciar?(S/N): ")
if iniciar == "s":
    cmc = True
elif iniciar == "n":
    cmc = False
else:
    print("Insira uma resposta válido!!")

while cmc:
    print("------------------------")
    print("----------MENU----------")
    print("------------------------")
    print("---1-Inserir------------")
    print("---2-Remorver-----------")
    print("---3-Listar Todos-------")
    print("---4-Ordenar------------")
    print("---5-Sair---------------")
    print("------------------------")
    opc = input("escolha uma opção: ")
    if opc == "1":
        nome = input("Insira um nome: ")
        lista.append(nome)
        print(lista)
    elif opc == "2":
        nome = input("Insira o nome de quem deseja remover: ")
        if nome in lista:
            lista.remove(nome)
            print("Removido")
        else:
            print("Nome não encontrado")
    elif opc == "3":
        for nome in lista:
            print(nome)
    elif opc == "4":
        lista.sort()
        print("Lista ordenada: ", lista)
    elif opc == "5":
        print("Saindo")
        break
    else:
        print("Opção inválida")