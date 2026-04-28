soma = 0
while True:
    valor = int(input(f"escolha um numero entre 1 e 100(0 para sair)"))
    match valor:
        case valor if valor >= 1 and valor <= 100:
            soma += valor
        case 0:
            print(f"Valor total {soma}")
            break
        case _:
            print("Valor invalido")