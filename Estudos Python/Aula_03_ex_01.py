#Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Qunatas letras tem primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
Print("Analisando seu nome...")
Print("Seu nome com todas as letras e maiúsculas é {}".format(nome.upper()))
Print("Seu nome com todas as letras e minúsculas é {}".format(nome.lower()))
Print("Seu nome tem {} letras no total".format(len(nome) - nome.count(" ")))
Print("Seu primeiro nome tem {} letras".format(nome.fid(" ")))
