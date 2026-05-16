# Write a program to manipulate pdf files using pyPDF. Your programs should be
# able to merge multiple pdf files into a single pdf. You are welcome to add
# more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting,
# merging, cropping, and transforming the pages of PDF files. It can also add
# custom data, viewing options, and passwords to PDF files. pypdf can retrieve
# text and metadata from PDFs as well.
from reportlab.pdfgen import canvas
from pypdf import PdfWriter
import os

# Create folder
folder_name = "PDF_Files"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)


# Function to create sample PDF
def create_pdf(filename, text):
    path = os.path.join(folder_name, filename)

    c = canvas.Canvas(path)
    c.drawString(100, 750, text)
    c.save()

    print(f"{filename} created.")


# Create sample PDFs
create_pdf("file1.pdf", "This is PDF File 1")
create_pdf("file2.pdf", "This is PDF File 2")
create_pdf("file3.pdf", "This is PDF File 3")

print("\nSample PDFs created successfully.\n")

pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
merger = PdfWriter()
for pdf in pdf_files:
    path = os.path.join(folder_name, pdf)
    merger.append(path)
    print(f"{pdf} added for merging.")

merged_path = os.path.join(folder_name, "merged.pdf")
with open(merged_path, "wb") as f:
    merger.write(f)

print("\nAll PDFs merged successfully.")
print("Merged file created: merged.pdf")
