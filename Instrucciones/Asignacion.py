from Abstract.NodoAST import NodoAST
from Abstract.Objeto import TipoObjeto
from Expresiones.Identificador import Identificador
from TS.Excepcion import Excepcion, TipoError
from TS.Simbolo import Simbolo
from TS.Tipo import Instrucciones


class Asignacion(NodoAST):
    def __init__(self, id, expresion, posiciones, tipo_instruccion, fila, columna):
        self.id = id
        self.expresion = expresion
        self.posiciones = posiciones
        self.tipo_instruccion = tipo_instruccion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.expresion is None:
            return Excepcion(TipoError.SEMANTICO, f"Error al obtener el valor de la asignacion", self.fila,
                             self.columna)

        valor = self.expresion.interpretar(tree, table)
        if valor.tipo == TipoObjeto.ERROR:
            return valor

        if self.tipo_instruccion == Instrucciones.ASIGNACION_ID:
            simbolo = Simbolo(self.id, self.fila, self.columna, valor)
            result = table.actualizarTabla(simbolo)  # actualiza o crea un nuevo simbolo
            if isinstance(result, Excepcion): return result
            return None
        elif self.tipo_instruccion == Instrucciones.ASIGNACION_ARREGLO:
            return None
        elif self.tipo_instruccion == Instrucciones.ASIGNACION_ACCESO:
            return None
        else:
            return Excepcion(TipoError.SEMANTICO, f"Error con el tipo de asignacion", self.fila, self.columna)

        return None

    def getNodo(self):
        return None


"""
a = 3;
b = "hola";
arreglo[1][2] = 4;
persona.datos.nombre = "soyyo";
"""
