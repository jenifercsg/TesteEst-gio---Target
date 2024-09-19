import json

def calcular_faturamento(file):
    with open(file, 'r') as f:
        dados = json.load(f)["faturamento_diario"]

    faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]    

    if not faturamento_valido:
        return "Não há faturamento válido para análise"
    
    menor_faturamento = min(faturamento_valido)
    mior_faturamento = max(faturamento_valido)
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_faturamento])

    return{
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": mior_faturamento,
        "dias_acima_da_media": dias_acima_da_media,
        
    }

resultado = calcular_faturamento('faturamento.json')

print(f"Menor valor de faturamento: {resultado['menor_faturamento']}")
print(f"Maior valor de faturamento: {resultado['maior_faturamento']}")
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_da_media']}")