from CRUD import CRUD
from Funcion import Funcion
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
    
