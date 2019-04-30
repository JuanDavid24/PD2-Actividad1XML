import pytest
from xmlschema.etree import ParseError
from XSD import valXSD

schema1 = "banco.xsd"
schema2 = "TestFiles/bancoRoto.xsd"

xml1 = "banco.xml"
xml2 = "TestFiles/bancoRoto.xml"
xml3 = "TestFiles/bancoSinTagCuentas.xml"
xml4 = "TestFiles/bancoBalanceMenor.xml"
xml5 = "TestFiles/bancoIdCuentaRepetida.xml"

def testOk():
    assert valXSD.XMLvsXSDIsValid(schema1, xml1) == True
    pass

def testXMLRoto():
    with pytest.raises(ParseError):
        valXSD.XMLvsXSDIsValid (schema1, xml2)
    pass

def testXSDRoto():
    with pytest.raises(ParseError):
        valXSD.XMLvsXSDIsValid(schema2, xml1)
    pass

def testXMLInvalido():
    assert valXSD.XMLvsXSDIsValid(schema1, xml3) == False
    pass

def testXMLBalanceMenor():
    assert valXSD.XMLvsXSDIsValid(schema1, xml4) == False
    pass

def testXMLIdCuentaRepetida():
    assert valXSD.XMLvsXSDIsValid(schema1, xml5) == False
    pass

