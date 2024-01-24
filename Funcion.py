from CRUD import CRUD
import json 
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
    

    
        
if __name__ == "__main__":
    from Funcion import Funcion
    from CRUD import CRUD
    funcion1 = Funcion(1, "08:10", "spiderman", "08/01/2024", "10:20", 70)
    funcion2 = Funcion(2, "08:10", "spiderman", "08/01/2024", "10:20", 70)
    
    crud = CRUD()
    funcion = Funcion()
    funcion.agregar(funcion1)
    funcion.agregar(funcion2)
    
    
    print("Json enviado")
    print(crud.read_json()) 
    
    
    print("Error en la clase")
    funcion.convert_to_object()
    