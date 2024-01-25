from CRUD import CRUD
from cine import Cine
class Sala(CRUD):
    def __init__(self, numero=None, num_asientos=None, hora_limpieza=None, max_personas=None, funciones=None):
        super().__init__()
        self.numero = numero
        self.num_asientos = num_asientos
        self.hora_limpieza = hora_limpieza
        self.max_personas = max_personas
        self.funciones = funciones

    def __str__(self):
        if not self.informacion:
            funciones_str = "\n".join([str(funcion) for funcion in self.funciones]) if self.funciones else "No hay funciones"
            return f"\nnumero: {self.numero},\nnum_asientos: {self.num_asientos},\nhora_limpieza: {self.hora_limpieza},\nmax_personas: {self.max_personas},\nfunciones: {funciones_str}"
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)

    def to_dictionary(self):
        if not self.informacion:
            return {
                'numero': self.numero,
                'num_asientos': self.num_asientos,
                'hora_limpieza': self.hora_limpieza,
                'max_personas': self.max_personas,
                'funciones': [funcion.to_dictionary() for funcion in self.funciones] if self.funciones else None
            }
        else:
            return None
        
    def isolate_cine_data(self):
        datos = self.read_json()    
        for cine_data in datos:
            cine = Cine()
            cine.nombre = cine_data['nombre']
            cine.ubicacion = cine_data['ubicacion']
            cine.hora_apertura = cine_data['hora_apertura']
            cine.hora_cierre = cine_data['hora_cierre']
            cine.numplantas = cine_data['numplantas']
            
            for data in cine_data['salas']:
                sala = Sala()
                sala.numero = data['numero']
                sala.num_asientos = data['num_asientos']
                sala.hora_limpieza = data['hora_limpieza']
                sala.max_personas = data['max_personas']
                self.informacion_iso.append(sala)
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
    
    print(sala1.isolate_cine_data())
