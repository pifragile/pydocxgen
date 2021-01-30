from pydocxgen.document.parts.document import Document
from pydocxgen.utils.zip import DocxFile

PARTS = [Document]
# Abstract representation of the docx document


class DocxDocument:
    def __init__(self):
        self.parts = {part.__name__: part() for part in PARTS}
        self.docx_file = DocxFile()

    # Renders all document parts an saves the zipped file
    def save(self, path):
        for part in self.parts.values():
            self.docx_file.write(part.path, part.render())

        self.docx_file.save(path)
