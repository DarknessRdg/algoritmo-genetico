from src import estrategias
from src.estrategias.mutacao import MutacaoStrategy
from src.mapa import CIDADES

# tamanho da população inicial
TAMANHO_POPULACAO_INICIAL = 10
# Controle populacional:
# Tamanho máximo que uma população pode atingir
TAMANHO_MAXIMO_POPULACAO = 100
# Taxa de reprodução em porcentagem : 0-100
TAXA_DE_REPRODUCAO = 1
# Taxa de mutação em porcentagem: 0-100
TAXA_MUTACAO = 50
# Quantidade máxima de gerações
MAX_GERACOES = 5

# Cidade ponto de partida da busca
CIDADE_INICIAL = CIDADES.get_cidade('A')

# Strategy para criação da população inicial
POPULACAO_INICIAL_STRATEGY = estrategias.PopulacaoInicialStrategy(
    inicio=CIDADE_INICIAL,
    tamanho_cromossos=CIDADES.tamanho
)

# Strategy para realizar cross over entre 2 cromossos
CROSS_OVER_STRATEGY = estrategias.CrossOverStrategy()

# Strategy para realizar controle populacional
CONTROLE_POPULACIONAL = estrategias.ControlePopulacionalStrategy()

# Strategy para realizar mutações em 1 cromossomo
MUTACAO_STRATEGY = MutacaoStrategy(taxa_mutacao=TAXA_MUTACAO)
