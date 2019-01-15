import os
from lxml import etree
from .errors import InvalidXmlInputError
from pydocxgen.document.document import Document


def xmltodoc(xml):
    if not xml:
        raise InvalidXmlInputError('xml should not be empty')
    root = etree.fromstring(xml)
    validate(root)
    return Document()


def validate(root):
    xsd = getxmlschema()
    if not xsd.validate(root):
        error = xsd.error_log.last_error
        raise InvalidXmlInputError(geterrormessage(error))


def geterrormessage(error):
    line = error.line
    column = error.column
    message = error.message

    return '{line}:{column} : {message}'\
        .format(line=line, message=message, column=column)


def getxmlschema():
    this_folder_path = os.path.dirname(os.path.abspath(__file__))
    docschema_path = os.path.join(this_folder_path, '..', 'docschema.xml')
    schema_file = open(docschema_path, 'r')
    xmlschema_doc = etree.parse(schema_file)

    return etree.XMLSchema(xmlschema_doc)
