import json

with open('dados.json') as json_file:
    dados_faturamento = json.load(json_file)

valores_faturamento = [dia['valor'] for dia in dados_faturamento]
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

valores_faturamento_sem_zero = [valor for valor in valores_faturamento if valor > 0]
media_mensal = sum(valores_faturamento_sem_zero) / len(valores_faturamento_sem_zero)

dias_acima_da_media = len([valor for valor in valores_faturamento if valor > media_mensal])

print("Menor valor de faturamento: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento: R$ {:.2f}".format(maior_valor))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))
