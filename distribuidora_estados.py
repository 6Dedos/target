faturamento_estados = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

total_faturamento = sum(faturamento_estados.values())

percentual_faturamento = {}
for estado, faturamento in faturamento_estados.items():
    percentual_faturamento[estado] = (faturamento / total_faturamento) * 100

print("Percentual de representação do faturamento por estado:")
for estado, percentual in percentual_faturamento.items():
    print(f"{estado}: {percentual:.2f}%")
