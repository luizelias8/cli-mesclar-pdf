# CLI Mesclar PDFs

## Descrição

Script em Python que mescla vários arquivos PDF em um único PDF usando a linha de comando (CLI). Utiliza a biblioteca PyPDF2 para manipulação de PDFs e suporta a mesclagem de arquivos a partir de diretórios ou caminhos específicos.

## Funcionalidades

- Mesclagem de PDFs: Mescla múltiplos arquivos PDF em um único PDF.

- Suporte a Diretórios: Pode mesclar todos os PDFs presentes em um diretório.

- Argumentos de Linha de Comando: Suporte a parâmetros para especificar arquivos de entrada e saída diretamente na linha de comando.

## Pré-requisitos

- Python 3.x

## Instalação

1. Clone o repositório para sua máquina local:
```
git clone https://github.com/luizelias8/cli-mesclar-pdfs.git
cd cli-mesclar-pdfs
```

2. Instale as dependências necessárias:
```
pip install -r requirements.txt
```

## Uso

Você pode utilizar o script diretamente da linha de comando. Abaixo estão os parâmetros disponíveis e exemplos de uso.

### Parâmetros

- `-o`, `--output`: Caminho do arquivo PDF de saída. Se não fornecido, o PDF mesclado será salvo como mesclado.pdf no diretório atual.
- `pdfs`: Lista de arquivos PDF ou diretórios contendo PDFs a serem mesclados.

### Exemplos

Mesclando arquivos PDF específicos
```
python cli_mesclar_pdfs.py -o caminho/para/saida/mesclado.pdf caminho/para/arquivo1.pdf caminho/para/arquivo2.pdf
```

Mesclando todos os PDFs de um diretório
```
python cli_mesclar_pdfs.py -o caminho/para/saida/mesclado.pdf caminho/para/diretorio
```

Sem especificar o caminho de saída
```
python cli_mesclar_pdfs.py caminho/para/arquivo1.pdf caminho/para/arquivo2.pdf
```
O arquivo de saída será salvo como `mesclado.pdf` no diretório atual.

## Contribuição

Contribuições são bem-vindas!

## Autor

- [Luiz Elias](https://github.com/luizelias8)