Case de Back-End: Desenvolvimento da Lógica de Negócios
Contexto:
Você foi contratado como estagiário em uma empresa de tecnologia que está desenvolvendo
uma API simples para cadastro e gestão de pessoas.
A empresa recebeu a seguinte solicitação de um cliente:
"Estamos buscando uma aplicação que nos permita cadastrar informações básicas sobre
nossos funcionários e realizar operações de consulta,
atualização e exclusão desses registros."
A API deve ser construida em Python, utilizando o framework de sua escolha (FastAPI, Flask,
Django, etc...)

Tarefas para o desenvolvimento da API:
1. Definição das Rotas (endpoints):
• Definir as rotas necessárias para a aplicação, incluindo o tratamento de solicitações de
cadastro, listagem, atualização e exclusão de pessoas.

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

3. Validação de Dados:
• Validar os dados recebidos para garantir que estejam corretos e seguros.
• Tratar erros e exceções de forma apropriada.

4. Operações de CRUD (Create, Read, Update, Delete):
• Implementar as operações de cadastro, leitura, atualização e exclusão de pessoas.
