import xmlschema

def XMLvsXSD_isValid(schemaName, xmlName):
    schema = xmlschema.XMLSchema(schemaName)
    return schema.is_valid(xmlName)

def XMLvsXSD_validate(schemaName, xmlName):
    schema = xmlschema.XMLSchema(schemaName)
    return schema.validate(xmlName)

xml = "banco.xml"
xsd = "banco.xsd"

print (XMLvsXSD_isValid(xsd, xml))
