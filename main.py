import random
import math
from Populacao import Populacao

TAMANHO_INDIVIDUO = 4
TAMANHO_POPULACAO = 2

populacao = Populacao(TAMANHO_POPULACAO, TAMANHO_INDIVIDUO)
populacao.gerarPopulacao()
populacao.calcularFitness()
populacao.fazerMutacao()
print ("hello word")
