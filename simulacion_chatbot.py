def mostrar_menu(menu_items):
    while True:
        print("¡Hola! ¿En qué podemos ayudarte?")
        for i, item in enumerate(menu_items, start=1):
            print(f"{i}. {item[0]}")

        opcion = input("Seleccione la opción que más se corresponda:(Escriba 'Adios' para salir): ")

        if opcion == 'Adios':
            break

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(menu_items):
                submenu_items = menu_items[opcion - 1][1]
                mostrar_submenu(submenu_items)
            else:
                print("Opción no válida. Por favor, seleccione una opción de las ofrecidas.")
        except ValueError:
            print("Entrada no válida. Por favor, seleccione una opción de las ofrecidas.")
            # No sería necesario marcar errores o excepciones ya que podria tratarse de un menú de elección con botones donde no deban introducir ningun texto

def mostrar_submenu(submenu_items):
    while True:
        print("\nSubmenú:")
        for i, item in enumerate(submenu_items, start=1):
            print(f"{i}. {item[0]}")

        opcion = input("Dentro de esta categoría puede encontrar las siguientes subopciones (escriba 'Atras' para volver, 'Adios' para salir): ")

        if opcion == 'Atras':
            break
        elif opcion == 'Adios':
            exit()

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(submenu_items):
                # Muestra el texto asociado a la subopción seleccionada
                print(f"{submenu_items[opcion - 1][1]}")
            else:
                print("Subopción no válida. Por favor, seleccione una subopción de las ofrecidas.")
        except ValueError:
            print("Entrada no válida. Por favor, seleccione una subopción de las ofrecidas.")

if __name__ == "__main__":
    menu_items = [
        ("Problemas de Acceso", [
            ("Plataforma", "En caso de aparecer inactivo o credenciales incorrectas debe restablecer su clave, si por el contrario aparece bloqueado contacte con su gestor"),
            #En caso de haber una incidencia generalizada se podría indicar al seleccionar dicha opción donde suceda
            ("No veo mis clases grabadas", "Debe seleccionar un intervalo de fechas para ver todas las realizadas en ese periodo de tiempo"),
            ("Salas de informática", "En este caso debe acceder con las claves iniciales proporcionadas de su correo institucional"),
        ]),
        ("Problemas con las aulas", [
            ("No veo mis asignaturas", "Debe revisar en el calendario académico si ha llegado la fecha de inicio de las mismas, en caso afirmativo debe revisar que no se encuentren ocultas en su perfil"),
            ("Huella no puntúa", "Debe acceder a dicha tarea y antes de cerrar la pestaña hacer clic en la x de la esquina superior derecha"),
            ("No veo intervenciones de compañeros en foros", "Posiblemente no haya intervenciones ya que existen diferentes grupos"),
            ("No puedo subir mi actividad", "Revise que el nombre no es demasiado largo ni que contenga caracteres especiales"),
        ]),
        ("Examenes Online", [
            ("No veo donde realizar mi prueba de conectividad", "Una vez comienza el periodo de examenes se debe realizar desde la web de tablon de examenes"),
            ("No me aparece la opción de finalizar examen", "Posiblemente no haya hecho clic en el botón de subir archivo tras haberlo seleccionado"),
            ("Desconozco las fechas de mis examenes", "Puede encontrar la fecha de sus examenes en el calendario académico que se encuentra en el aula de información general"),
        ]),
        # Podría aumentarse con varios tipos de opciones y subopciones, tan solo he reflejado algunas de las comunes
    ]

    mostrar_menu(menu_items)