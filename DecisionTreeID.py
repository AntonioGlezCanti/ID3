import csv
import ID3
import numpy as np

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = []
        self.filas = []
        self.columnas = []
        self.etiquetas = []

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS)
        self._obtenerEtiquetas()
        self.filas = np.ones(len(self.tabla))
        self.columnas = np.ones(len(self.tabla[0]))

    def drawDecisionTree(self):
        None
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        file = open(ficheroCSV)
        reader = csv.reader(file)
        for row in reader:
            self.tabla.append(row)

    def _obtenerEtiquetas (self):
        et = [] #array donde se almacenaran las etiquetas de cada columna
        for j in range(len(self.tabla[0])): #leemos por columnas la tabla
            for i in range(1,len(self.tabla)-1):
                val = self.tabla[i][j]
                if val not in et: #si es una etiqueta nueva la añadimos
                    et.append(val)
            self.etiquetas.append(et) #guardamos el conjunto de etiquetas junto a las demás
            et = []

    def _getAtributos(self):
        return self.filas,self.columnas,self.tabla,self.etiquetas

main = DecisionTreeID()
main.learnDT(r"C:\Users\gonza\Documents\Informática\Aprendizaje\ID3\ejemplo.csv")
f,c,t,e = main._getAtributos()
id3 = ID3.ID3(f,c,t,e)
print(id3._calcularEntropia())

