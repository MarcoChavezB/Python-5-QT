from SalaConsola import SalaConsola
from cine import Cine


class CineConsola(Cine):
    def __init__(self):
        super().__init__()
        self.cines = Cine()
        self.consola = SalaConsola()
        
    
    def show(self):
        self.cines.show()

    
    def agregar(self):
        nombre = input("Ingrese el nombre del cine: ")
        ubicacion = input("Ingrese la ubicación del cine: ")
        hora_apertura = input("Ingrese la hora de apertura del cine: ")
        hora_cierre = input("Ingrese la hora de cierre del cine: ")
        numplantas = input("Ingrese el número de plantas del cine: ")
        
        salas = self.consola.agregar()
    
        cine = Cine(nombre, ubicacion, hora_apertura, hora_cierre, salas, numplantas)
        
        self.cines.agregar(cine)
        
    def eliminar(self):
        print("Ingrese el indice del cine a eliminar: ")
        indice = int(input())
        self.cines.eliminar(indice)
        
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
                self.consola.modificar()
            else:
                print("Opción no válida. No se realizaron modificaciones.")
        else:
            print("No se encontró ningún cine con ese ID.")
            
            
            
            
    def guardarJson(self):
        cines_info = []
        for c in self.cines.informacion:
            cines_info.append(c.to_dictionary())
        self.cines.save_json("json/cines.json", data=cines_info)




    def showJson(self):
        print(self.cine.read_json("json/cines.json"))
        
    def init_main(self, intancia):
        while True:
            print("1. Agregar cine")
            print("2. Mostrar cines")
            print("3. Eliminar cine")
            print("4. Modificar cine")
            print("5. guardar json")
            print("6. mostrar json")
            print("5. agg")
            opcion = input("Ingrese el número de la opción: ")
            
            if opcion == "1":
                intancia.agregar()
            elif opcion == "2":
                intancia.show()
            elif opcion == "3":
                intancia.eliminar()
            elif opcion == "4":
                intancia.modificar()
            elif opcion == "5":
                intancia.guardarJson()
            elif opcion == "6":
                intancia.showJson()
            else:
                print("Opción no válida. Intente de nuevo.")    
            
            
            
        
                

if __name__ == "__main__":     
    from cine import Cine
    cine = CineConsola()
    cine.init_main(cine)
    
    
        
        
        