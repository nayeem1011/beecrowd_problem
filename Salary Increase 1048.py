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