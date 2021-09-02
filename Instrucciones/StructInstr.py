from Abstract.NodoAST import NodoAST


class StructInst(NodoAST):
    def __init__(self, mutable, identificador, struct_variables, fila, columna):
        self.mutable = mutable
        self.identificador = identificador
        self.struct_variables = struct_variables
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return None

    def getNodo(self):
        return None
