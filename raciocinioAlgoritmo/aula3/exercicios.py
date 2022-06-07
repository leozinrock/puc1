import desconto as desconto

salario = float(input("Digite o salário mensal atual do funcionário: "))
novo = salario - (salario * 10 / 100)
print('O salario atual é R${}, com o desconto de 10% vai ficar R${}'.format(salario, novo))