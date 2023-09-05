print("seja bem vindo =)")

while True:
    num1 = float(input("digite o primeiro número: "))
    operador = input("digite a operação (+, -, x, /)")
    num2 = float(input("digite o segundo número: "))
    
    resultado = None
    
    if operador == '-':
        resultado = num1 - num2
        print("resultado", resultado)
    elif operador == '+':
        resultado = num1 + num2
        print("resultado", resultado)

    elif operador == 'x':
        resultado = num1 * num2
        print("resultado", resultado)

    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print("resultado", resultado)
        
        else:
            print("erro: divisão por zero.")
            continue

    else:
        print("operador inválido")
    resultado = input("deseja continuar calculando ? (s/n)")

    if resultado != 's' and resultado != 'S': 
        break
    
print("finalisando...")