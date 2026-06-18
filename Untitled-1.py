def cargar_csv(csv):

    empleados = []

    try:

        with open(csv, "r") as archivo:

            lineas = archivo.readlines()

            for i in range(1, len(lineas)):

                linea = lineas[i].strip()
                datos = linea.split(",")

                empleado = {
                    "legajo": int(datos[0]),
                    "nombre": datos[1],
                    "diasdisponibles": int(datos[2])
                }

                empleados.append(empleado)

    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    except ValueError as e:
        print(f"ValueError: {e}")

    except IndexError:
        print("Error: Faltan columnas en el CSV")

    except Exception as e:
        print("Ocurrio el siguiente error: ", type(e).__name__)
        print(e)

    return empleados

            