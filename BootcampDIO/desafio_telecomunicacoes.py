# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
    if consumo <= 10:
        return f"Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return f"Plano Prata Fibra - 100Mbps"
    elif consumo > 20:
        return f"Plano Premium Fibra - 300Mbps"
# TODO: Retorne o plano de internet adequado:
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Informe o valor do seu consumo mensal: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))