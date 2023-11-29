def determinar_taxa_reajuste(salario):
    if salario <= 400.00:
        return 15
    elif salario <= 800.00:
        return 12
    elif salario <= 1200.00:
        return 10
    elif salario <= 2000.00:
        return 7
    else:
        return 4
salario = float(input())
# Determinar a taxa de reajuste com base no salário
taxa_reajuste = determinar_taxa_reajuste(salario)

# Calcular o valor do reajuste e o novo salário
valor_reajuste = salario * (taxa_reajuste / 100)
novo_salario = salario + valor_reajuste

# Imprimir os resultados em português
print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(valor_reajuste))
print("Em percentual: {} %".format(taxa_reajuste))
