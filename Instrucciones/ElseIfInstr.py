from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Instrucciones.BreakInstr import BreakInst
from Instrucciones.ReturnInstr import ReturnInstr
from TS.Excepcion import Excepcion, TipoError
from TS.TablaSimbolos import TablaSimbolos


class ElseIfInstr(NodoAST):
    def __init__(self, condicion, instrucciones_if, fila, columna):
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if condicion.tipo == TipoObjeto.ERROR: return condicion

        if condicion.tipo == TipoObjeto.BOOL:
            if bool(condicion.valor):
                nuevaTabla = TablaSimbolos(table)
                for instruccion in self.instrucciones_if:
                    result = instruccion.interpretar(tree, nuevaTabla)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result, BreakInst): return result
                    if isinstance(result, ReturnInstr): return result
                return True
        else:
            return Excepcion(TipoError.SEMANTICO, f"Error, la condicion para la instruccion if no es de tipo bool",
                             self.fila, self.columna)

        return None

    def getNodo(self):
        return None
