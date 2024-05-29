def csv_reader(path: str) -> list:
    """
    Inicializa uma lista vazia para armazenar os dados
    Usa o gerenciador de contexto `with` para abrir o arquivo
    Cria um objeto leitor de CSV
    Itera sobre as linhas do arquivo CSV
    Adiciona cada linha (um dicionário) à lista de dados
    Exibe os dados lidos do arquivo CSV

    Args:
        path (str): caminho do arquivo csv

    Returns:
        list: retorno da função. Uma lista com dicionarios
    """
    import csv
    covid_data: list = list()

    with open(file=path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(f=csv_file, delimiter=';')

        for l in csv_reader:
            covid_data.append(l)

    for d in covid_data:
        print(d)


csv_reader(path='arquivo.csv')
