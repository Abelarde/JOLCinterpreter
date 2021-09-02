from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from TS.Excepcion import Excepcion


class Identificador(NodoAST):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())
        if simbolo is None:
            return Excepcion("SEMÁNTICO", " variable " + self.identificador + " no encontrada.", self.fila, self.columna)
        return simbolo.getValor()   # INSTANCIA DE LA CLASE OBJETO

    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.IDENTIFICADOR)
        nodo.agregarHijo(str(self.identificador))
        return nodo
