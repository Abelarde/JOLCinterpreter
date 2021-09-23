from abc import ABC, abstractmethod     #modulo abc

"""
-Se pueden definir tanto atributos como funciones/metodos
-No pueden ser instanciadas
-Uso solamente para construir subclases [como una interfaz]
-Implementacion no necesaria de todos los metodos/funciones [abstractos]
-En la subclase implementar TODOS los METODOS ABSTRACTOS
-Evita duplicar codigo
-Obliga a cierta implementacion

-Sino hereda de ABC o no contiene almenos un metodo abstracto entonces si permite instanciar las clases Python

"""

class NodoAST(ABC):     #clase ABC
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()      #desde la subclase llamo a la implementacion del metodo de la clase abstracta ABC

    @abstractmethod     #decorador del modulo abc
    def interpretar(self, tree, table):
        pass

    @abstractmethod
    def getNodo(self):
        pass
