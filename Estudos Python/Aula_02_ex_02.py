#Faça um programa que leia o coprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

co = float(input("Comprimento do conteto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa é {:.2f}: " .format(hi))
