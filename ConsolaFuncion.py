from Funcion import Funcion

# agagrrar la informacion del json al principio 
# pero tamvien ser capaz de enviar una funcion que se comporte como arreglo desde salas
# otra variable para cargar las funciones del json y mandarla a llamar ka diferencia es qie el archovo
# funciones le va a decir cargar json con un metodo 
# una para guardar las funciones del json y otra para guardar las funciones directamente de la lista 
# guardar una funcion dentro de las dfucniones serparar las funciones por variables

class ConsolaFuncion(Funcion):
    def __init__ (self):
        super().__init__()
        self.json_information = []
        self.funciones = Funcion()
        if not self.funciones.Nfuncion:
            self.json_information = self.funciones.read_json("json/funciones.json")
        
    
    
    def cargarJson (self):
        self.funciones = self.funciones.read_json("json/funciones.json")
        print("Datos cargados correctamente.")
    
    def show(self):
        self.funciones.show()
        
    
    def agregar(self):
        print("¿Cuántas funciones desea agregar?")
        i = int(input())
        funciones = []
        while i > 0:
            Nfuncion = input(f"Ingrese el número de la función {i}: ")
            hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
            pelicula = input("Ingrese el nombre de la película: ")
            fecha_estreno = input("Ingrese la fecha (DD/MM/YYYY): ")
            hora_fin = input("Ingrese la hora de fin (HH:MM): ")
            costo_boleto = input("Ingrese el precio: ")
            
            instancia = Funcion(int(Nfuncion), hora_inicio, pelicula, fecha_estreno, hora_fin, int(costo_boleto))
            funciones.append(instancia)
            self.funciones.agregar(instancia)
            
            i = i - 1

        return funciones


        
    def eliminar(self):
        id_eliminar = input("Ingrese el indice de la función a eliminar: ")
        self.funciones.eliminar(int(id_eliminar))


    def modificar(self):
        indice = input("Ingrese el indice de la función a modificar: ")
        funcion_modificar = self.funciones.showIndex(int(indice))
        
        if funcion_modificar:
            print("Función a modificar:")
            print(funcion_modificar)
            print("Seleccione qué atributo desea modificar:")
            print("1. Hora de inicio")
            print("2. Nombre de la película")
            print("3. Fecha")
            print("4. Hora de fin")
            print("5. Precio")
            

            opcion_modificar = input("Ingrese el número de la opción que desea modificar: ")

            if opcion_modificar == "1":
                funcion_modificar.hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ")
            elif opcion_modificar == "2":
                funcion_modificar.pelicula = input("Ingrese el nuevo nombre de la película: ")
            elif opcion_modificar == "3":
                funcion_modificar.fecha_estreno = input("Ingrese la nueva fecha (DD/MM/YYYY): ")
            elif opcion_modificar == "4":
                funcion_modificar.hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ")
            elif opcion_modificar == "5":
                funcion_modificar.costo_boleto = int(input("Ingrese el nuevo precio: "))
            else:
                print("Opción no válida. No se realizaron modificaciones.")
        else:
            print("No se encontró ninguna función con ese ID.")

    def guardarJson(self):
        funciones_info = [] 
        for f in self.funciones.informacion:
            funciones_info.append(f.to_dictionary())
        self.funciones.save_json("json/funciones.json", data=funciones_info)


        
    def showJson(self):
        print(self.funciones.read_json("json/funciones.json"))
        
    def isolate_objetos(self):
        data = self.funciones.read_json("json/funciones.json")
        self.funciones.isolate_objetos(data)
        for f in self.funciones.informacion_iso:
            self.funciones.agregar(f)
        
        
    def init_main(self, intancia):
        while True:
            print("1. Mostrar funciones")
            print("2. Agregar función")
            print("3. Eliminar función")
            print("4. Modificar función")
            print("5. Guardar en JSON")
            print("6. Leer JSON")
            print("7. Convertir a objeto")
            print("8. Salir")
            print("9. Limpiar pantalla")
            print("10. Cargar datos")
            opcion = input("Ingrese el número de la opción: ")
            
            if opcion == "1":
                print("Funciones:")
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
                intancia.showJson()
            elif opcion == "7":
                intancia.isolate_objetos()
            elif opcion == "8":
                break
            elif opcion == "9":
                os.system('cls')    
            elif opcion == "|":
                os.system('cls')

        
            
if __name__ == "__main__":
    import os
    consola = ConsolaFuncion()
    consola.init_main(consola)

