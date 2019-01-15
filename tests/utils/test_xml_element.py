from pydocxgen.utils.xml import XmlElement


def test_xml_element_creation():
    # Create an XML element
    xml_element = XmlElement('test')

    # Ensure element was created and has an lxml element associated with it
    assert isinstance(xml_element, XmlElement)
    assert xml_element.lxml.tag == 'test'


def test_to_string_conversion():
    xml_element = XmlElement('test')

    # Convert a simple element to a string and check
    string_output = xml_element.to_string()
    assert string_output == '<test xmlns:w="http://www.w3.org/1999/xhtml"/>'


def test_addition_of_child_elements():
    xml_element = XmlElement('test')
    child1 = xml_element.add_child('w:child1')
    child2 = xml_element.add_child('w:child2')

    # Ensure child elements are also instances of XmlElement
    assert isinstance(child1, XmlElement) and isinstance(child2, XmlElement)

    # Ensure there is an associated lxml element for the children
    assert len(xml_element.lxml) == 2
    assert 'child1' in xml_element.lxml[0].tag

    # Check if children are included in the string output
    string_output = xml_element.to_string()
    assert string_output == ('<test xmlns:w="http://www.w3.org/1999/xhtml">'
                             '<w:child1/>'
                             '<w:child2/>'
                             '</test>')


def test_conversion_of_attrib():
    xml_element = XmlElement('test', attribs={'w:someTag': 'someValue'})
    string_output = xml_element.to_string()

    # Ensure the attributes were added correctly
    assert string_output == ('<test xmlns:w="http://www.w3.org/1999/xhtml" '
                             'w:someTag="someValue"/>')
