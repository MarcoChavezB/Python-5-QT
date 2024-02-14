from SalaConsola import SalaConsola
from cine import Cine
from sala import Sala 
from MongoDBManager import MongoDBManager

class CineConsola(Cine):
    def __init__(self, useJson=True):
        super().__init__()        
        self.cines = Cine()
        self.useJson = useJson
        
        if useJson:
            self.init_Json()
            
    
    def init_Json(self):
        self.cines.isolate_objetos(self.cines.read_json(json_data="json/cines.json"))
    
    
    def show(self):
        self.cines.show()


    def agregar(self):
        nombre = input("Ingrese el nombre del cine: ")
        ubicacion = input("Ingrese la ubicación del cine: ")
        hora_apertura = input("Ingrese la hora de apertura del cine: ")
        hora_cierre = input("Ingrese la hora de cierre del cine: ")
        numplantas = input("Ingrese el número de plantas del cine: ")
        print(numplantas)
        
        consola = SalaConsola(useJson=False)
        sala = consola.add()
        cine = Cine(nombre, ubicacion, hora_apertura, hora_cierre, sala, numplantas)
        self.cines.agregar(cine)
        
        if self.useJson:
            self.guardarJson()
        
    def eliminar(self):
        print("Ingrese el indice del cine a eliminar: ")
        indice = int(input())
        self.cines.eliminar(indice)
        
        if self.useJson:
            self.guardarJson()
        
    def modificar(self):
        print("Ingrese el indice del cine a modificar: ")
        indice = int(input())
        cine_modificar = self.cines.showIndex(indice)

        if cine_modificar:
            print("Cine a modificar:")
            print(cine_modificar)
            print("Seleccione qué atributo desea modificar:")
            print("1. Nombre del cine")
            print("2. Ubicación del cine")
            print("3. Hora de apertura")
            print("4. Hora de cierre")
            print("5. Número de plantas")
            print("6. Salas")

            
            opcion_modificar = input("Ingrese el número de la opción que desea modificar: ")
            
            if opcion_modificar == "1":
                cine_modificar.nombre = input("Ingrese el nuevo nombre del cine: ")
            elif opcion_modificar == "2":
                cine_modificar.ubicacion = input("Ingrese la nueva ubicación del cine: ")
            elif opcion_modificar == "3":
                cine_modificar.hora_apertura = input("Ingrese la nueva hora de apertura del cine: ")
            elif opcion_modificar == "4":
                cine_modificar.hora_cierre = input("Ingrese la nueva hora de cierre del cine: ")
            elif opcion_modificar == "5":
                cine_modificar.numplantas = input("Ingrese el nuevo número de plantas del cine: ")
            elif opcion_modificar == "6":
                
                consola = SalaConsola(useJson=False)
                consola.salas = cine_modificar.salas
                consola.init_main()
                self.cines.modificar(indice, cine_modificar)
                
            else:
                print("Opción no válida. No se realizaron modificaciones.")
        else:
            print("No se encontró ningún cine con ese ID.")
            
        if self.useJson:
            self.guardarJson()
            
            
            
    def guardarJson(self):
        cines_info = []
        for c in self.cines.informacion:
            cines_info.append(c.to_dictionary())
        self.cines.save_json("json/cines.json", data=cines_info)

    def showJson(self):
        print(self.cine.read_json("json/cines.json"))
        
        
        
        
        
    def guardarMongoDB(self):
        data = self.cines.read_json("json/cines.json")
        mongo = MongoDBManager(collection_name="cines")
        mongo.insert(data)
        
        
        
        
        
    def init_main(self, intancia):
        while True:
            print("\n--------------------------\n Menu Cine \n --------------------------")
            print("1. Mostrar")
            print("2. Agregar")
            print("3. Eliminar")
            print("4. Modificar")
            print("5. Guardar Json")
            print("6. Guardar MongoDB")
            opcion = input("Ingrese el número de la opción: ")
            print("---------------------------")
            
            if opcion == "1":
                intancia.show()
            elif opcion == "2":
                intancia.agregar()
            elif opcion == "3":
                intancia.eliminar()
            elif opcion == "4":
                intancia.modificar()
            elif opcion == "5":
                intancia.guardarJson()
            elif opcion == "6":
                intancia.guardarMongoDB()
            else:
                print("Opción no válida. Intente de nuevo.")    
            
        
                

if __name__ == "__main__":     
    from cine import Cine
    cine = CineConsola()
    cine.init_main(cine)
    
    
        
        
        