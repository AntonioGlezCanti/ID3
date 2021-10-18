import csv

class DecisionTreeID :
    
    def __init__(self):
        self.tabla = []
        self.filas = []
        self.columnas = []

    def learnDT(self,ficheroCVS):
        self._readCSV(ficheroCVS)
    
    def drawDecisionTree(self):
        None
    
    def prediction (self,registroCSV):
        None

    def _readCSV(self,ficheroCSV):
        file = open(ficheroCSV)
        reader = csv.reader(file)
        for row in reader:
            self.tabla.append(row)
        print(self.tabla)

    def _obtenerEtiquetas (self):
        et = [] #array donde se almacenaran las etiquetas de cada columna
        for j in range(len(self.tabla[0])-1): #leemos por columnas la tabla
            for i in range(1,len(self.tabla)-1):
                val = self.tabla[i][j]
                if val not in et: #si es una etiqueta nueva la añadimos
                    et.append(val)
            self.etiquetas.append(et) #guardamos el conjunto de etiquetas junto a las demás
            et = []
