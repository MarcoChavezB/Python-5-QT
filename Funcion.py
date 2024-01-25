from CRUD import CRUD
import json 
from cine import Cine
from sala import Sala

class Funcion(CRUD):
    def __init__(self, Nfuncion=None, hora_inicio=None, pelicula=None, fecha_estreno=None, hora_fin=None, costo_boleto=None):
        super().__init__()
        self.Nfuncion = Nfuncion
        self.hora_inicio = hora_inicio
        self.pelicula = pelicula
        self.fecha_estreno = fecha_estreno
        self.hora_fin = hora_fin
        self.costo_boleto = costo_boleto

    def __str__(self):
        if not self.informacion:
            return f"\nNfuncion: {self.Nfuncion}\nhora_inicio: {self.hora_inicio}\npelicula: {self.pelicula}\nfecha_estreno: {self.fecha_estreno}\nhora_fin: {self.hora_fin}\ncosto_boleto: {self.costo_boleto}"
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)

    def to_dictionary(self):
        if not self.informacion:  
            return {
                'Nfuncion': self.Nfuncion,
                'hora_inicio': self.hora_inicio,
                'pelicula': self.pelicula,
                'fecha_estreno': self.fecha_estreno,
                'hora_fin': self.hora_fin,
                'costo_boleto': self.costo_boleto
            }
        else: 
            return [funcion.to_dictionary() for funcion in self.funciones] if self.funciones else []
       
 
    def isolate_funcion_data(self):
        datos = self.read_json()
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            
            for dataSala in cine_data['salas']:
                sala = Sala()
                self.populate_object(sala, dataSala, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
                
                for dataFuncion in dataSala['funciones']:
                    funcion = Funcion()
                    self.populate_object(funcion, dataFuncion, ['Nfuncion', 'hora_inicio', 'pelicula', 'fecha_estreno', 'hora_fin', 'costo_boleto'])
                    self.informacion_iso.append(funcion)
        return self.informacion_iso  
    
    
    
    
    def process_all_data(self):
        datos = self.read_json()
        cine = Cine()
        sala = Sala()  
        funcion = Funcion()

        for cine_data in datos:
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)

            for dataSala in cine_data['salas']:
                self.populate_object(sala, dataSala, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
                self.informacion_iso.append(sala)

                for dataFuncion in dataSala['funciones']:
                    self.populate_object(funcion, dataFuncion, ['Nfuncion', 'hora_inicio', 'pelicula', 'fecha_estreno', 'hora_fin', 'costo_boleto'])
                    self.informacion_iso.append(funcion)

        return self.informacion_iso
    
    


    

    
    

if __name__ == "__main__":
    from Funcion import Funcion
    from sala import Sala
    from cine import Cine

    crud = CRUD()
    funcion = Funcion()

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
    funcion.process_all_data()
    funcion.show_isolate()
    