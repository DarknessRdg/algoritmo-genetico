from src import estrategias
from src.mapa import CIDADES

TAMANHO_POPULACAO_INICIAL = 4
TAMANHO_CROMOSSOMOS = CIDADES.tamanho

CIDADE_INICIAL = CIDADES.get_cidade('A')


POPULACAO_INICIAL_STRATEGY = estrategias.PopulacaoInicialStrategy(
    inicio=CIDADE_INICIAL,
    tamanho_cromossos=TAMANHO_CROMOSSOMOS
)
