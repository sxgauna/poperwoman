from PIL import Image
import os

def dividir_guardar_imagen(ruta_imagen, carpeta_destino, divisiones_x_columna):
    if not os.path.isfile(ruta_imagen):
        print(f"Error: The file {ruta_imagen} does not exist.")
        return

    try:
        with Image.open(ruta_imagen) as img:
            ancho, alto = img.size
            img = img.convert('RGBA')  # Ensure image has an alpha channel

            tamano_cuadrado = ancho // divisiones_x_columna
            divisiones_x_fila = alto // tamano_cuadrado
            os.makedirs(carpeta_destino, exist_ok=True)

            contador = 0
            for i in range(divisiones_x_fila):
                for j in range(divisiones_x_columna):
                    izquierda = j * tamano_cuadrado
                    superior = i * tamano_cuadrado
                    derecha = izquierda + tamano_cuadrado
                    inferior = superior + tamano_cuadrado

                    cuadrado = img.crop((izquierda, superior, derecha, inferior))
                    nombre_archivo = f"tile ({contador}).png"
                    cuadrado.save(os.path.join(carpeta_destino, nombre_archivo), format='PNG')
                    contador += 1

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
dividir_guardar_imagen("assets/images/tiles/tileset1.png", "assets/images/tiles/", 12)


