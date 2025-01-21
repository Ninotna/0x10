#!/Users/antonin/OC/Projets/venv/bin/python
"""
split_and_convert_pdf.py - Divise un PDF et convertit chaque page en PNG
"""

import os
from PyPDF2 import PdfReader, PdfWriter
import fitz  # PyMuPDF


def split_and_convert_pdf(input_file, output_directory, base_filename):
    """
    Divise un PDF en pages individuelles et convertit chaque page en PNG.
    @arg input_file: Chemin du fichier PDF d'entrée
    @arg output_directory: Répertoire pour les fichiers de sortie
    @arg base_filename: Préfixe à utiliser pour les fichiers générés
    Return: Aucun
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Lire le PDF
    reader = PdfReader(input_file)
    total_pages = len(reader.pages)

    for page_number in range(total_pages):
        # Nommer les fichiers en fonction de base_filename
        pdf_output_file = os.path.join(
            output_directory, f"{base_filename}_page_{page_number + 1}.pdf"
        )
        png_output_file = os.path.join(
            output_directory, f"{base_filename}_page_{page_number + 1}.png"
        )

        # Diviser en fichiers PDF individuels
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])
        with open(pdf_output_file, "wb") as output_pdf:
            writer.write(output_pdf)

        # Convertir la page en PNG
        doc = fitz.open(pdf_output_file)  # Charger le PDF
        page = doc.load_page(0)  # Charger la première page
        pix = page.get_pixmap()  # Obtenir l'image
        pix.save(png_output_file)
        doc.close()

    print(f"PDF divisé et converti en PNG dans le répertoire : {output_directory}")


# Exemple d'utilisation
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: ./split_and_convert_pdf.py <fichier_pdf> <repertoire_sortie> <nom_fichier_base>"
        )
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_dir = sys.argv[2]
    base_file_name = sys.argv[3]
    split_and_convert_pdf(input_pdf, output_dir, base_file_name)
