def inverter_string(texto):
    invertida = ""
    for i in range(len(texto)-1,-1,-1):
        invertida += texto[i]
    return invertida

texto = input("Digite uma string para ser invertida: ")
resultado = inverter_string(texto)
print(f"String invertida: {resultado}")    