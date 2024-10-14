import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from automata.fa.nfa import NFA
import string
import re
import os

#Archivo
nombre_archivo="sin_titulo.imm"
ruta_archivo=""

# Autómata
states = {f"q{i}" for i in range(60)}

nfa = NFA(
    states=states,
    input_symbols={char for char in list(string.printable)},
    transitions={
        'q0': {
            '<': {'q47'},
            '>': {'q47'},
            'y': {'q1'},
            'o': {'q1'},
            'n': {'q2'},
            'i': {'q3'},
            'i': {'q33'},
            'f': {'q48'},
            's': {'q13'},
            'p': {'q18'},
            'e': {'q16'},
            'm': {'q21'},
            'r': {'q28'},
            'c': {'q52'},
            '+': {'q10'},
            '-': {'q10'},
            '*': {'q10'},
            '/': {'q10'},
            '%': {'q10'},
            '{': {'q7'},
            '}': {'q7'},
            '(': {'q8'},
            ')': {'q8'},
            '[': {'q9'},
            ']': {'q9'},
            'F': {'q11'},
            'V': {'q11'},
            '=': {'q12'},
        },
        # n-o
        'q2': {
            'o': {'q1'},
        },
        # i-gual
        'q3': {
            'g': {'q4'},
        },
        'q4': {
            'u': {'q5'},
        },
        'q5': {
            'a': {'q6'},
        },
        'q6': {
            'l': {'q1'},
        },
        # s-i no
        'q13': {
            'i': {'q14'},
        },
        'q14': {
            'n': {'q15'},
        },
        'q15': {
            'o': {'q14'},
        },
        # e-n
        'q16': {
            'n': {'q17'},
        },
        # p-ara
        'q18': {
            'a': {'q19'},
        },
        'q19': {
            'r': {'q20'},
        },
        'q20': {
            'a': {'q17'},
        },
        # m-ientras
        'q21': {
            'i': {'q22'},
        },
        'q22': {
            'e': {'q23'},
        },
        'q23': {
            'n': {'q24'},
        },
        'q24': {
            't': {'q25'},
        },
        'q25': {
            'r': {'q26'},
        },
        'q26': {
            'a': {'q27'},
        },
        'q27': {
            's': {'q17'},
        },
        # r-omper
        'q28': {
            'o': {'q29'},
        },
        'q29': {
            'm': {'q30'},
        },
        'q30': {
            'p': {'q31'},
        },
        'q31': {
            'e': {'q32'},
        },
        'q32': {
            'r': {'q17'},
        },
        # i-mprimir
        'q33': {
            'm': {'q34'},
            'n': {'q41'},
        },
        'q34': {
            'p': {'q35'},
        },
        'q35': {
            'r': {'q36'},
        },
        'q36': {
            'i': {'q37'},
        },
        'q37': {
            'm': {'q38'},
        },
        'q38': {
            'i': {'q39'},
        },
        'q39': {
            'r': {'q40'},
        },
        # in-gresar
        'q41': {
            'g': {'q42'},
        },
        'q42': {
            'r': {'q43'},
        },
        'q43': {
            'e': {'q44'},
        },
        'q44': {
            's': {'q45'},
        },
        'q45': {
            'a': {'q46'},
        },
        'q46': {
            'r': {'q51'},
        },
        'q51': {
            'N': {'q40'},
            '': {'q40'},
        },
        # >= <= / > <
        'q47': {
            '=': {'q1'},
            '': {'q1'},
        },
        # f-un
        'q48': {
            'u': {'q49'},
        },
        'q49': {
            'n': {'q50'},
        },
        # c-ontinuar
        'q52': {
            'o': {'q53'},
        },
        'q53': {
            'n': {'q54'},
        },
        'q54': {
            't': {'q55'},
        },
        'q55': {
            'i': {'q56'},
        },
        'q56': {
            'n': {'q57'},
        },
        'q57': {
            'u': {'q58'},
        },
        'q58': {
            'a': {'q59'},
        },
        'q59': {
            'r': {'q17'},
        },
    },
    initial_state='q0',
    final_states={'q1', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q14', 'q17', 'q40', 'q50'},
)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos Ivan++", "*.imm")])
    if file_path:
        global ruta_archivo
        global nombre_archivo
        ruta_archivo= file_path
        nombre_archivo= file_path[file_path.rindex("/")+1:]
        win.title(nombre_archivo)
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Borrar el contenido actual
            text_area.insert(tk.END, content)
            syntax_highlight()

def save_file_as():
    global ruta_archivo
    global nombre_archivo
    file_path = filedialog.asksaveasfilename(defaultextension=".imm", filetypes=[("Archivos Ivan++", "*.imm")], initialfile=nombre_archivo)
    if file_path:
        ruta_archivo= file_path
        nombre_archivo= file_path[file_path.rindex("/")+1:]
        win.title(nombre_archivo)
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)

def save_file():
    if ruta_archivo!="":
        with open(ruta_archivo, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
    else:
        save_file_as()

def syntax_highlight():
    texto = text_area.get(1.0, tk.END).split()
    text_area.tag_remove("sys", 1.0, tk.END)
    text_area.tag_remove("loop", 1.0, tk.END)
    text_area.tag_remove("logic", 1.0, tk.END)
    text_area.tag_remove("llaves", 1.0, tk.END)
    text_area.tag_remove("par", 1.0, tk.END)
    text_area.tag_remove("corch", 1.0, tk.END)
    text_area.tag_remove("operador", 1.0, tk.END)
    text_area.tag_remove("bool", 1.0, tk.END)
    text_area.tag_remove("asing", 1.0, tk.END)
    text_area.tag_remove("cond", 1.0, tk.END)

    simbolos_especiales=("+", "-", "/", "%", "*", "^", "=", ">", "<" "(", ")", "{", "}", "[", "]")

    #Separar operadores en palabras
    texto_provicional=[]
    for palabra in texto:
        for simbolo in simbolos_especiales:
            if simbolo in palabra:
                indice= palabra.index(simbolo)
                if (simbolo==">" or simbolo=="<") and len(palabra) > indice+1 and palabra[indice+1]=="=":
                    if indice>1:
                        texto_provicional.append(palabra[:indice-1])
                        
                    texto_provicional.append(simbolo+"=")

                    if len(palabra) > indice+2:
                        texto_provicional.append(palabra[indice+2:])
                else:
                    if indice>1:
                        texto_provicional.append(palabra[:indice-1])
                        
                    texto_provicional.append(simbolo)

                    if len(palabra) > indice+1:
                        texto_provicional.append(palabra[indice+1:])
            else:
                texto_provicional.append(palabra)

    texto= set(texto_provicional)

    for word in texto:
        start = 1.0
        while True:
            start = text_area.search(word, start, tk.END)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            if nfa.accepts_input(word):
                salida_nfa= nfa.read_input(word)
                if('q1' in salida_nfa):
                    text_area.tag_add("logic", start, end)
                elif('q7' in salida_nfa):
                    text_area.tag_add("llaves", start, end)
                elif('q8' in salida_nfa):
                    text_area.tag_add("par", start, end)
                elif('q9' in salida_nfa):
                    text_area.tag_add("corch", start, end)
                elif('q10' in salida_nfa):
                    text_area.tag_add("operador", start, end)
                elif('q11' in salida_nfa):
                    text_area.tag_add("bool", start, end)
                elif('q12' in salida_nfa):
                    text_area.tag_add("asing", start, end)
                elif('q14' in salida_nfa):
                    text_area.tag_add("cond", start, end)
            start = end

    #Strings
    # texto_completo= text_area.get(1.0, tk.END)
    # strings= re.findall(r'".*"', texto_completo)
    # strings = set(strings)
    # for string in strings:
    #     start = 1.0
    #     while True:
    #         start = text_area.search(string, start, tk.END)
    #         if not start:
    #             break
    #         end = f"{start}+{len(string)}c"
    #         text_area.tag_add("string", start, end)

    #Comentarios
    # comentarios= re.findall(r'#.*', texto_completo)
    # comentarios = set(comentarios)
    # for comentario in comentarios:
    #     start = 1.0
    #     while True:
    #         start = text_area.search(comentario, start, tk.END)
    #         if not start:
    #             break
    #         end = f"{start}+{len(comentario)}c"
    #         text_area.tag_add("comen", start, end)


def reemplazo(match):
    return f'print({match.group(1)})'

def compilar():
    global ruta_archivo
    global nombre_archivo
    
    codigo_py= text_area.get(1.0, tk.END)

    #Identación
    codigo_temporal=""
    llaves=0
    for linea in codigo_py.split("\n"):
        linea_modificada="\n"
        for i in range(llaves):
            linea_modificada+="  "

        linea_modificada+=linea

        if("{" in linea):
            llaves+=1
        if("}" in linea):
            llaves-=1
            
        codigo_temporal+=linea_modificada
    codigo_py= codigo_temporal

    #simbolos
    codigo_py= codigo_py.replace("{", ":").replace("}", "")

    #return
    codigo_py= codigo_py.replace("regresa ", "return ")
    
    #Condicionales
    codigo_py= codigo_py.replace("sino si", "elif")
    codigo_py= re.sub(r"\s?si\s", "if ", codigo_py)
    codigo_py= re.sub(r"\s?sino\s", "else ", codigo_py)

    #Booleanos
    codigo_py= re.sub(r"\s?V\s", " True ", codigo_py)
    codigo_py= re.sub(r"\s?F\s", " False ", codigo_py)

    #Función
    codigo_py= re.sub(r"\s?fun\s", "def ", codigo_py)

    #control
    codigo_py= codigo_py.replace("mientras ", "while ").replace("para ", "for ").replace("romper", "break").replace("continuar", "continue").replace(" igual ", "==")
    
    #Rango
    codigo_py= re.sub(r"en\s\((\d+),\s?(\d+)(,\s?(\d+))?\)", r"in range(\1,\2\3)", codigo_py)

    #Operadores booleanos
    codigo_py= codigo_py.replace(" y ", "and").replace(" o ", "or")
    codigo_py= re.sub(r"\s?no\s", "not ", codigo_py)
    
    #entrada
    codigo_py= codigo_py.replace("ingresar", "input()").replace("ingresarN", "int(input())")

    #matematicas
    codigo_py= codigo_py.replace("^", "**")
    codigo_py.replace("++", "+=1").replace("--", "-=1")
    
    #Imprimir
    lineas_print= list(linea.replace("imprimir ", "print(")+f"{')' if 'imprimir ' in linea else ''}" for linea in codigo_py.split("\n"))
    codigo_py=""
    for linea in lineas_print:
        codigo_py+= linea+"\n"

    # consola.configure(state='normal')
    # consola.delete(1.0, tk.END)  # Borrar el contenido actual
    # consola.insert(tk.END, codigo_py)
    # consola.configure(state='disabled')

    #Escribir a archivo .py
    if ruta_archivo=="": ruta_archivo= nombre_archivo
    archivo= ruta_archivo.replace(".imm", ".py")
    print("archivo: ", archivo)
    with open(archivo, 'w') as file:
        file.write(codigo_py)
        #Ejecutar
        try:
            consola.configure(state='normal')
            consola.delete(1.0, tk.END)
            consola.insert(tk.END, "> Archivo compilado en "+archivo+"\n")
            consola.configure(state='disabled')
            os.system(f'start cmd /k python "{archivo}"')
        except:
            consola.configure(state='normal')
            consola.delete(1.0, tk.END)
            consola.insert(tk.END, "> Error al compilar el archivo\n")
            consola.configure(state='disabled')

# Crear tkinter ventana principal
win = tk.Tk()
win.title(nombre_archivo)
win.configure(background="gray1")

# Crear un frame para la cabecera
header_frame = tk.Frame(win, background="gray1")
header_frame.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=10)

# Etiqueta del título en la cabecera
ttk.Label(win, text="IDE Ivan++", font=("Fira Code", 18),background="gray1", foreground="green1").grid(column=0, row=0)

# Botón de abrir en la cabecera
open_button = tk.Button(header_frame, text="Abrir archivo", command=open_file, background="gray10", foreground="white")
open_button.grid(column=0, row=1, padx=10)

# Botón de guardar como en la cabecera
save_as_button = tk.Button(header_frame, text="Guardar Como", command=save_file_as, background="gray10", foreground="white")
save_as_button.grid(column=1, row=1, padx=10)

# Botón de guardar en la cabecera
save_button = tk.Button(header_frame, text="Guardar", command=save_file, background="gray10", foreground="white")
save_button.grid(column=2, row=1, padx=10)

# Botón de compilar
open_button = tk.Button(header_frame, text="Compilar", command=compilar, background="gray10", foreground="white")
open_button.grid(column=12, row=1, padx=10)

# Crear área de texto con desplazamiento
text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=100, height=20, font=("Fira Code", 15), foreground="white", background="gray10", insertbackground="white", insertwidth=2)
text_area.grid(column=0, row=2, pady=10, padx=10)

consola= scrolledtext.ScrolledText(win, wrap=tk.WORD, width=100, height=5, font=("Fira Code", 15), foreground="white", background="gray10", insertbackground="white", insertwidth=2)
consola.grid(column=0, row=3, pady=10, padx=10)
consola.insert(tk.END, ">")
consola.configure(state='disabled')

# Colocar el cursor en el área de texto
text_area.focus()

# Configurar una etiqueta para resaltar
text_area.tag_configure("sys", foreground="chartreuse1")
text_area.tag_configure("control", foreground="cadetblue1")
text_area.tag_configure("llaves", foreground="darkgoldenrod1")
text_area.tag_configure("par", foreground="chartreuse")
text_area.tag_configure("corch", foreground="cyan3")
text_area.tag_configure("operador", foreground="lightcoral")
text_area.tag_configure("bool", foreground="hotpink")
text_area.tag_configure("asing", foreground="coral")
text_area.tag_configure("logic", foreground="cornflowerblue")
text_area.tag_configure("cond", foreground="magenta2")
text_area.tag_configure("fun", foreground="darkslateblue")
text_area.tag_configure("comen", foreground="lightyellow3")
text_area.tag_configure("string", foreground="orangered1")


# Asociar la función de resaltado al evento de liberación de tecla
text_area.bind("<KeyRelease>", lambda event: syntax_highlight())

win.mainloop()