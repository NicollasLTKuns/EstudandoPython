while True:
    print("Menu de opções")
    print("1 - cadastrar")
    print("2 - consultar")
    print("3 - sair")
    opc = input(">>")
    match opc.lower():
        case '1'| "cadastrar" | "um":
            print("cadastrar")
        case '2' | "consultar" | "dois":
            print("consultar")
        case '3'| "sair" | "exit" |"quit" | "tres" | "três":
            print("Até logo")
            break
        case _:
            print("Opção ivalida, tente novamente")