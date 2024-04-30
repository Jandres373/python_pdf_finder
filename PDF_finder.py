""" 
    Este programa busca y muestra los resultados de una búsqueda en Google.
    El usuario ingresa un término de búsqueda, y el programa realiza la búsqueda en Google en formato PDF.
    desarrollado por J.A.M
"""

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import re
import webbrowser
from googlesearch import search


def abrir_enlace():
    index = widget_resultados.index(tk.CURRENT)

    line_start = widget_resultados.index(f"{index} linestart")
    line_end = widget_resultados.index(f"{index} lineend +1c")
    linea_completa = widget_resultados.get(line_start, line_end).strip()

    match = re.search(r'https://.*\.pdf$', linea_completa)

    if match:
        url = match.group()
        webbrowser.open_new(url)
    else:
        messagebox.showinfo("Alerta", "No se ha encontrado un enlace válido.")


def buscar_y_mostrar():
    search_phrase = entrada_busqueda.get()

    resultados = []
    for resultado in search(search_phrase + " filetype:pdf", num_results=10, advanced=True):
        if re.match(r'https://.*\.pdf$', resultado.url):
            resultados.append(resultado.title + "\n" + resultado.description +
                              "\n" + resultado.url + "\n" + "\n" + "\n")
    if len(resultados) == 0:
        messagebox.showinfo(
            "Alerta", "No se encontraron resultados para la búsqueda.")
        return

    widget_resultados.delete(1.0, tk.END)  # Limpiar el contenido actual
    widget_resultados.insert(tk.END, "\n".join(resultados))

    start = 1.0
    for resultado in resultados:
        match = re.search(r'https://.*\.pdf', resultado)
        if match:
            start = widget_resultados.search(
                match.group(), start, tk.END, regexp=True)
            end = f"{start}+{len(match.group())}c"
            widget_resultados.tag_add("link", start, end)
            start = end


ventana = tk.Tk()
ventana.title("Buscador de Archivos PDF")

etiqueta_busqueda = tk.Label(
    ventana, text="Bienvenido al buscador de PDF's by J.A.M")
etiqueta_busqueda.pack(pady=10)

etiqueta_busqueda = tk.Label(
    ventana, text="Ingrese Término de Búsqueda:")
etiqueta_busqueda.pack(pady=10)

entrada_busqueda = tk.Entry(ventana, width=30)
entrada_busqueda.pack(pady=10)

boton_buscar = tk.Button(
    ventana, text="Buscar y Mostrar Resultados", command=buscar_y_mostrar)
boton_buscar.pack(pady=20)

widget_resultados = scrolledtext.ScrolledText(ventana, width=60, height=20)
widget_resultados.pack(pady=10)

widget_resultados.tag_configure("link", foreground="blue", underline=True)
widget_resultados.tag_bind("link", "<Button-1>", abrir_enlace)

mensaje_resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=mensaje_resultado)
etiqueta_resultado.pack()

ventana.mainloop()
