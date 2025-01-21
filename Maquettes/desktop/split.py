#!/Users/antonin/OC/Projets/venv/bin/python
"""
split_pdf_with_basename.py - Splits a PDF into individual pages with a custom basename
"""

import os
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_file, output_directory, base_name):
    """
    Splits a PDF into individual pages and saves them with a custom basename.
    @arg input_file: Path to the input PDF file
    @arg output_directory: Directory to save the output PDFs
    @arg base_name: Base name for the output files
    Return: None
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the PDF file
    reader = PdfReader(input_file)
    total_pages = len(reader.pages)

    for page_number in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])

        # Create a file for each page using the basename
        output_file = os.path.join(
            output_directory, f"{base_name}page_{page_number + 1}.pdf"
        )
        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

    print(f"PDF split into {total_pages} pages. Files saved in: {output_directory}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print(
            "Usage: ./split_pdf_with_basename.py <input_pdf> <output_directory> <base_name>"
        )
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_dir = sys.argv[2]
    base_name = sys.argv[3]

    split_pdf(input_pdf, output_dir, base_name)
