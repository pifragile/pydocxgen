import shutil
from zipfile import ZipFile
import os
from pydocxgen.document.document import DocxDocument


# Ensures that parts are properly added to the document
def test_docx_document_creation():
    document = DocxDocument()
    # Check if the document part was added to parts
    assert 'Document' in document.parts

    # Create temp folder
    temp_path = 'temp'
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)

    # Save the document
    path = 'temp/test.docx'
    document.save(path)

    # Check if the document was indeed saved
    with ZipFile(path) as zip_file:
        with zip_file.open('word/document.xml') as document_file:
            file_content = document_file.read().decode("utf-8")
            assert file_content == '<w:document></w:document>'

    # Delete the temp folder
    shutil.rmtree(temp_path)
