from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    """Função que ao passar como parâmetro uma data no formato date exemplo: 01/01/2021, retornará uma string """
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    """Função que ao passar como parâmetro uma data no formato str exemplo: "01/01/2021", retornará um date """
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    """ Função para formatar moeda em REAL """
    return f'R$ {valor:,.2f}'

