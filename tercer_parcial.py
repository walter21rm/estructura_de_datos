import os

class Persona:
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

class Autor(Persona):
    def __init__(self, cod_autor, pais, editorial, cod_persona, nombre, apellido_paterno, apellido_materno):
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

class Libro:
    def __init__(self, cod_libro, titulo, ano, tomo, cod_autor, cod_categoria):
        self.cod_libro = cod_libro
        self.titulo = titulo
        self.ano = ano
        self.tomo = tomo
        self.cod_autor = cod_autor
        self.cod_categoria = cod_categoria

class Libreria:
    def __init__(self):
        self.autores = []
        self.categorias = []
        self.libros = []

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def generar_reporte(self):
        for libro in self.libros:
            ruta_reporte = rf'C:\Users\walte\OneDrive\Documentos\libros\{libro.cod_libro}.txt'
            with open(ruta_reporte, 'w', encoding='utf-8') as file:
                file.write(f'Código del Libro: {libro.cod_libro}\n')
                file.write(f'Título del Libro: {libro.titulo}\n')
                file.write(f'Año del Libro: {libro.ano}\n')
                file.write(f'Tomo del Libro: {libro.tomo}\n')
                
                # Detalles del Autor
                autor = next((a for a in self.autores if a.cod_autor == libro.cod_autor), None)
                if autor:
                    file.write(f'Código del Autor: {autor.cod_autor}\n')
                    file.write(f'Nombre del Autor: {autor.nombre} {autor.apellido_paterno} {autor.apellido_materno}\n')
                    file.write(f'País del Autor: {autor.pais}\n')
                    file.write(f'Editorial del Autor: {autor.editorial}\n')
                
                # Detalles de la Categoría
                categoria = next((c for c in self.categorias if c.cod_categoria == libro.cod_categoria), None)
                if categoria:
                    file.write(f'Código de la Categoría: {categoria.cod_categoria}\n')
                    file.write(f'Nombre de la Categoría: {categoria.categoria}\n')

    def editar_libro(self, cod_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        for libro in self.libros:
            if libro.cod_libro == cod_libro:
                libro.titulo = nuevo_titulo
                libro.ano = nuevo_ano
                libro.tomo = nuevo_tomo
                ruta_reporte = rf'C:\Users\walte\OneDrive\Documentos\libros\{libro.cod_libro}.txt'
                with open(ruta_reporte, 'w', encoding='utf-8') as file:
                    file.write(f'Código del Libro: {libro.cod_libro}\n')
                    file.write(f'Título del Libro: {libro.titulo}\n')
                    file.write(f'Año del Libro: {libro.ano}\n')
                    file.write(f'Tomo del Libro: {libro.tomo}\n')
                    
                    # Detalles del Autor
                    autor = next((a for a in self.autores if a.cod_autor == libro.cod_autor), None)
                    if autor:
                        file.write(f'Código del Autor: {autor.cod_autor}\n')
                        file.write(f'Nombre del Autor: {autor.nombre} {autor.apellido_paterno} {autor.apellido_materno}\n')
                        file.write(f'País del Autor: {autor.pais}\n')
                        file.write(f'Editorial del Autor: {autor.editorial}\n')
                    
                    # Detalles de la Categoría
                    categoria = next((c for c in self.categorias if c.cod_categoria == libro.cod_categoria), None)
                    if categoria:
                        file.write(f'Código de la Categoría: {categoria.cod_categoria}\n')
                        file.write(f'Nombre de la Categoría: {categoria.categoria}\n')
                break

    def eliminar_libro(self, cod_libro):
        for libro in self.libros:
            if libro.cod_libro == cod_libro:
                ruta_reporte = rf'C:\Users\walte\OneDrive\Documentos\libros\{libro.cod_libro}.txt'
                if os.path.exists(ruta_reporte):
                    os.remove(ruta_reporte)
                self.libros.remove(libro)
                break

class Mantenimiento:
    def __init__(self):
        self.libreria = Libreria()

    def agregar_autor(self, autor):
        self.libreria.agregar_autor(autor)

    def agregar_categoria(self, categoria):
        self.libreria.agregar_categoria(categoria)

    def agregar_libro(self, libro):
        self.libreria.agregar_libro(libro)

    def generar_reporte(self):
        self.libreria.generar_reporte()

    def editar_libro(self, cod_libro, nuevo_titulo, nuevo_ano, nuevo_tomo):
        self.libreria.editar_libro(cod_libro, nuevo_titulo, nuevo_ano, nuevo_tomo)

    def eliminar_libro(self, cod_libro):
        self.libreria.eliminar_libro(cod_libro)

def menu_principal():
    mantenimiento = Mantenimiento()

    while True:
        print("\nMenú Principal:")
        print("1. Agregar Autor")
        print("2. Agregar Categoría")
        print("3. Agregar Libro")
        print("4. Generar Reporte")
        print("5. Editar Libro")
        print("6. Eliminar Libro")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cod_autor = int(input("Ingrese el código del autor: "))
            nombre_autor = input("Ingrese el nombre del autor: ")
            apellido_paterno_autor = input("Ingrese el apellido paterno del autor: ")
            apellido_materno_autor = input("Ingrese el apellido materno del autor: ")
            pais_autor = input("Ingrese el país del autor: ")
            editorial_autor = input("Ingrese la editorial del autor: ")

            autor = Autor(cod_autor, pais_autor, editorial_autor, cod_autor, nombre_autor, apellido_paterno_autor, apellido_materno_autor)
            mantenimiento.agregar_autor(autor)

        elif opcion == "2":
            cod_categoria = int(input("Ingrese el código de la categoría: "))
            nombre_categoria = input("Ingrese el nombre de la categoría: ")

            categoria = Categoria(cod_categoria, nombre_categoria)
            mantenimiento.agregar_categoria(categoria)

        elif opcion == "3":
            cod_libro = int(input("Ingrese el código del libro: "))
            titulo_libro = input("Ingrese el título del libro: ")
            ano_libro = int(input("Ingrese el año del libro: "))
            tomo_libro = int(input("Ingrese el tomo del libro: "))
            cod_autor_libro = int(input("Ingrese el código del autor del libro: "))
            cod_categoria_libro = int(input("Ingrese el código de la categoría del libro: "))

            libro = Libro(cod_libro, titulo_libro, ano_libro, tomo_libro, cod_autor_libro, cod_categoria_libro)
            mantenimiento.agregar_libro(libro)

        elif opcion == "4":
            mantenimiento.generar_reporte()
            print("Los reportes se han generado en C:\\Users\\walte\OneDrive\\Documentos\\libros")

        elif opcion == "5":
            cod_libro = int(input("Ingrese el código del libro que desea editar: "))
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_ano = int(input("Ingrese el nuevo año del libro: "))
            nuevo_tomo = int(input("Ingrese el nuevo tomo del libro: "))

            mantenimiento.editar_libro(cod_libro, nuevo_titulo, nuevo_ano, nuevo_tomo)
            print(f"El libro con código {cod_libro} se ha editado correctamente.")

        elif opcion == "6":
            cod_libro = int(input("Ingrese el código del libro que desea eliminar: "))
            mantenimiento.eliminar_libro(cod_libro)
            print(f"El libro con código {cod_libro} se ha eliminado correctamente.")

        elif opcion == "7":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()