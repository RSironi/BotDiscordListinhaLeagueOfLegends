import xml.etree.ElementTree as ET

arquivo = "listinhabotlol2.0/Data/config.xml"
tree = ET.parse(arquivo)
root = tree.getroot()

BOT_TOKEN = root[0][0].text

HOST = root[1][0].text
DATABASE = root[1][1].text
USER = root[1][2].text
PASSWORD = root[1][3].text
