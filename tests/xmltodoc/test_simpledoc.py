from pydocxgen.xmltodoc.xmltodoc import xmltodoc
from pydocxgen.xmltodoc.errors import InvalidXmlInputError
import pytest


def test_empty_input():
    with pytest.raises(InvalidXmlInputError):
        xmltodoc('')


def test_invalid_input():
    with pytest.raises(InvalidXmlInputError):
        xmltodoc('<doc></doc>')


def test_valid_input():
    empty_input = '<document></document>'
    empty_output = '<w:document></w:document>'
    assert xmltodoc(empty_input).render() == empty_output
