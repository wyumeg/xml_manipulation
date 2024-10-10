from lxml import etree
import xml
from report_generator import schema_path

# Estrutura do XML representada como um dicionário
xml_structure = schema_path


class XMLProcessor:
    def __init__(self, xml_file, xml_structure):
        self.tree = etree.parse(xml_file)
        self.root = self.tree.getroot()
        self.structure = xml_structure

    def extract_data(self, tag_path):
        """Extrai dados do XML com base no caminho especificado no esquema."""
        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
        element = self.root.xpath(tag_path, namespaces=namespaces)
        if element:
            return element[0].text
        return None

    def process_tag(self, tag, structure):
        """Recursivamente processa as tags no esquema."""
        result = {}
        for subtag, path_or_structure in structure.items():
            if isinstance(path_or_structure, dict):
                # Se houver subestrutura, processa recursivamente
                result[subtag] = self.process_tag(subtag, path_or_structure)
            else:
                # Caso contrário, extraia os dados usando o XPath
                result[subtag] = self.extract_data(path_or_structure)
        return result

    def process(self):
        """Processa todo o esquema e retorna os dados."""
        return self.process_tag('NFe', self.structure['NFe'])

# Caminho absoluto para o diretório do projeto
xml_file_path = r'C:\\Users\\User\\Desktop\\mirante\\Nova pasta\\31240913569316000140550010000111291367320771-ProcNfe.xml'
processor = XMLProcessor(xml_file_path, xml_structure) #type: ignore
dados = processor.process()
print(dados)