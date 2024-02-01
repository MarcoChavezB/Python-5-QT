from CRUD import CRUD


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
            return (
                f"\nNfuncion: {self.Nfuncion}\n"
                f"hora_inicio: {self.hora_inicio}\n"
                f"pelicula: {self.pelicula}\n"
                f"fecha_estreno: {self.fecha_estreno}\n"
                f"hora_fin: {self.hora_fin}\n"
                f"costo_boleto: {self.costo_boleto}"
            )
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)
        
    # def to_dictionary(self):
    #     if not self.informacion:  
    #         return {
    #             'Nfuncion': self.Nfuncion,
    #             'hora_inicio': self.hora_inicio,
    #             'pelicula': self.pelicula,
    #             'fecha_estreno': self.fecha_estreno,
    #             'hora_fin': self.hora_fin,
    #             'costo_boleto': self.costo_boleto
    #         }
    #     else: 
    #         return [funcion.to_dictionary() for funcion in self.funciones] if self.funciones else []
        
    
    # def isolate_objetos(self,data):
    #     from CRUD import CRUD
    #     crud = CRUD()
    #     for dataFuncion in data:
    #         funcion = Funcion()
    #         funcion.Nfuncion = dataFuncion['Nfuncion']
    #         funcion.hora_inicio = dataFuncion['hora_inicio']
    #         funcion.pelicula = dataFuncion['pelicula']
    #         funcion.fecha_estreno = dataFuncion['fecha_estreno']
    #         funcion.hora_fin = dataFuncion['hora_fin']
    #         funcion.costo_boleto = dataFuncion['costo_boleto']
    #         self.informacion_iso.append(funcion)
    #         print(crud.to_dictionary())
    #         crud.agregar(funcion)
    #         funcion.save_json("json/funciones.json",data=crud.to_dictionary())
            # Modifica la función to_dictionary en la clase Funcion
# Modifica la función to_dictionary en la clase Funcion
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

    def populate_object(self, objeto, datos, atributos):
        for atributo in atributos:
            if atributo in datos:
                setattr(objeto, atributo, datos[atributo])

    def isolate_objetos(self,data):
        from CRUD import CRUD
        crud = CRUD()
        for dataFuncion in data:
            funcion = Funcion()
            funcion.Nfuncion = dataFuncion['Nfuncion']
            funcion.hora_inicio = dataFuncion['hora_inicio']
            funcion.pelicula = dataFuncion['pelicula']
            funcion.fecha_estreno = dataFuncion['fecha_estreno']
            funcion.hora_fin = dataFuncion['hora_fin']
            funcion.costo_boleto = dataFuncion['costo_boleto']
            self.informacion_iso.append(funcion)
            print(crud.to_dictionary())
            crud.agregar(funcion)
            funcion.save_json("json/funciones.json",data=crud.to_dictionary())

if __name__ == "__main__":
    from Funcion import Funcion
    from CRUD import CRUD
    
    crud = CRUD()
        
    funcion1 = Funcion(2, "08:10", "Spiderman", "08/01/2024", "10:20", 70)
    funcion2 = Funcion(3, "10:10", "Superman", "10/01/2024", "12:20", 90)

    funciones=Funcion()
    crud.agregar(funcion1)
    crud.agregar(funcion2)
    crud.save_json("json/funciones.json", data=crud.to_dictionary())
    
    datos = funciones.read_json("json/funciones.json")
    funciones.isolate_objetos(datos)
    # for c in funciones.informacion_iso:
    #     print(type(c))

                
