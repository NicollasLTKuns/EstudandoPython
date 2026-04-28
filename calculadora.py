n1 = float(input("Insira um núero: "))
n2 = float(input("Insira outro núero: "))
print("Operação soma: +")
print("Operação subtração: -")
print("Operação multiplicação: *")
print("Operação divisão: /")
operacao = input("Insira a operação desejada: ")
match operacao:
    case "+":
        resultado = n1 + n2
        print(f"O resultado é: {resultado}")
    case "-":
        resultado = n1 - n2
        print(f"O resultado é: {resultado}")
    case  "*":
        resultado = n1 * n2
        print(f"O resultado é: {resultado}")
    case "/":
        resultado = n1 / n2
        print(f"O resultado é: {resultado}")