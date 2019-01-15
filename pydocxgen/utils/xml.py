from lxml import etree

NSMAP = {'w': "http://www.w3.org/1999/xhtml"}


class XmlElement():
    def __init__(self, name, attribs={}):
        processed_attrib = {
            self.insert_namespace_url(attrib): value for
            attrib, value in attribs.items()}

        self.lxml = etree.Element(
            self.insert_namespace_url(name),
            nsmap=NSMAP,
            **processed_attrib)

    def add_child(self, name, attribs={}):
        child = XmlElement(name, attribs=attribs)
        self.lxml.append(child.lxml)

        return child

    def to_string(self, **kwargs):
        return etree.tostring(self.lxml, **kwargs).decode("utf-8")

    @staticmethod
    def insert_namespace_url(text):
        if ':' in text:
            namespace, name = text.split(':')
            text = '{' + NSMAP[namespace] + '}' + name

        return text
