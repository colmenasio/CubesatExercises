import numpy as np
import tkinter as tk
import cv2
from PIL import Image, ImageTk

# ESTE EJERCICIO UTILIZA LA LIBRERIA `PIL`
# Instaladla con `pip install pillow`

# Este ejercicio no es un ejercicio como tal sino un playground donde podeis probar cosas de procesado de imagen.
# Las funciones `display_image` y `read_png` no teneis (ni debeis) de tocarlas.
# Implementad vuestras propias funciones que hagan cosas con vuestra imagen. Llamadlas desde __main__ para modificar la imagen
# SUGERENCIAS BÁSICAS
# # >>> Darle la vuelta a la imagen (mirror the image)
# # >>> Invertir los colores
# # >>> Jugad con la intensidad de la imagen
# # >>> Probar a hacer cosas mas raras como aumentar la intensidad de un rango de colores espefíficos
# # >>> Transformadla a escala de grises

# COSAS MAS AVANZADAS FILTROS
# Esto son mas bien retos. Son cosas relativamente mas avanzadas que requieren investigar y lanzarse sin miedo.
# Se que sois capaces si os atreveis, pero no os culparia si os achanta
# Hay miles de recursos online. Chatgpt os puede ayudar. Google os puede ayudar.
# Si os interesa alguna, sed valientes. Y si teneis dudas, escribidnos
# Muchas de estas ideas giran en torno a FILTROS CONVOLUCIONALES. Un buen punto de partida es este video:
# SOLO VEROS LA PARTE DE IMAGE PROCESSING. El resto no tiene nada que ver y os va a aburrir bastante
# https://youtu.be/KuXjwB4LzSA?si=wh7obswlHB3rALn1&t=513
# Las ideas son:
# # >>> Blurring the image
# # >>> Basic Edge Detection
# # >>> Image Sharpening

# Implementad aqui vuestras funciones
####################
def ejemplo_remove_red_channel(R: np.matrix[np.uint8], G: np.matrix[np.uint8], B: np.matrix[np.uint8]):
    R.fill(0) # Fill the red channel with zeroes and leave the other ones unchanged
    return R, G, B

####################

# No hace falta tocar estas dos funciones
##########################################################################
##########################################################################
def display_image(R: np.matrix[np.uint8], G: np.matrix[np.uint8], B: np.matrix[np.uint8]):
    # Check sizes and types
    if R.shape != G.shape or G.shape != B.shape:
        raise AttributeError("R, G, and B matrices are of different sizes!")
    if R.dtype != np.uint8 or G.dtype != np.uint8 or B.dtype != np.uint8:
        raise ValueError("R, G, and B matrices must have values of type np.uint8 but they don't.")

    # Convert to NumPy array and stack channels to create an RGB image
    R_array = np.array(R)
    G_array = np.array(G)
    B_array = np.array(B)
    image_array = np.stack((R_array, G_array, B_array), axis=-1)  # Shape: (height, width, 3)

    # Create an image using Pillow
    height, width, _ = image_array.shape
    pil_image = Image.fromarray(image_array)  # Create a PIL image from the NumPy array

    # Create Tkinter window
    root = tk.Tk()
    root.title("RGB Image Display")
    tk_image = ImageTk.PhotoImage(pil_image)
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    label.pack()

    # Run Tkinter event loop
    root.mainloop()

def read_png(image_path: str) -> tuple[np.matrix[np.uint8], np.matrix[np.uint8], np.matrix[np.uint8]]:
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not open or find the image.")

    # Split into R, G, B channels
    b, g, r = cv2.split(image)
    # Convert to np.matrix
    return np.matrix(r, dtype=np.uint8), np.matrix(g, dtype=np.uint8), np.matrix(b, dtype=np.uint8)
#############################################################################
#############################################################################

if __name__ == '__main__':
    # Load la image
    R, G, B = read_png("silly_cat.jpg")

    ## LLAMAD A VUESTRAS FUNCIONES PARA EDITAR LA IMAGEN
    # Por ejemplo
    R, G, B = ejemplo_remove_red_channel(R, G, B)

    # Display la imagen
    display_image(R, G, B)