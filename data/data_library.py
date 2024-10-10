class DataLibrary:
    def __init__(self):
        """Inicializa a biblioteca para armazenar os dados processados."""
        self.data = {}  # Armazena os dados em um dicionário

    def add_data(self, xml_file, parsed_data):
        """Adiciona os dados processados de um arquivo XML na biblioteca.
        
        Args:
            xml_file (str): Caminho do arquivo XML.
            parsed_data (dict): Dados processados do arquivo XML.
        """
        self.data[xml_file] = parsed_data

    def get_data(self, xml_file):
        """Recupera os dados processados para um arquivo XML específico.
        
        Args:
            xml_file (str): Caminho do arquivo XML.
            
        Returns:
            dict: Os dados processados do arquivo XML, ou None se não encontrado.
        """
        return self.data.get(xml_file)

    def get_all_data(self):
        """Recupera todos os dados processados da biblioteca.
        
        Returns:
            dict: Todos os dados armazenados.
        """
        return self.data

    def clear_data(self):
        """Limpa todos os dados armazenados na biblioteca."""
        self.data.clear()

    def remove_data(self, xml_file):
        """Remove os dados processados de um arquivo XML específico."""
        if xml_file in self.data:
            del self.data[xml_file]
