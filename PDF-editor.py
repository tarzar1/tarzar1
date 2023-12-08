import tkinter as tk
from tkinter import Scrollbar, VERTICAL, RIGHT, Y
import fitz  # PyMuPDF

class PDFTextPositioner:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("PDF Text Positioner")

        # Configura una barra de desplazamiento vertical
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configura un widget de texto para mostrar y editar el texto
        self.text_widget = tk.Text(self.root, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(expand=True, fill='both', padx=50, pady=1)

        # Asocia la barra de desplazamiento con el widget de texto
        self.scrollbar.config(command=self.text_widget.yview)

        # Cambia el tema a oscuro
        self.set_dark_theme()

        # Llama a la función para posicionar el texto desde el PDF
        self.position_text()

        # Habilita la edición
        self.text_widget.config(state=tk.NORMAL)

        # Inicia el bucle principal de la GUI
        self.root.mainloop()

    def set_dark_theme(self):
        # Configura el tema oscuro para el widget de texto
        self.text_widget.config(insertbackground='white', selectbackground='#0080C0', selectforeground='white')

        # Configura el tema oscuro para la ventana principal
        self.root.tk_setPalette(background='#1E1E1E', foreground='white', activeBackground='#1080C0', activeForeground='white')

    def position_text(self):
        # Abre el archivo PDF
        pdf_document = fitz.open(self.pdf_path)

        # Itera sobre las páginas del PDF
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]

            # Obtiene el texto y las posiciones de los bloques en la página
            text_blocks = page.get_text("blocks")

            # Itera sobre los bloques de texto de la página
            for text_block in text_blocks:
                block_text = text_block[4]
                block_x, block_y, _, _ = text_block[:4]  # Extrae las coordenadas x, y del bloque

                # Redondea las coordenadas x e y a números enteros
                rounded_x, rounded_y = round(block_x), round(block_y)

                # Construye la posición del bloque en el widget de texto
                position = f"{rounded_x}.{rounded_y}"  # Use the rounded coordinates as the index

                # Inserta el texto en el widget de texto en la posición correspondiente
                self.text_widget.insert(position, block_text + "\n")

        # Cierra el documento PDF
        pdf_document.close()

# Ruta del archivo PDF
pdf_path = "poem.pdf"  # Reemplaza con la ruta de tu archivo PDF

# Crea una instancia de PDFTextPositioner
pdf_positioner = PDFTextPositioner(pdf_path)
