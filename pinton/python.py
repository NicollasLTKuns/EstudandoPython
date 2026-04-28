while True:
    print("Menu de opções")
    print("1 - cadastrar")
    print("2 - consultar")
    print("3 - sair")
    opc = input(">>")
    match opc.lower():
        case '1':
            print("cadastrar")
        case '2':
            print("consultar")
        case '3':
            print("Até logo")
            break
        case _:
            print("Opção ivalida, tente novamente")