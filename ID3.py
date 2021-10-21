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
        self.ganancia = -1
        self.nodo = None #Nodo seleccionado

    def calcularNodo(self):
        self._calcularEntropia()
        for i in range(len(self.tabla.columns)-1):
            self._calcularGanancia(self.tabla.columns[i])
        print(self.nodo)

    """Calculamos la entropia del nodo, es decir la general"""
    def _calcularEntropia(self):
        cont = self.tabla[self.atrDec].value_counts().tolist() #obtenemos la frecuencia de cada etiqueta
        self.entropia = self._entropia(cont) 

    """Calculamos la ganancia dado un atributo, que será de tipo String"""
    def _calcularGanancia(self,atributo):
        etAtr = self.etiquetas[atributo] #etiquetas del atributo para el que se desea calcular la ganancia
        cont = self.tabla.groupby([self.atrDec,atributo])[atributo].count() #agrupamos por atrDec y atributo, y contamos
        cont2 = self.tabla.groupby(atributo)[self.atrDec].count()
        g = self.entropia #inicializamos la ganancia
        nrow = len(self.tabla)
        
        for et in etAtr:
            val = []
            for ed in self.etDec:
                val.append(cont.get(ed,0).get(et,0)) #obtenemos la cantidad de la etiqueta correspondiente para cada etiqueta de atrDec                
            e = self._entropia(val) #calculamos la entropia
            g -= cont2[et]/nrow*e 
        if g > self.ganancia: #si la ganancia es mayor que la calculada anteriormente nos quedamos con ella
            self.ganancia = g
            self.nodo = atributo

    """Calculamos la entropia dado una lista de conteos"""
    def _entropia(self, cont):
        entropia = 0
        total = sum(cont)
        for c in cont:
            if c != 0:
                entropia -= c/total*math.log2(c/total)  #aplicamos la formula de la entropia           
        return entropia
        
        
