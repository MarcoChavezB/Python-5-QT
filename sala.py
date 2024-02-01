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
            funciones_str = "\n".join([str(funcion) for funcion in self.funciones]) if self.funciones else ""
            return (
                f"numero: {self.numero},\n"
                f"num_asientos: {self.num_asientos},\n"
                f"hora_limpieza: {self.hora_limpieza},\n"
                f"max_personas: {self.max_personas},\n\n"
                f"funciones: {funciones_str}"
            )
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
        
    def isolate_objetos(self,data):
        for d in data:
            funciones = Funcion()
            funciones.isolate_funciones_objetos(d["funciones"])
            d["funciones"]=funciones
            sala = Sala(numero=d["numero"],num_asientos=d["num_asientos"],hora_limpieza=d["hora_limpieza"],max_personas=d["max_personas"],funciones=d["funciones"])
            self.informacion_iso.append(sala)