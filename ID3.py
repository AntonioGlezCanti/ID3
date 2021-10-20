import math
import numpy as np

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.atrDec = self.tabla.columns[len(self.tabla.columns)-1] 
        self.entropia = 0

    def _calcularEntropia(self):
        cont = self.tabla.groupby(self.atrDec)[self.atrDec].count().tolist()
        self.entropia = self._entropia(cont)
        return(self.entropia)
    
    def _calcularGanancia(self,index):
        entropias = []
        cont = []
        atributo = self.tabla.columns[index]
        etAtr = self.etiquetas[index]
        for et in etAtr:
            cont.append(self.tabla.groupby([self.atrDec,atributo])[atributo].count().tolist())
            print(self.tabla.groupby([self.atrDec,atributo])[atributo].count())
            entropias.append(self._entropia(cont[len(cont)-1]))
        print(entropias)
        print(cont)
        ganancia = self.entropia
        for i in range(len(cont)):
            ganancia = - sum(cont[i])/len(self.tabla)*entropias[i]
        return ganancia

    def _entropia(self, cont):
        entropia = 0
        total = sum(cont)
        for c in cont:
            entropia -= c/total*math.log2(c/total)  #aplicamos la formula de la entropia           
        return entropia
        
        