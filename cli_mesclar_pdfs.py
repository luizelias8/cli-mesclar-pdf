import argparse
import os
import glob
from PyPDF2 import PdfMerger

__version__ = '1.0.1'

def mesclar_pdfs(arquivos_entrada, caminho_saida):
    """Função para mesclar PDF usando PyPDF2."""

    try:
        # Cria uma instância do PdfMerger que será usada para mesclar os arquivos PDF
        merger = PdfMerger()

        # Loop sobre cada arquivo PDF na lista de arquivos de entrada
        for pdf in arquivos_entrada:
            # Adiciona o PDF atual ao objeto merger
            merger.append(pdf)

         # Escreve o conteúdo dos PDFs mesclados em um novo arquivo PDF no caminho de saída
        merger.write(caminho_saida)

         # Fecha o objeto merger para liberar recursos
        merger.close()

        print(f'PDFs mesclados com sucesso! Arquivo de saída: {caminho_saida}')

    except Exception as e:
        # Captura qualquer exceção que ocorra durante o processo de mesclagem
        print('Ocorreu um erro ao tentar mesclar os PDFs.')

        # Imprime a mensagem de erro detalhada
        print(f'Mensagem de erro: {e}')

def coletar_pdfs(caminhos_entrada):
    pdfs = []
    for caminho in caminhos_entrada:
        caminho_absoluto = os.path.abspath(caminho)
        if os.path.isfile(caminho_absoluto):
            if caminho_absoluto.lower().endswith('.pdf'):
                pdfs.append(caminho_absoluto)
            else:
                print(f'Arquivo ignorado (não é PDF): {caminho_absoluto}')
        elif os.path.isdir(caminho_absoluto):
            # Adiciona todos os arquivos PDF no diretório (recursivamente)
            pdfs.extend(glob.glob(os.path.join(caminho_absoluto, '**', '*.pdf'), recursive=True))
        else:
            print(f'Caminho inválido ignorado: {caminho_absoluto}')
    return pdfs

def obter_caminho_saida(caminho_saida):
    # Define o caminho padrão para o arquivo de saída como "mesclado.pdf" no diretório atual
    caminho_padrao = os.path.join(os.getcwd(), 'mesclado.pdf')

    # Verifica se foi fornecido um caminho de saída
    if caminho_saida:
        # Converte o caminho fornecido para um caminho absoluto
        caminho_absoluto = os.path.abspath(caminho_saida)

        # Verifica se o caminho fornecido termina com ".pdf", ou seja, é um arquivo PDF
        if caminho_absoluto.lower().endswith('.pdf'):
            # Obtém o diretório onde o arquivo PDF será salvo
            diretorio = os.path.dirname(caminho_absoluto)
            # Verifica se o diretório do arquivo PDF existe
            if os.path.exists(diretorio):
                return caminho_absoluto # Retorna o caminho completo do arquivo PDF especificado
            else:
                # Se o diretório não existir, retorna o caminho padrão
                return caminho_padrao

        # Verifica se o caminho fornecido é um diretório
        elif os.path.isdir(caminho_absoluto):
            # Verifica se o diretório especificado existe
            if os.path.exists(caminho_absoluto):
                # Retorna o caminho completo do arquivo "mesclado.pdf" dentro do diretório especificado
                return os.path.join(caminho_absoluto, 'mesclado.pdf') # Retorna o diretório com "mesclado.pdf"
            else:
                # Se o diretório não existir, retorna o caminho padrão
                return caminho_padrao

        else:
             # Se o caminho não for um arquivo PDF nem um diretório válido, retorna o caminho padrão
            return caminho_padrao
    else:
        # Se nenhum caminho for fornecido, retorna o caminho padrão
        return caminho_padrao

def main():
    parser = argparse.ArgumentParser(description='Mesclar arquivos PDF usando PyPDF2.')
    parser.add_argument('pdfs', nargs='+', help='Lista de arquivos PDF ou diretórios contendo PDFs a serem mesclados.')
    parser.add_argument('-o', '--output', help="Caminho do arquivo PDF de saída. Se não fornecido ou se o caminho não existir, salvará como 'mesclado.pdf' no diretório atual.")
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    # Obtém o caminho do arquivo de saída
    arquivo_saida = obter_caminho_saida(args.output)

    # Coleta todos os PDFs dos caminhos fornecidos
    arquivos_entrada = coletar_pdfs(args.pdfs)

    mesclar_pdfs(arquivos_entrada, arquivo_saida)

if __name__ == '__main__':
    main()