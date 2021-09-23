from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion, TipoError
from TS.Simbolo import Simbolo
from TS.TablaSimbolos import TablaSimbolos


class LlamadaFuncion(NodoAST):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre.lower())   # OBTENER LA FUNCION

        if result is None:  # NO SE ENCONTRO LA FUNCION
            return Excepcion(TipoError.SEMANTICO, "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)

        if result.parametros[0] is None:
            result.parametros.pop(0)

        # OBTENER PARAMETROS
        if len(result.parametros) != len(self.parametros): #LA CANTIDAD DE PARAMETROS ES LA ADECUADA
            return Excepcion(TipoError.SEMANTICO, "Cantidad de Parametros incorrecta.", self.fila, self.columna)

        nuevaTabla = TablaSimbolos(tree.getTSGlobal())
        contador = 0

        for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
            resultExpresion = expresion.interpretar(tree, table)
            if isinstance(resultExpresion, Excepcion): return resultExpresion
            simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), self.fila, self.columna, resultExpresion)
            resultTabla = nuevaTabla.setTabla(simbolo)
            if isinstance(resultTabla, Excepcion): return resultTabla
            contador += 1
        value = result.interpretar(tree, nuevaTabla)         # INTERPRETAR EL NODO FUNCION
        if isinstance(value, Excepcion): return value
        return value

    def getNodo(self):
        return None

"""
function hola (LISTA_PARAMETROS)
LISTA_INSTRUCCIONES
end;

function ejemplo()
x = 10;
println(x);
end;

ejemplo();

"""