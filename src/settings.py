from src import estrategias
from src.aleatorio import ElementoRoleta, Roleta
from src.mapa import CIDADES

TAMANHO_POPULACAO_INICIAL = 4
TAMANHO_CROMOSSOMOS = CIDADES.tamanho

MAX_GERACOES = 5

CIDADE_INICIAL = CIDADES.get_cidade('A')

POPULACAO_INICIAL_STRATEGY = estrategias.PopulacaoInicialStrategy(
    inicio=CIDADE_INICIAL,
    tamanho_cromossos=TAMANHO_CROMOSSOMOS
)

CROSS_OVER_STRATEGY = estrategias.CrossOverStrategy()


def ordenar_populacao(populacao):
    populacao.sort(key=lambda cromossomo: cromossomo.fitness, reverse=True)


def criar_roleta(populacao):
    elementos = (
        ElementoRoleta(elemento=cromossomo, probablidade=cromossomo.fitness)
        for cromossomo in populacao
    )

    return Roleta(*elementos)


def main():
    populacao = POPULACAO_INICIAL_STRATEGY.criar(TAMANHO_POPULACAO_INICIAL)

    historico_populacional = []

    for geracao in range(2, MAX_GERACOES + 1):
        historico_populacional.append(populacao)

        ordenar_populacao(populacao)
        roleta = criar_roleta(populacao)

        pai, mae = roleta.selecionar(2)

        filhos = CROSS_OVER_STRATEGY.cross_over(pai, mae, geracao)

        populacao.extend(filhos)

    ordenar_populacao(populacao)

    for i in populacao:
        print(i)


if __name__ == '__main__':
    main()
