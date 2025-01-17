from lxml import etree

class XMLParser:
    def __init__(self, xml_file):
        """Inicializa o parser e carrega o arquivo XML."""
        try:
            # Tenta carregar e fazer o parsing do arquivo XML
            self.tree = etree.parse(xml_file)
            self.root = self.tree.getroot()
        except Exception as e:
            raise Exception(f"Erro ao carregar o arquivo XML: {e}")
    
    def get_root(self):
        """Retorna o elemento raiz do XML."""
        return self.root

    def find_element(self, xpath_query):
        """Encontra um elemento no XML com base em uma consulta XPath.
        
        Usa o namespace correto para o XML da NF-e.
        """
        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}  # Namespace para consultas XPath
        try:
            # Executa a consulta XPath
            result = self.root.xpath(xpath_query, namespaces=namespaces)
            return result
        except Exception as e:
            raise Exception(f"Erro ao buscar o elemento com XPath '{xpath_query}': {e}")
    
    def pretty_print(self):
        """Imprime o XML de forma organizada."""
        try:
            print(etree.tostring(self.root, pretty_print=True, encoding='utf-8').decode('utf-8'))
        except Exception as e:
            raise Exception(f"Erro ao imprimir o XML: {e}")

if __name__ == "__main__":
    parser = XMLParser(xml_file_path) # type: ignore
