from src.cromossomo import Cromossomo
from src.aleatorio import Roleta, ElementoRoleta
from .fitness import FitnessStrategy


def criar_cromossomo(*args, **kwargs):
    """
    Cria um cromosso e já atribui o valor fitness utilizando
    o strategy de fitness para o cálculo.
    """
    cromossomo = Cromossomo(*args, **kwargs)
    cromossomo.fitness = FitnessStrategy().calcular(cromossomo.genes)
    cromossomo.fitness_a = FitnessStrategy().calcular_a(cromossomo.genes)
    return cromossomo


def criar_roleta_equilibrada(conjunto) -> Roleta:
    """
    Cria uma roleta com os pesos iguais para todos o elementos, de modo que
    todos terão a mesma probabilidade de ser sorteado.
    """
    elemetos_roleta = (
        ElementoRoleta(elemento=elemento, probablidade=1)
        for elemento in conjunto
    )

    return Roleta(*elemetos_roleta)
