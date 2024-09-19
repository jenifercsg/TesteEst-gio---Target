def fibonacci(numero):
    a, b = 0, 1
    sequencia = [a, b]

    while b < numero:
        a, b = b, a + b
        sequencia.append(b)

    if numero in sequencia:
        return f"O número {numero} pertence a sequência fibonacci"
    else:
        return f"O número {numero} não pertence a sequência fibonacci"
    
numero_informado = int(input("Informe um número: "))
print(fibonacci(numero_informado))  