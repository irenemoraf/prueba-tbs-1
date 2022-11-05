

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


    def add_alumno(self, alumno):
         # Juan
        '''
        Añade un alumno al listado existente.
        '''
        self.alumnos.append(alumno)

    
    def change_professor(self, profesor):
        self.profesor = profesor

        # Adrian

    def remove_alumno(self,alumno):

        self.alumno.remove(alumno)
        # Carmen
        return self.alumno

    def add_asignatura(self,asignatura):
        self.asignaturas.append(asignatura)

    def change_aula(self,mi_aula):
       self.aula = mi_aula
       return mi_aula
        

c1 = Clase()
print(f'Alumnos: {c1.alumnos}')
print(f'Aula: {c1.aula}')
print(f'Profesor: {c1.profesor}')
print(f'Asignaturas:{ c1.asignaturas}')


c2 = Clase(alumnos=['Adrian','Pedro','Luis'],aula='C15',profesor="Layton",asignaturas=["Programacion1","Programacion2"])
print(f'Alumnos: {c2.alumnos}')
print(f'Aula: {c2.aula}')
print(f'Profesor: {c2.profesor}')
print(f'Asignaturas:{ c2.asignaturas}')

c2.add_alumno('Manuel')
print(f'Alumnos: {c2.alumnos}')

c2.change_professor('Maria')
print(f'Profesor: {c2.profesor}')

c2.remove_alumno('Pedro')
print(f'Alumnos: {c2.alumnos}')

c2.add_asignatura('Programacion3')
print(f'Asignaturas:{ c2.asignaturas}')

c2.change_aula('B14')
print(f'Aula: {c2.aula}')
