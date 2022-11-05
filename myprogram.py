

class Clase():
    alumnos = None
    aula = None
    profesor = None 
    asignaturas = None 

    def __init__(self, alumnos, aula, profesor, asignaturas):
        self.alumnos = alumnos
        self.aula = aula
        self.profesor = profesor
        self.asignaturas = asignaturas


    def add_alumno(self):
        # Juan
        pass
    
    def change_professor(self):
        # Adrian
        pass

    def remove_alumno(self):
        # Carmen
        pass

    def add_asignatura(self,asignatura):
        self.asignaturas.append(asignatura)

    def change_aula(self,mi_aula):
       self.aula = mi_aula
       return mi_aula
        