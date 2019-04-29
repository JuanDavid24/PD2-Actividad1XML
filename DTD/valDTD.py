from lxml import etree

xml1 = "bancoDTD.xml"

def dtdValidate(xml):
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(xml, parser)

dtdValidate(xml1)