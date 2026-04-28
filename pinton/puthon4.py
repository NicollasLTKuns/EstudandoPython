dados = ['Bruno', 42, 3.14, 3, 'C']
for d in dados:
    match d:
        case str(d):
            print("String: ", d)
        case int(d):
            print("Inteiro", d)
        case float(d):
            print("float: ", d)
        case _:
            print("Caso default, tipo desconhecido")