from Funcion import Funcion

class ConsolaFuncion():
    def __init__ (self, useJson=True):
        super().__init__()
        if useJson:
            self.funciones = Funcion()
            self.useJson = useJson
            self.init_Json()
        else:
            self.funciones = Funcion()
        
        
    def init_Json(self):
        data = self.funciones.read_json("json/funciones.json")
        for d in data:
            funcion = Funcion(d['Nfuncion'], d['hora_inicio'], d['pelicula'], d['fecha_estreno'], d['hora_fin'], d['costo_boleto'])
            self.funciones.agregar(funcion)
        return self.informacion
    
    def mostrar(self):
        self.funciones.show()
        
    
    def add(self):
        print("¿Cuántas funciones desea agregar?")
        i = int(input())
        while i > 0:
            Nfuncion = input(f"Ingrese el número de la función {i}: ")
            hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
            pelicula = input("Ingrese el nombre de la película: ")
            fecha_estreno = input("Ingrese la fecha (DD/MM/YYYY): ")
            hora_fin = input("Ingrese la hora de fin (HH:MM): ")
            costo_boleto = input("Ingrese el precio: ")
            
            #cambio
            instancia = Funcion(int(Nfuncion), hora_inicio, pelicula, fecha_estreno, hora_fin, int(costo_boleto))
            self.funciones.agregar(instancia)
            
            if self.useJson:
                self.guardarJson()
            
            i = i - 1
        return self.funciones


    def eliminar(self):
        id_eliminar = input("Ingrese el indice de la función a eliminar: ")
        self.funciones.eliminar(int(id_eliminar))
        if self.useJson:
            self.guardarJson()


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
        if self.useJson:
            self.guardarJson()



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
            print("\n--------------------------\n Menu Funciones \n --------------------------")
            print("1. Mostrar")
            print("2. Agregar")
            print("3. Eliminar")
            print("4. Modificar")
            print("5. Guardar en JSON")
            print("6. Leer JSON")
            opcion = input("Ingrese el número de la opción: ")
            print("---------------------------")
            
            if opcion == "1":
                print("Funciones:")
                intancia.mostrar()
            elif opcion == "2":
                intancia.add()
            elif opcion == "3":
                intancia.eliminar()
            elif opcion == "4":
                intancia.modificar()
            elif opcion == "5":
                intancia.guardarJson()
            elif opcion == "6":
                intancia.showJson()

        
            
if __name__ == "__main__":
    import os
    consola = ConsolaFuncion()
    consola.init_main(consola)

