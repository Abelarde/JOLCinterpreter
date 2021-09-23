from Abstract.Objeto import Objeto
from abc import ABC, abstractmethod


class Primitivo(Objeto):
    def __init__(self, tipo, valor):
        self.tipo = tipo    # NOTE:TIPO CRUDO
        self.valor = valor  # NOTE:VALOR CRUDO

    def toString(self):
        return str(self.valor)

    def getValue(self):
        return self.valor

    def getTipo(self):
        return str(self.tipo)
