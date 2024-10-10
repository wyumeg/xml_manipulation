import os
import json
import asyncio
from extractors.report_generator import ReportGenerator

project_root = os.path.dirname(os.path.abspath(__file__))

async def main():
    
    # Caminhos para os arquivos de esquema JSON
    header_schema_path = os.path.join(project_root, 'schemas', 'header_schema.json')
    items_schema_path = os.path.join(project_root, 'schemas', 'items_schema.json')

    # Pergunta ao usuário se ele quer selecionar Arquivo(s) ou uma Pasta
    file_folder_selection = input("Por favor, insira o tipo de seleção (1.Arquivo(s) ou 2.Pasta): ").strip()
    
    if file_folder_selection == "1":
        xml_files_input = input("Insira os caminhos completos para os arquivos XML, separados por vírgula: ")
        xml_files = [file.strip() for file in xml_files_input.split(',')]
    elif file_folder_selection == "2":
        folder_path = input("Insira o caminho completo para a pasta contendo os arquivos XML: ").strip()
        xml_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xml')]
        if not xml_files:
            print(f"Nenhum arquivo XML encontrado na pasta '{folder_path}'.")
            return
    else:
        print("Seleção inválida.")
        return

    # Geração do relatório
    output_path = os.path.join(project_root, 'output', 'report.xlsx')
    report_generator = ReportGenerator(xml_files, header_schema_path, items_schema_path)
    report_generator.generate_report(output_path)

if __name__ == "__main__":
    asyncio.run(main())
