from lxml import etree

xml1 = "bancoDTD.xml"

def dtd_validate(xml):
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(xml, parser)

dtd_validate(xml1)