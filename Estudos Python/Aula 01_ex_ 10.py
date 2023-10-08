#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input("Qual é preço do produto? R$"))
preçodesconto = preço - (preço*5/100)

print("O preço do produto com desconto de 5% é: R$ {}".format(preçodesconto))
