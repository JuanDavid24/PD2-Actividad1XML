import pytest
from xmlschema.etree import ParseError
from XSD import valXSD

schema1 = "banco.xsd"
schema2 = "Test_files/banco_roto.xsd"

xml1 = "banco.xml"
xml2 = "Test_files/banco_roto.xml"
xml3 = "Test_files/banco_sinTagCuentas.xml"

def test_ok():
    assert valXSD.XMLvsXSD_isValid(schema1, xml1) == True
    pass

def test_xmlRoto():
    with pytest.raises(ParseError):
        valXSD.XMLvsXSD_isValid (schema1, xml2)
    pass

def test_xsdRoto():
    with pytest.raises(ParseError):
        valXSD.XMLvsXSD_isValid(schema2, xml1)
    pass
def test_xmlInvalido():
    assert valXSD.XMLvsXSD_isValid(schema1, xml3) == False
    pass


