from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Instrucciones.BreakInstr import BreakInst
from Instrucciones.ReturnInstr import ReturnInstr
from TS.Excepcion import Excepcion, TipoError
from TS.TablaSimbolos import TablaSimbolos


class IfInstr(NodoAST):
    def __init__(self, tipo_if, condicion, instrucciones_if, instrucciones_else, instrucciones_else_if, fila, columna):
        self.tipo_if = tipo_if
        self.condicion = condicion
        self.instrucciones_if = instrucciones_if
        self.instrucciones_else = instrucciones_else
        self.instrucciones_else_if = instrucciones_else_if
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
            else:
                if self.instrucciones_else_if is not None:
                    for elsif in self.instrucciones_else_if:
                        result = elsif.interpretar(tree, table)
                        if isinstance(result, Excepcion): return result
                        if isinstance(result, BreakInst): return result
                        if isinstance(result, ReturnInstr): return result
                        if result: return None
                if self.instrucciones_else is not None:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.instrucciones_else:
                        result = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(result, Excepcion): return result
                        if isinstance(result, BreakInst): return result
                        if isinstance(result, ReturnInstr): return result
        else:
            return Excepcion(TipoError.SEMANTICO, f"Error, la condicion para la instruccion if no es de tipo bool",
                             self.fila, self.columna)

        return None

    def getNodo(self):
        return None


"""
println("Probando expresiones Arítmeticas, Booleanas y Lógicas");
if ((true == true && false != false) || true == false)
    println("No entra acá");
else
    println("Entra acá");
end;

if true == false
    println("No entra acá");
else
    println("Entra acá");
end;

if (1 == (1 + 1 - (1 * 2 / 2)) && 20.5 == 20.5)
    println("Entra acá");
else
    println("No entra acá");
end;

if "Hola" == "Mundo"
    println("No entra acá");
else
    println("Entra acá");
end;

if "Hola" == "Mundo"
    println("No entra acá");
elseif 4 == 3
    println("primer elseif");
elseif 4 == 5
    println("segundo elseif");
elseif 4 == 9
    println("tercer elseif");
else
    println("Entra acá");
end;
"""
