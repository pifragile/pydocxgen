from pydocxgen.xmltodoc.xmltodoc import xmltodoc
from pydocxgen.xmltodoc.errors import InvalidXmlInputError
import pytest


def test_empty_input():
    with pytest.raises(InvalidXmlInputError) as e:
        xmltodoc('')
    assert str(e.value) == 'xml should not be empty'


def test_invalid_input():
    with pytest.raises(InvalidXmlInputError) as e:
        xmltodoc('<doc></doc>')
    expected_error_msg = \
        '1:0 : Element \'doc\': No matching global declaration available ' \
        'for the validation root.'
    assert str(e.value) == expected_error_msg


def test_valid_input():
    empty_input = '<document></document>'
    empty_output = '<w:document></w:document>'
    assert xmltodoc(empty_input).render() == empty_output
