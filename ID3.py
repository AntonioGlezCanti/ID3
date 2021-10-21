import math
import numpy as np
import pandas as pd
import pandas.core.series as ser

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.tablaOriginal = tabla
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla.loc[filas,columnas]
        self.etiquetas = etiquetas
        self.atrDec = self.tabla.columns[len(self.tabla.columns)-1] #atributo de decision
        self.etDec = self.etiquetas[self.atrDec] #etiquetas del atributo de decision
        self.entropia = 0
        self.ganancia = -1
        self.nodo = None #Nodo seleccionado
        self.hijos = {}
        self.calcularNodo()
        #print(self.tabla)

    def _crearHijos(self):
        if self.entropia != 0:
            print(self.nodo)
            col = self.columnas
            col.remove(self.nodo)
            for e in self.etiquetas.get(self.nodo):
                fil = self.tabla[self.tabla[self.nodo] == e].index.to_list()
                self.hijos.update({e:ID3(fil,col,self.tablaOriginal,self.etiquetas)})
            print(self.hijos)

    """Calcula el nodo con mayor ganancia y lo guarda en la variable nodo"""
    def calcularNodo(self):
        self._calcularEntropia()
        for i in range(len(self.columnas)-1):
            self._calcularGanancia(self.columnas[i])
        if(self.entropia == 0):
            self.nodo = self.tabla.iloc[0][self.atrDec]

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
                val.append(cont.get(ed,ser.Series([])).get(et,0)) #obtenemos la cantidad de la etiqueta correspondiente para cada etiqueta de atrDec                
            e = self._entropia(val) #calculamos la entropia
            g -= cont2.get(et,0)/nrow*e 
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
        
    def __repr__(self):
        return self.nodo
