import tkinter as tk
import random

def cargar_juego_piedrapapeltijera(ventana):
    def jugar(opcion_jugador):
        opciones = ["Piedra", "Papel", "Tijeras"]
        opcion_computadora = random.choice(opciones)
        
        # Determinar el resultado del juego
        if opcion_jugador == opcion_computadora:
            resultado = "Empate"
        elif (opcion_jugador == "Piedra" and opcion_computadora == "Tijeras") or \
            (opcion_jugador == "Papel" and opcion_computadora == "Piedra") or \
            (opcion_jugador == "Tijeras" and opcion_computadora == "Papel"):
            resultado = "¡Ganaste!"
        else:
            resultado = "Perdiste"

        # Actualizar la etiqueta con el resultado
        label_resultado.config(text=f"Resultado: {resultado}", bg="#2c3e50")
        label_jugador.config(text=f"Jugador: {opcion_jugador}", bg="#2c3e50")
        label_computadora.config(text=f"Computadora: {opcion_computadora}", bg="#2c3e50")
        
        # Mostrar imagen de la computadora
        if opcion_computadora == "Piedra":
            label_img_computadora.config(image=img_piedra)
        elif opcion_computadora == "Papel":
            label_img_computadora.config(image=img_papel)
        else:
            label_img_computadora.config(image=img_tijeras)

    # Configuración de la ventana del juego
    ventana.title("Piedra, Papel o Tijeras")
    ventana.geometry("580x400")
    ventana.config(bg="#2c3e50")

    # Ruta de todas las imágenes y convertirlas en objetos PhotoImage
    img_piedra = tk.PhotoImage(file="PythonCodeInfo/img/piedra.png").subsample(4, 4)
    img_papel = tk.PhotoImage(file="PythonCodeInfo/img/papel.png").subsample(4, 4)
    img_tijeras = tk.PhotoImage(file="PythonCodeInfo/img/tijera.png").subsample(4, 4)

    # Columna izquierda (Opciones del jugador)
    frame_jugador = tk.Frame(ventana)
    frame_jugador.grid(row=0, column=0, padx=10, pady=10)

    boton_piedra = tk.Button(frame_jugador, image=img_piedra, command=lambda: jugar("Piedra"))
    boton_piedra.pack(pady=5)

    boton_papel = tk.Button(frame_jugador, image=img_papel, command=lambda: jugar("Papel"))
    boton_papel.pack(pady=5)

    boton_tijeras = tk.Button(frame_jugador, image=img_tijeras, command=lambda: jugar("Tijeras"))
    boton_tijeras.pack(pady=5)

    # Columna derecha (Opciones de la computadora)
    frame_computadora = tk.Frame(ventana)
    frame_computadora.grid(row=0, column=2, padx=10, pady=10)

    label_img_computadora = tk.Label(frame_computadora)
    label_img_computadora.pack(pady=5)

    # Columna central (Resultados)
    frame_resultado = tk.Frame(ventana)
    frame_resultado.grid(row=0, column=1, padx=10, pady=10)

    label_resultado = tk.Label(frame_resultado, text="Resultado:", font=("Helvetica", 14))
    label_resultado.pack(pady=10)

    label_jugador = tk.Label(frame_resultado, text="Jugador: ", font=("Helvetica", 12))
    label_jugador.pack(pady=5)

    label_computadora = tk.Label(frame_resultado, text="Computadora: ", font=("Helvetica", 12))
    label_computadora.pack(pady=5)

    # Mantener las referencias a las imágenes para evitar que se recojan por el recolector de basura
    ventana.img_piedra = img_piedra
    ventana.img_papel = img_papel
    ventana.img_tijeras = img_tijeras
