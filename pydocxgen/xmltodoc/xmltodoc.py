from lxml import etree
from .errors import InvalidXmlInputError
from pydocxgen.document.document import Document


def xmltodoc(xml):
    if not xml:
        raise InvalidXmlInputError
    document_root = etree.fromstring(xml)
    if document_root.tag != 'document':
        raise InvalidXmlInputError
    return Document()
