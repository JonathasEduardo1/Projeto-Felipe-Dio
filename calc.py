#Variáveis

vitorias = 1000
derrotas = 901

# Função calcular o nível do Herói com base no saldo de vitorias

def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

# Estrutura condicional para determinar a classificação do Herói com base no nível
  
    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return saldo_vitorias, nivel

# Retorno do código com exibição de mensagem ao jogador/usuário

saldo, nivel = calcular_nivel(vitorias, derrotas)
print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
