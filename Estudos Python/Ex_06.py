#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere U$$1.00 = R$3.27

d = float(input("Quanto de dinheiro você tem na carteira? R$"))
dolar = d * 3.27

print("Você consegue comprar U$$ {:.2f} dolares" .format(dolar))
