# VERSION MAS RECIENTE
import json
class CRUD:
    def __init__(self):
        self.informacion = []
        self.informacion_iso = []


    def agregar(self, instancia):
        if instancia == None:
            return False
        else:
            self.informacion.append(instancia)
            return True
    
    def show(self):
        for i in self.informacion:
            print(i)
            
    def show_isolate(self):
        for i in self.informacion_iso:
            print(i)
           

    def modificar(self, indice, instancia):
        if 0 <= indice < len(self.informacion):
            self.informacion[indice] = instancia
            return True
        else:
            return False

    def eliminar(self, indice):
        if 0 <= indice < len(self.informacion):
            del self.informacion[indice]
            return True
        else:
            return False
        
    def to_dictionary(self):
        if len(self.informacion) == 0:
            return []
        else:
            dict_list = [vars(elemento) for elemento in self.informacion]
            return dict_list
        
    def read_json(slef, json_data = "informacionJSON.json"):
        with open(json_data, 'r') as archivo:
            data = json.load(archivo)
            return data
        
    def save_to_json(self, filename="informacionJSON.json"):
        dict_list = [elemento.to_dictionary() for elemento in self.informacion]
        with open(filename, 'w') as archivo:
            json.dump(dict_list, archivo, indent=4)
            
            
    def format_isolate(self, lista):
        for i in lista:
            for clave, valor in i.items():
                print(f"{clave}: {valor}", end=", ")
        print()  
    print()
        
    def isolate_all_data(self):
        datos = self.read_json()
        result = []

        for cine_data in datos:
            cine_info = {
                'nombre': cine_data['nombre'],
                'ubicacion': cine_data['ubicacion'],
                'hora_apertura': cine_data['hora_apertura'],
                'hora_cierre': cine_data['hora_cierre'],
                'numplantas': cine_data['numplantas']
            }
            result.append(cine_info)

            salas = cine_data.get("salas", [])
            for sala in salas:
                sala_info = {
                    'numero': sala['numero'],
                    'num_asientos': sala['num_asientos'],
                    'hora_limpieza': sala['hora_limpieza'],
                    'max_personas': sala['max_personas']
                }
                result.append(sala_info)

                funciones = sala.get("funciones", [])
                for funcion in funciones:
                    funcion_info = {
                        'Nfuncion': funcion['Nfuncion'],
                        'hora_inicio': funcion['hora_inicio'],
                        'pelicula': funcion['pelicula'],
                        'fecha_estreno': funcion['fecha_estreno'],
                        'hora_fin': funcion['hora_fin'],
                        'costo_boleto': funcion['costo_boleto']
                    }
                    result.append(funcion_info)

        return self.format_isolate(result)



if __name__ == "__main__":
    from Funcion import Funcion
    from sala import Sala
    from cine import Cine

    crud = CRUD()

    funcion1 = Funcion(1, "08:10", "spiderman", "08/01/2024", "10:20", 70)
    funcion2 = Funcion(3, "10:10", "Superman", "10/01/2024", "12:20", 90)
    sala1 = Sala("b1", 150, "08:00", 200, [funcion1, funcion2])
    cine1 = Cine("Cinemex", "Torreon", "08:00", "22:00", [sala1], 3)


    funcion3 = Funcion(2, "09:30", "Avengers", "09/01/2024", "11:45", 80)
    funcion4 = Funcion(4, "12:00", "Batman", "11/01/2024", "14:15", 100)
    sala2 = Sala("c1", 120, "09:00", 180, [funcion3, funcion4])
    cine2 = Cine("Cinepolis", "Torreon", "08:30", "21:30", [sala2], 2)

    cines = Cine()
    cines.agregar(cine1)
    cines.agregar(cine2)
    cines.save_to_json()

    print("----------------All data----------------")
    print(cines.isolate_all_data())
    

