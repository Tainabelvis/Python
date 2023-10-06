
2. Armazenamento de Dados:
• Implementar a lógica para armazenar os dados das pessoas cadastradas. Neste caso, você
pode armazená-los em memória ou utilizar algum banco de dados de sua escolha.
• Criar estruturas de dados apropriadas para representar as pessoas.
A entidade "Pessoa" deverá possuir os seguintes atributos:
Nome Completo
Data de nascimento
Endereço
CPF
Estado Civil



# Criaçao estruturas de dados Pessoa:

pessoa = {
    "Nome Completo": "Taina Belvis Garcez",
    "Data de Nascimento": "05/02/1993",
    "Endereço": "Rua Abernesia, 578 Santo Andre",
    "CPF": "123.456.789-00",
    "Estado Civil": "Casada"
}

# Para ver as informações das pessoas na lista:


print("Nome Completo:", pessoa["Nome Completo"])
print("Data de Nascimento:", pessoa["Data de Nascimento"])
print("Endereço:", pessoa["Endereço"])
print("CPF:", pessoa["CPF"])
print("Estado Civil:", pessoa["Estado Civil"])


