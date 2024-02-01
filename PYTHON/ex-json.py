import json

# Nome do arquivo JSON
nome_arquivo = "exemplo.json"

# Dados JSON
dados_json = {
    "nome": "Joao",
    "idade": 30,
    "cidade": "Sao Paulo"
}

# Cria e abre um novo arquivo no modo de escrita
with open(nome_arquivo, "w") as arquivo:
    # Escreve os dados JSON no arquivo
    json.dump(dados_json, arquivo)
