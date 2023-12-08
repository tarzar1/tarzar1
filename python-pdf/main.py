import tkinter as tk
from tkinter import Text, Scrollbar, VERTICAL, RIGHT, Y
import fitz  # PyMuPDF

class PDFTextPositioner:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.root = tk.Tk()
        self.root.title("PDF Text Positioner")

        # Configura una barra de desplazamiento vertical
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configura un widget de texto para mostrar y editar el texto
        self.text_widget = Text(self.root, wrap='none', font=('Arial', 12), fg='white', bg='black', yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(expand=True, fill='both', padx=10, pady=40)

        # Asocia la barra de desplazamiento con el widget de texto
        self.scrollbar.config(command=self.text_widget.yview)

        # Cambia el tema a dark
        self.set_dark_theme()

        # Llama a la función para posicionar el texto desde el PDF
        self.position_text()

        # Habilita la edición
        self.text_widget.config(state=tk.NORMAL)

        # Inicia el bucle principal de la GUI
        self.root.mainloop()

    def set_dark_theme(self):
        # Configura el tema dark para el widget de texto
        self.text_widget.config(insertbackground='white', selectbackground='#0080C0', selectforeground='white')

        # Configura el tema dark para la ventana principal
        self.root.tk_setPalette(background='#1E1E1E', foreground='white', activeBackground='#0080C0', activeForeground='white')

    def center_text(self):
        # Centra el texto verticalmente en el widget de texto
        self.text_widget.tag_configure("center", justify='center')
        self.text_widget.tag_add("center", "1.0", "end")

    def position_text(self):
        # Abre el archivo PDF
        pdf_document = fitz.open(self.pdf_path)

        # Concatena el texto de todas las páginas en una sola cadena
        full_text = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            for text_block in page.get_text("blocks"):
                full_text += text_block[4][:100]  # Limita la impresión a los primeros 100 caracteres del texto
                full_text += '\n'

        pdf_document.close()

        # Inserta el texto en el widget de texto
        self.text_widget.insert(tk.END, full_text)

        # Centra el texto verticalmente después de insertar todo el texto
        self.center_text()

# Ruta del archivo PDF
pdf_path = "109-Poemas-escogidos.pdf"  # Reemplaza con la ruta de tu archivo PDF

# Crea una instancia de PDFTextPositioner
pdf_positioner = PDFTextPositioner(pdf_path)
