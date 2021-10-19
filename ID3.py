import math
import numpy as np

class ID3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.entropia = 0

    def _calcularEntropia(self):
        atrDec = len(self.tabla[0])-1 #index del atributo de decision (el último atributo)
        cont = self._obtenerRepeticiones(atrDec)
        total = sum(cont)
        for i in range(0,len(cont)):
            self.entropia -= cont[i]/total*math.log2(cont[i]/total)  #aplicamos la formula de la entropia           
        return self.entropia

    def _obtenerRepeticiones(self,atributo):
        et = self.etiquetas[atributo] #etiquetas del atributo de decision
        cont = np.zeros(len(et)) #array que cuenta la cantidad de cada etiqueta

        for i in range(1, len(self.tabla)): #recorremos la ultima columna
            if self.filas[i] == 1 : #Si la fila no esta tachada
                index = et.index(self.tabla[i][atributo]) 
                cont[index]+=1#incrementamos el numero de la etiqueta
        return(cont)

    def _calcularGanancia(self, atributo):
        cont = self._obtenerRepeticiones(atributo)
        
        