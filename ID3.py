import math

class id3 :

    def __init__(self,filas,columnas,tabla,etiquetas):
        self.filas = filas
        self.columnas = columnas
        self.tabla = tabla
        self.etiquetas = etiquetas
        self.entropia = 0

    def _calcularEntropia(self):
        cont = [] #array que cuenta la cantidad de cada etiqueta
        total = 0 #total de filas (pueden estar tachadas, por eso las contamos)
        atrDec = len(self.tabla[0])-1 #index del atributo de decision (el último atributo)
        et = self.etiquetas[atrDec] #etiquetas del atributo de decision
        for i in range(0, len(self.tabla)): #recorremos la ultima columna
            if self.filas[i]: #Si la fila no esta tachada
                index = et.index(self.tabla[i][atrDec]) 
                cont.insert(index,cont[index]+1)#incrementamos el numero de la etiqueta
                total += 1
        for i in range(0,len(cont)):
            self.entropia -= cont[i]/total*math.log2(cont[i]/total)  #aplicamos la formula de la entropia           