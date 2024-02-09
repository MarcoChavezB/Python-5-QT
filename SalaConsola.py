from ConsolaFuncion import ConsolaFuncion
from sala import Sala

class SalaConsola(Sala):
    def __init__(self):
        super().__init__()
        self.salas = Sala()
        self.consola = ConsolaFuncion() 
    
    def show(self):
        self.salas.show()
        

    def agg(self):
        funciones = self.consola.agg()
        sala1 = Sala(1, 100, "08:00", 100, funciones)
        return sala1
        
        
    def agregar(self):
        print("Cuantas sala desea agregar?")
        i = int(input())
        salas = []
        
        while i > 0:
            numero = input("Ingrese el número de la sala: ")
            num_asientos = input("Ingrese el número de asientos: ")
            hora_limpieza = input("Ingrese la hora de limpieza: ")
            max_personas = input("Ingrese el número máximo de personas: ")

            funciones = self.consola.agregar()

            sala = Sala(numero, int(num_asientos), hora_limpieza, int(max_personas), funciones)
            salas.append(sala)            
            self.salas.agregar(sala)
            i = i - 1
        return salas
    
    def eliminar (self):
        index = input("Ingrese el indice de la sala a eliminar: ")
        self.salas.eliminar(int(index))
    
    def modificar(self):
        index = input("Ingrese el indice de la sala a modificar: ")
        sala_modificar = self.salas.showIndex(int(index))
        
        if sala_modificar:
            print("Sala a modificar:")
            print(sala_modificar)
            print("Seleccione qué atributo desea modificar:")
            print("1. Número de la sala")
            print("2. Número de asientos")
            print("3. Hora de limpieza")
            print("4. Número máximo de personas")
            print("5. Funciones")
            
            opcion_modificar = input("Ingrese el número de la opción que desea modificar: ")
            
            if opcion_modificar == "1":
                sala_modificar.numero = input("Ingrese el nuevo número de la sala: ")
            elif opcion_modificar == "2":
                sala_modificar.num_asientos = input("Ingrese el nuevo número de asientos: ")
            elif opcion_modificar == "3":
                sala_modificar.hora_limpieza = input("Ingrese la nueva hora de limpieza: ")
            elif opcion_modificar == "4":
                sala_modificar.max_personas = input("Ingrese el nuevo número máximo de personas: ")
            elif opcion_modificar == "5":
                self.consola.modificar()
            else:
                print("Opción no válida. No se realizaron modificaciones.")
        else:
            print("No se encontró ninguna sala con ese ID.")
    
    
    
    def guardarJson(self):
        salas_info = []
        for s in self.salas.informacion:
            salas_info.append(s.to_dictionary())
        self.salas.save_json("json/salas.json", data=salas_info)
    
    
    
    
    def showJson(self):
        print(self.sala.read_json("json/salas.json"))

    def init_main(self, instancia):
        while True:
            print("1. Mostrar salas")
            print("2. Agregar sala")
            print("3. Eliminar sala")
            print("4. Modificar Objecto")
            print("5. Guardar Json")
            print("6. Mostrar Json")
            print("7. Convertir Json a objeto")
            opcion = input("Ingrese el número de la opción: ")
            
            if opcion == "1":
                print("Salas:")
                instancia.show()
            elif opcion == "2":
                instancia.agregar()
            elif opcion == "3":
                instancia.eliminar()
            elif opcion == "4":
                instancia.modificar()
            elif opcion == "5":
                instancia.guardarJson()
            elif opcion == "6":
                instancia.showJson()
            elif opcion == "7":
                instancia.isolate_objetos()
                
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    from SalaConsola import SalaConsola
    from sala import Sala
    consola  = SalaConsola()
    consola.init_main(consola)
    


    
        