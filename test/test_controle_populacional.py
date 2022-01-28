from unittest import TestCase

from src.cromossomo import Cromossomo
from src.estrategias.populacao import ControlePopulacionalStrategy

strategy = ControlePopulacionalStrategy()


class TestRemoverCancerigeno(TestCase):
    def test_remover_se_geracao_passou(self):
        cromossomo_valido = Cromossomo(geracao=11, cancerigeno=True)
        cromossomo_invalido = Cromossomo(geracao=10, cancerigeno=True)

        populacao = [
            cromossomo_valido,
            cromossomo_invalido
        ]

        self.assertListEqual(
            [cromossomo_valido],
            strategy.remover_cancerigenos(populacao, 12)
        )

    def test_nao_remover_se_passar_da_geracao_porem_nao_cancerigeno(self):
        sem_cancer = Cromossomo(geracao=11, cancerigeno=True)

        populacao = [
            sem_cancer
        ]

        self.assertListEqual(
            [sem_cancer],
            strategy.remover_cancerigenos(populacao, 100)
        )


class TestControleLimitePopulacional(TestCase):
    def test_remover_somente_os_excedentes_ao_limite(self):
        permanece = Cromossomo(geracao=2)
        remove = Cromossomo(geracao=2)

        populacao = [
            permanece,
            remove
        ]

        self.assertListEqual(
            [permanece],
            strategy.controle_quantidade_populacao(populacao, 1)
        )

    def test_nao_remover_se_populacao_menor_que_limite(self):
        permanece = Cromossomo(geracao=2)
        remove = Cromossomo(geracao=2)

        populacao = [
            permanece,
            remove
        ]

        self.assertListEqual(
            populacao,
            strategy.controle_quantidade_populacao(populacao, 3)
        )
