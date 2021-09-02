from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion

# CLASE PARA CONEXION CON LA GRAMATICA

class Constante(NodoAST):
    def __init__(self, valor, fila, columna):
        self.valor = valor  # Primitivo() # este sera una instancia de la clase OBJETO [NO = [O las clases que estaran en Objeto]]
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self.valor   # Primitivo()

    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.CONSTANTES)
        nodo.agregarhijo(str(self.valor))
        return nodo


