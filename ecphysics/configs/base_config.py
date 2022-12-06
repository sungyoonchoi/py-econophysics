from enum import Enum


class StockMarket(Enum):
    코스피 = 'KOSPI'
    코스닥 = 'KOSDAQ'
    뉴욕거래소 = 'NYSE'
    나스닥   = 'NASDAQ'
    아멕스 = 'AMEX'
    SP500 = 'S&P500'
    상해거래소 = 'SSE'
    신천거래소 = 'SZSE'
    홍콩거래소 = 'HKEX'
    도쿄거래소 = 'TSE'
    호치민거래소 = 'HOSE'

    @classmethod
    def to_dict(cls):
        return dict(map(lambda item: (item.name, item.value), cls))
