from enum import Enum


# CLASE PARA REPORTE DEL AST

class NodoReporteArbol():
    def __init__(self, valor):
        self.hijos = []
        self.valor = valor

    def setHijos(self, hijos):
        self.hijos = hijos

    def agregarHijo(self, valorHijo):
        self.hijos.append(NodoReporteArbol(valorHijo))

    def agregarHijos(self, hijos):
        for hijo in hijos:
            self.hijos.append(hijo)

    def agregarHijoNodo(self, hijo):
        self.hijos.append(hijo)

    def agregarPrimerHijo(self, valorHijo):
        self.hijos.insert(0, NodoReporteArbol(valorHijo))

    def agregarPrimerHijoNodo(self, hijo):
        self.hijos.insert(0, hijo)

    def getValor(self):
        return str(self.valor)

    def setValor(self, valor):
        self.valor = valor

    def getHijos(self):
        return self.hijos


# TIPOS DE EXPRESIONES
class Expresion(Enum):
    CONSTANTES = 1
    IDENTIFICADOR = 2
    ARITMETICA = 3
    LOGICA = 4
    RELACIONAL = 5
    NATIVA = 6
    IMPRIMIR = 7
