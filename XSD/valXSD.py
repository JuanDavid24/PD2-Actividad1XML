import xmlschema

def XMLvsXSDIsValid(schemaName, xmlName):
    schema = xmlschema.XMLSchema(schemaName)
    return schema.is_valid(xmlName)

def XMLvsXSDValidate(schemaName, xmlName):
    schema = xmlschema.XMLSchema(schemaName)
    return schema.validate(xmlName)

xml = "banco.xml"
xsd = "banco.xsd"

print (XMLvsXSDValidate(xsd, xml))
