import fitz  # PyMuPDF

def pdf_text_locator(pdf_path, target_coordinates):
    # Abre el archivo PDF
    pdf_document = fitz.open(pdf_path)

    # Diccionario para almacenar texto y sus coordenadas
    text_coordinates = {}

    # Itera sobre cada página del PDF
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        # Itera sobre cada bloque de texto en la página
        for block_index, text_block in enumerate(page.get_text("blocks")):
            # Extrae el texto y las coordenadas del bloque de texto
            text = text_block[4]
            rect = fitz.Rect(text_block[:4])  # Rectángulo que representa las coordenadas
            coordinates = (rect.x0, rect.y0)

            # Almacena el texto y sus coordenadas en el diccionario
            text_coordinates[coordinates] = text

    # Cierra el documento PDF
    pdf_document.close()

    # Busca el texto en las coordenadas proporcionadas por el usuario
    if target_coordinates in text_coordinates:
        found_text = text_coordinates[target_coordinates]
        print(f"Texto encontrado en coordenadas {target_coordinates}: {found_text}")
    else:
        print(f"No se encontró texto en las coordenadas {target_coordinates}.")

# Ruta del archivo PDF
pdf_path = "109-Poemas-escogidos.pdf"

# Coordenadas proporcionadas por el usuario
target_coordinates = (42.51969909667969, 83.83541870117188)

# Llama a la función para buscar y mostrar texto en coordenadas específicas
pdf_text_locator(pdf_path, target_coordinates)
