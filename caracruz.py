import tkinter as tk
from tkinter import PhotoImage
import random
import os

def cargar_juego_caracruz(ventana):
    def lanzar_moneda():
        """Lanza la moneda y actualiza la etiqueta con el resultado."""
        resultado = random.choice(["Cara", "Cruz"])
        if resultado == "Cara":
            etiqueta_resultado.config(image=img_cara)
        else:
            etiqueta_resultado.config(image=img_cruz)
        etiqueta_texto.config(text=f"¡Es {resultado}!")

    # Rutas de las imágenes
    ruta_cara = "PythonCodeInfo/img/cara.png"
    ruta_cruz = "PythonCodeInfo/img/cruz.png"

    def cargar_imagenes():
        """Carga las imágenes desde archivos y maneja errores."""
        global img_cara, img_cruz
        if os.path.exists(ruta_cara) and os.path.exists(ruta_cruz):
            img_cara = PhotoImage(file=ruta_cara)
            img_cruz = PhotoImage(file=ruta_cruz)
            return True
        return False

    # Configurar el fondo de la ventana del juego
    ventana.config(bg="#2c3e50")  # Color de fondo uniforme para la ventana

    # Cargar imágenes
    if cargar_imagenes():
        # Etiqueta para mostrar la imagen del resultado
        etiqueta_resultado = tk.Label(ventana, bg="#2c3e50")  # Fondo igual al de la ventana
        etiqueta_resultado.pack(pady=20)

        # Etiqueta para mostrar el texto del resultado
        etiqueta_texto = tk.Label(ventana, text="Lanza la moneda", font=("Arial", 20), bg="#2c3e50", fg="white")
        etiqueta_texto.pack(pady=10)

        # Botón para lanzar la moneda
        boton_lanzar = tk.Button(ventana, text="Lanzar Moneda", font=("Arial", 16), bg="#2980b9", fg="white", command=lanzar_moneda)
        boton_lanzar.pack(pady=20)
    else:
        # Mostrar un mensaje de error si las imágenes no se encuentran
        etiqueta_error = tk.Label(ventana, text="Error: Imágenes no encontradas", font=("Arial", 16), bg="#2c3e50", fg="red")
        etiqueta_error.pack(pady=20)
