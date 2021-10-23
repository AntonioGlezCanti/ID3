import math
import pandas.core.series as ser
import termcolor as tm

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
        self.ganancia = -1 #inicializamos a -1 ya que se puede dar el caso de que la ganancia sea 0, y en ese caso tendriamos que quedarnos con ella si es la primera
        self.nodo = None #Nodo seleccionado
        self.hijos = {}
        self.calcularNodo()

    """Calcula el nodo con mayor ganancia y lo guarda en la variable nodo"""
    def calcularNodo(self):
        print(self.tabla)
        self._calcularEntropia() #calculamos la entropia
        if(self.entropia == 0): #Si es igual a 0, significa que solo hay una etiqueta de decision en la columna, la sacamos y ese será el valor del nodo
            self.nodo = self.tabla.iloc[0][self.atrDec]
        else:
            for i in range(len(self.columnas)-1): #Calculamos la ganancia para cada atributo
                self._calcularGanancia(self.columnas[i]) 
            print(f'{self.nodo} -> {self.entropia} -> {self.ganancia}')
            self._crearHijos() #creamoos los hijos

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
    
    """Crea los hijos para el nodo seleccionado con anterioridad"""
    def _crearHijos(self):
        col = self.columnas.copy() #copiamos el array de columnas para pasarselo a los hijos, ya que si es una referencia dará problemas
        #print(f'{col} -> {self.nodo}')
        col.remove(self.nodo) #quitamos la columna del nodo
        for e in self.etiquetas.get(self.nodo): # para cada etiqueta del nodo
            fil = self.tabla[self.tabla[self.nodo] == e].index.to_list() #obtenemos las filas de cada etiqueta
            self.hijos.update({e:ID3(fil,col,self.tablaOriginal,self.etiquetas)}) #creamos el hijo, que ejecutará calcularNodo() y lo guardamos con la respectiva etiqueta
    
    def prediction(self,registroCSV):
        if not bool(self.hijos):
            return (f'{self.atrDec} : {self.nodo}')
        else:
            rama = registroCSV.get(self.nodo)
            return self.hijos.get(rama).prediction(registroCSV)

    def pintarArbol(self, nvl, listNvl):
        s = tm.colored(f'{self.nodo}\n','red')
        if bool(self.hijos):
            numHijos = len(self.hijos)
            listNvl.append(nvl)
            for rama, nodo in self.hijos.items():
                numHijos-=1;
                tab = self.tabuladores(nvl,listNvl)
                s += tm.colored( tab + f'----{rama}\n','cyan')
                if numHijos == 0: listNvl.remove(nvl)
                tab = self.tabuladores(nvl+1,listNvl)
                s +=  tm.colored(tab + f'|----> {nodo.pintarArbol(nvl+2,listNvl)}','cyan')
        return s
    
    def tabuladores(self,nvl,listNvl):
        s = ""
        for i in range(1, nvl+1):
            s+='\t'
            if i in listNvl: s += '|'
        return s