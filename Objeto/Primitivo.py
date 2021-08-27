from Abstract.Objeto import Objeto
from abc import ABC, abstractmethod

# NOTE: alguna clase para manejar los que no sean primitivos?

class Primitivo(Objeto):
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def toString(self):
        return str(self.valor)

    def getValue(self):
        return self.valor

