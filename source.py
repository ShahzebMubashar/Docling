from docling.document_converter import DocumentConverter

source = "Raw (2 Pages).pdf"

converter = DocumentConverter()
result = converter.convert(source)

print(result.document.export_to_dict())

with open('conversion_results.txt', 'w', encoding='utf-8') as f:
    f.write("\n\nJson Converter: \n")
    f.write(result.document.export_to_dict())