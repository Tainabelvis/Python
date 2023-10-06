#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Escreva o salário do funcionario: R$"))
novosalario = salario + (salario*15/100)

print("O salário que era R$ {:.2f}, agora teve um aumento de 15% e foi corrigido para R$ {:.2f}" . format(salario,novosalario))
