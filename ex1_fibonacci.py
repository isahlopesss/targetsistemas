num = int(input("Informe um número: "))

retorno = False

n1 = 0
n2 = 1

while n1 <= num:
    aux = n1 + n2
    n1 = n2
    n2 = aux

    if n1 == num:
        retorno = True

if retorno:
    print("O número informado pertence a sequência")
else:
    print("O número informado não pertence a sequência")