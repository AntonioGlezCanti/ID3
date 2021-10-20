import math
import numpy as np

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.atrDec = self.tabla.columns[len(self.tabla.columns)-1] #atributo de decision
        self.etDec = self.etiquetas[self.atrDec] #etiquetas del atributo de decision
        self.entropia = 0
        self.ganancias = {}

    def calcularNodo(self):
        self._calcularEntropia()
        for i in range(len(self.tabla.columns)-1):
            self._calcularGanancia(self.tabla.columns[i])
        print(self.ganancias)


    """Calculamos la entropia del nodo, es decir la general"""
    def _calcularEntropia(self):
        cont = self.tabla[self.atrDec].value_counts().tolist() #obtenemos la frecuencia de cada etiqueta
        self.entropia = self._entropia(cont) 

    """Calculamos la ganancia dado un atributo, que será de tipo String"""
    def _calcularGanancia(self,atributo):
        entropias = {} #diccionario auxiliar para guardar la entropias de cada etiqueta
        etAtr = self.etiquetas[atributo] #etiquetas del atributo para el que se desea calcular la ganancia
        cont = self.tabla.groupby([self.atrDec,atributo])[atributo].count() #agrupamos por atrDec y atributo, y contamos
        for et in etAtr:
            val = []
            for ed in self.etDec:
                val.append(cont.get(ed,0).get(et,0)) #obtenemos la cantidad de la etiqueta correspondiente para cada etiqueta de atrDec                
            e = self._entropia(val) #calculamos la entropia
            entropias.update({et:e}) #la almacenamos
        ganancia = self.entropia #inicializamos la ganancia
        cont = self.tabla.groupby(atributo)[self.atrDec].count() #agrupamos por atributo de modo que obtenemos la cantidad que hay de cada etiqueta
        for et in etAtr:
            ganancia -= cont[et]/len(self.tabla)*entropias[et] #aplicamos la formula de la ganancia
        self.ganancias.update({atributo:ganancia}) #almacenamos la ganancia

    """Calculamos la entropia dado una lista de conteos"""
    def _entropia(self, cont):
        entropia = 0
        total = sum(cont)
        for c in cont:
            if c != 0:
                entropia -= c/total*math.log2(c/total)  #aplicamos la formula de la entropia           
        return entropia
        
        