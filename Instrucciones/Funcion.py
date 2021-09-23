from Abstract.NodoAST import NodoAST
from Instrucciones.BreakInstr import BreakInst
from Instrucciones.ReturnInstr import ReturnInstr
from TS.Excepcion import Excepcion, TipoError
from TS.TablaSimbolos import TablaSimbolos


class Funcion(NodoAST):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()   # NOTE: entonces cas-sensitive o no
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table)

        for instruccion in self.instrucciones:      # REALIZAR LAS ACCIONES
            value = instruccion.interpretar(tree, nuevaTabla)
            if isinstance(value, Excepcion):
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
            if isinstance(value, BreakInst):
                err = Excepcion(TipoError.SEMANTICO, "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsola(err.toString())
            if isinstance(value, ReturnInstr):
                return value.result

        return None

    def getNodo(self):
        return None

