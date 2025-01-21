#!/Users/antonin/OC/Projets/venv/bin/python
"""
convert_pdfs_to_pngs.py - Convertit tous les fichiers PDF d'un dossier en fichiers PNG
"""

import os
import fitz  # PyMuPDF


def convert_pdfs_to_pngs(input_directory, output_directory):
    """
    Convertit tous les fichiers PDF dans un dossier en fichiers PNG.
    @arg input_directory: Dossier contenant les fichiers PDF
    @arg output_directory: Dossier où enregistrer les PNG
    Return: Aucun
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Parcourir tous les fichiers PDF dans le dossier d'entrée
    for file_name in os.listdir(input_directory):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_directory, file_name)
            base_name = os.path.splitext(file_name)[0]  # Nom du fichier sans extension

            # Charger le PDF
            doc = fitz.open(pdf_path)
            for page_number in range(len(doc)):
                page = doc.load_page(page_number)  # Charger la page
                pix = page.get_pixmap()  # Obtenir l'image de la page
                png_file = os.path.join(output_directory, f"{base_name}.png")
                pix.save(png_file)  # Enregistrer la page en PNG
            doc.close()

    print(f"Tous les fichiers PDF ont été convertis en PNG dans : {output_directory}")


# Exemple d'utilisation
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./convert_pdfs_to_pngs.py <dossier_entree> <dossier_sortie>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    convert_pdfs_to_pngs(input_dir, output_dir)
