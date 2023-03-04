import xml.etree.ElementTree as ET

tree = ET.parse('dados.xml')
root = tree.getroot()

menor_valor = float('inf')
maior_valor = float('-inf')
soma_valores = 0
dias_acima_media = 0
num_dias_mes = 30  # Considerando um mês com 30 dias

for row in root.iter('row'):
    dia = int(row.find('dia').text)
    valor = float(row.find('valor').text)


    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor


    soma_valores += valor


    if valor > soma_valores/num_dias_mes:
        dias_acima_media += 1

media_mensal = soma_valores/num_dias_mes

print(f'Menor valor: {menor_valor:.2f}')
print(f'Maior valor: {maior_valor:.2f}')
print(f'Número de dias acima da média mensal: {dias_acima_media}')
