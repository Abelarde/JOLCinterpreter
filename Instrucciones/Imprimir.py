from enum import Enum
from Abstract.NodoAST import NodoAST
from TS.Tipo import TIPO, Instrucciones

class Imprimir(NodoAST):
    def __init__(self, salto, expresioness, fila, columna):
        self.salto = salto
        self.expresioness = expresioness
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
