class Buscador:
    def __init__(self,dato):
        self.lista=dato

    def recorrerelemento(self):
        for ele in self.lista:
            print(ele,end=" ")

        print("\n")

        for ele in self.lista[::-1]:
            print(ele,end=" ")

        print("\n")

        for pos,ele in enumerate(self.lista):
            print("[{}]= {}".format(pos,ele))

        print()

        for pos in range(len(self.lista)):
            print("[{}]= {}".format(pos,self.lista[pos]))

        print()

        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]= {}".format(pos,self.lista[pos]))

    def buscar(self,buscado):
        encontrado=False
        for pos, ele in enumerate(self.lista):
            if ele==buscado:
                encontrado=True
                break

        if encontrado:    return pos
        else:   return -1

datos=[2,3,1,5,8]  
bus = Buscador(datos)
# bus.recorrerElemento()    
# valor=5
# resp=bus.buscar(valor)
# if resp != -1: print("El numero {} se encuentra en la pocision '{}' de la lista {}".format(valor,resp,datos))
# else: print("El numero {} no se encuentra en la lista {}".format(valor,datos))
numerosbuscados=(2,4,6,1)
respuestas={}
for valor in numerosbuscados:
    resp=bus.buscar(valor)
    if resp !=-1: respuestas[valor]=resp
print(respuestas)
