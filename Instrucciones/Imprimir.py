from enum import Enum
from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from TS.Excepcion import Excepcion
from TS.Tipo import Instrucciones

class Imprimir(NodoAST):
    def __init__(self, salto, expresioness, fila, columna):
        self.salto = salto
        self.expresioness = expresioness
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        for item in self.expresioness:
            value = item.interpretar(tree, table)   #NOTE:CLASE OBJETO
            if isinstance(value, Excepcion):
                continue
            tree.updateConsola(value.valor)  # TODO: Actualizar singleton en su campo consola
        return None


    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.IMPRIMIR)
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
