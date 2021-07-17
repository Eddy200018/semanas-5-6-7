class Insertador:
    def __init__(self,dato):
        self.lista=dato

    def insertar(self,num):
        self.lista.sort()
        auxlista=[]
        auxlista2=[num]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break        
        if auxlista != []: self.lista=self.lista[0:pos]+auxlista +self.lista[pos:]
        else: self.lista=self.lista[0:]+auxlista2

    def insertar2(self,num):
        self.lista.sort()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)
        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista

    def insertarOrden(self,num):
        self.lista.append(num)
        self.lista.sort()

    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break
        if enc:self.lista=self.lista[0:pos]+self.lista[pos+1:]
        self.lista.sort()
        return enc

num=10
datos= [25,15,20,10]
insert = Insertador(datos)
insert.eliminar(num)
print(insert.lista)







class Ordenador:
    def __init__(self,dato):
        self.lista=dato

    def ordenarAsc(self):
        for pos in range(len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux= self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def ordenarDes(self):
        for pos in range(len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] < self.lista[sig]:
                    aux= self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primerEliminado(self):
        primero=self.lista[0]
        self.lista = self.lista[1:]
        return primero

    def primerEliminado2(self):
        primero=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primero

    def ultimo(self):
        return self.lista[-1]

    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        self.lista = self.lista[:-1]
        return ultimo

    def ultimoEliminado2(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return ultimo

    

datos = [25,15,20,10]
ord = Ordenador(datos)
print(ord.lista)