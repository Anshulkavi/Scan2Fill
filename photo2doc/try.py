from pdf2image import convert_from_path

images = convert_from_path("sem6_result.pdf", poppler_path=r"E:\poppler\Library\bin")
for img in images:
    img.show()
