from CRUD import CRUD
class Cine(CRUD):
    def __init__(self, nombre=None, ubicacion=None, hora_apertura=None, hora_cierre=None, salas=None, numplantas=None):
        super().__init__()
        self.informacion = []
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.numplantas = numplantas
        self.salas = salas

    def __str__(self):
        if not self.informacion:
            salas_str = "\n".join([str(sala) for sala in self.salas]) if self.salas else ""
            return (
                f"\nnombre: {self.nombre}\n"
                f"ubicacion: {self.ubicacion}\n"
                f"hora_apertura: {self.hora_apertura}\n"
                f"hora_cierre: {self.hora_cierre}\n"
                f"numplantas: {self.numplantas}\n"
                f"salas: {salas_str}\n" 
            )
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)


    def to_dictionary(self):
        if not self.informacion:
            return {
                'nombre': self.nombre,
                'ubicacion': self.ubicacion,
                'hora_apertura': self.hora_apertura,
                'hora_cierre': self.hora_cierre,
                'numplantas': self.numplantas,
                'salas': [sala.to_dictionary() for sala in self.salas] if self.salas else None
            }
        else:
            return None
        
        
    def isolate_cine_data(self):
        datos = self.read_json()
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)
            
        
    def isolate_all_data(self):
        from sala import Sala
        from Funcion import Funcion

        datos = self.read_json()
        for cine_data in datos:
            cine = Cine()
            self.populate_object(cine, cine_data, ['nombre', 'ubicacion', 'hora_apertura', 'hora_cierre', 'numplantas'])
            self.informacion_iso.append(cine)
            
            for dataSala in cine_data['salas']:
                sala = Sala()
                self.populate_object(sala, dataSala, ['numero', 'num_asientos', 'hora_limpieza', 'max_personas'])
                self.informacion_iso.append(sala)
                
                for dataFuncion in dataSala['funciones']:
                    funcion = Funcion()
                    self.populate_object(funcion, dataFuncion, ['Nfuncion', 'hora_inicio', 'pelicula', 'fecha_estreno', 
                                                                'hora_fin', 'costo_boleto'])
                    self.informacion_iso.append(funcion)
                    
        return self.informacion_iso
    
    
    

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
    cines.isolate_all_data()
    cines.show_isolate()
    