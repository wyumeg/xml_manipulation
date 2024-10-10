import json
import os
from openpyxl import Workbook
from extractors.xml_processor import XMLProcessor

class ReportGenerator:
    def __init__(self, xml_files, report1_nfe_path, report2_items_path):
        self.xml_files = xml_files
        self.nfe_schema = self.load_schema(report1_nfe_path)
        self.items_schema = self.load_schema(report2_items_path)

    def load_schema(self, schema_path):
        """Carrega o esquema JSON."""
        try:
            with open(schema_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar o esquema {schema_path}: {e}")
            return None

    def generate_report(self, output_path):
        """Gera o relatório XLSX com base nos esquemas fornecidos."""
        wb = Workbook()
        
        # Processar cabeçalhos
        header_sheet = wb.active
        header_sheet.title = "Cabeçalhos"
        header_data = self.process_group(self.nfe_schema)
        self.write_to_sheet(header_sheet, header_data)

        # Processar itens
        item_sheet = wb.create_sheet(title="Itens")
        item_data = self.process_group(self.items_schema)
        self.write_to_sheet(item_sheet, item_data)

        # Salvar o arquivo XLSX
        wb.save(output_path)
        print(f"Relatório XLSX gerado em: {output_path}")

    def process_group(self, schema):
        """Processa os arquivos XML de acordo com o esquema fornecido."""
        all_data = []
        for xml_file in self.xml_files:
            processor = XMLProcessor(xml_file, schema)
            extracted_data = processor.process()
            all_data.append(extracted_data)
        return all_data

    def write_to_sheet(self, sheet, data):
        """Escreve os dados extraídos no arquivo XLSX."""
        if not data:
            return
        
        # Escrever cabeçalhos (nomes das tags)
        headers = data[0].keys() if data else []
        sheet.append(headers)
        
        # Escrever os dados
        for entry in data:
            row = [entry.get(key, "") for key in headers]
            sheet.append(row)
