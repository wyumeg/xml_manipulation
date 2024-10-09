import os
import asyncio
from parsers.parser_xml import XMLParser

# Caminho absoluto para o diretório do projeto
project_root = os.path.dirname(os.path.abspath(__file__))


async def process_xml_file(xml_file_path):
    """Processa um arquivo XML de forma assíncrona."""
    try:
        parser = XMLParser(xml_file_path)
        file_name = os.path.basename(xml_file_path)
        print(f"Arquivo XML {xml_file_path} carregado com sucesso.")
        
        # Exemplo: Extrair e exibir o nome do emitente
        emitente = parser.find_element('//nfe:emit/nfe:xNome')
        if emitente:
            print(f"Emitente do arquivo {file_name}: {emitente[0].text}")
        else:
            print(f"Emitente não encontrado no arquivo {xml_file_path}.")
        # Exemplo: Extrair e exibir o nome do destinatario
        destinatario = parser.find_element('//nfe:dest/nfe:xNome')
        if destinatario:
            print(f"Destinatário do arquivo {file_name}: {destinatario[0].text}")
        else:
            print(f"Destinatário não encontrado no arquivo {file_name}.")
            
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_name}: {e}")
        
async def main():
    # Pergunta ao usuário pela lista de arquivos XML (separados por vírgula)
    xml_files_input = input("Por favor, insira os caminhos completos para os arquivos XML, separados por vírgula: ")
    xml_files = [file.strip() for file in xml_files_input.split(',')]

    # Verifica se os arquivos fornecidos existem
    for xml_file in xml_files:
        if not os.path.exists(xml_file):
            print(f"Erro: O arquivo '{xml_file}' não foi encontrado.")
            return

    # Cria tarefas assíncronas para processar cada arquivo XML
    tasks = [process_xml_file(xml_file) for xml_file in xml_files]
    
    # Aguarda a conclusão de todas as tarefas
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Executa a função principal assíncrona
    asyncio.run(main())