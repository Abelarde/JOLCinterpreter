from Abstract.NodoAST import NodoAST


class ForInst(NodoAST):
    def __init__(self, identificador, condicion, instrucciones, fila, columna):
        self.identificador = identificador
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
