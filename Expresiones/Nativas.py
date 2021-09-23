import math

from Abstract.NodoAST import NodoAST
from Abstract.NodoReporteArbol import NodoReporteArbol, Expresion
from Abstract.Objeto import TipoObjeto
from Objeto.Primitivo import Primitivo
from TS.Excepcion import Excepcion, TipoError
from TS.Tipo import FuncionesPrimitivas

# TODO: manejar el try catch tambien para los errores
# TODO: podria tambien ir saliendo asi con los erroes pero tambien de la manera en la que lo manejo

class Nativas(NodoAST):
    def __init__(self, funcion_nativa, expresion_uno, expresion_dos, tipo_dato, fila, columna):
        self.funcion_nativa = funcion_nativa
        self.expresion_uno = expresion_uno
        self.expresion_dos = expresion_dos
        self.tipo_dato = tipo_dato
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        res_uno = self.expresion_uno.interpretar(tree, table)

        if res_uno.tipo == TipoObjeto.ERROR:
            return res_uno

        res_dos = None
        if self.expresion_dos is not None:
            res_dos = self.expresion_dos.interpretar(tree, table)
            if res_dos.tipo == TipoObjeto.ERROR:
                return res_dos

        # TODO: validaciones o try except: https://www.geeksforgeeks.org/python-math-function-sqrt/

        if self.funcion_nativa == FuncionesPrimitivas.SQRT:
            return Primitivo(TipoObjeto.FLOAT64, math.sqrt(float(str(res_uno.getValue()))))

        elif self.funcion_nativa == FuncionesPrimitivas.TAN:
            return Primitivo(TipoObjeto.FLOAT64, math.tan(float(str(res_uno.getValue()))))

        elif self.funcion_nativa == FuncionesPrimitivas.COS:
            return Primitivo(TipoObjeto.FLOAT64, math.cos(float(str(res_uno.getValue()))))

        elif self.funcion_nativa == FuncionesPrimitivas.SIN:
            return Primitivo(TipoObjeto.FLOAT64, math.sin(float(str(res_uno.getValue()))))

        elif self.funcion_nativa == FuncionesPrimitivas.LOG:
            if res_dos is not None:
                return Primitivo(TipoObjeto.FLOAT64, math.log(float(str(res_uno.getValue())), float(str(res_dos.getValue()))))
            else:
                return Excepcion(TipoError.SEMANTICO, f"Falta un parametro para ejecutar la funcion nativa", self.fila, self.columna)

        elif self.funcion_nativa == FuncionesPrimitivas.LOG10:
            return Primitivo(TipoObjeto.FLOAT64, math.log10(float(str(res_uno.getValue()))))

        elif self.funcion_nativa == FuncionesPrimitivas.PARSE:
            if self.tipo_dato == TipoObjeto.FLOAT64:
                return Primitivo(TipoObjeto.FLOAT64, float(str(res_uno.getValue())))
            elif self.tipo_dato == TipoObjeto.INT64:
                return Primitivo(TipoObjeto.INT64, int(str(res_uno.getValue())))

        elif self.funcion_nativa == FuncionesPrimitivas.TRUNC:
            if self.tipo_dato == TipoObjeto.INT64:
                return Primitivo(TipoObjeto.INT64, int(str(res_uno.getValue())))

        elif self.funcion_nativa == FuncionesPrimitivas.FLOAT:
            return Primitivo(TipoObjeto.FLOAT64, float(str(res_uno.getValue())))

        elif self.funcion_nativa == FuncionesPrimitivas.STRING:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()))

        elif self.funcion_nativa == FuncionesPrimitivas.TYPEOF:
            a = res_uno.getTipo().split('.')
            if len(a) == 2:
                return Primitivo(TipoObjeto.STRING, a[1])
            else:
                return Excepcion(TipoError.SEMANTICO, f"Error al obtener el tipo de dato", self.fila, self.columna);

        elif self.funcion_nativa == FuncionesPrimitivas.UPPERCASE:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()).upper())

        elif self.funcion_nativa == FuncionesPrimitivas.LOWERCASE:
            return Primitivo(TipoObjeto.STRING, str(res_uno.getValue()).lower())

        return Excepcion(TipoError.SEMANTICO, f"Funcion nativa desconocida: {self.funcion_nativa}", self.fila, self.columna);

    def getNodo(self):
        nodo = NodoReporteArbol(Expresion.NATIVA)

        nodo.agregarHijoNodo(self.funcion_nativa)
        nodo.agregarHijoNodo(self.expresion_uno.getNodo())

        if self.expresion_dos is not None:
            nodo.agregarHijoNodo(self.expresion_dos.getNodo())
        elif self.tipo_dato is not None:
            nodo.agregarHijoNodo(self.tipo_dato)
        return nodo

        """
                if self.funcion_nativa == FuncionesPrimitivas.PUSH:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))

                if self.funcion_nativa == FuncionesPrimitivas.POP:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))

                if self.funcion_nativa == FuncionesPrimitivas.LENGTH:
                    return Primitivo(TipoObjeto.FLOAT64, math.sqrt(int(str(res_uno.getValue()))))
        """
