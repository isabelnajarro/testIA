
fichero = "mi_archivo.txt"

try:
    with open(fichero, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró")
    with open(fichero, "w") as archivo:
        archivo.write("ABCDEFGHIKLMNOPQRSTUVWXYZ\n")
        archivo.write("1234567890\n")
        archivo.write("¡!¿?\n")
        archivo.write("+-*/\n")
        archivo.write(".,:;-_\n")
    print("Archivo creado")
    archivo.close()

# Abre el archivo en modo lectura y lee cada línea
with open(fichero, "r") as archivo_lectura:
    # Muestra cada línea y la posición actual del cursor
    print("\nContenido del archivo:")
    print("\n".join(f"Línea {num_linea}: {linea.strip()} | Posición actual: {archivo_lectura.tell()}" for num_linea, linea in enumerate(archivo_lectura, start=1)))



with open(fichero, "w+") as archivo_escritura:
    archivo_escritura.write("AaEeIiOoUu")

with open(fichero, "a+") as archivo_anexar:
    archivo_anexar.seek(0) 
    contenido = archivo_anexar.read() 
    print("\nContenido completo después de anexar:", contenido)

try:
    with open(fichero, "a") as archivo_error:
        pass
except Exception as e:
    print("\nError al abrir en modo 'a' ya que solo te permite escribir al final del fichero")


