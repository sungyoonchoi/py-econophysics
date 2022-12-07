from enum import Enum

class BaseEnum(Enum):

    @classmethod
    def to_dict(cls, key_val_change = False):
        
        if key_val_change:
            return dict(map(lambda item: (item.value, item.name), cls))
        else:
            return dict(map(lambda item: (item.name, item.value), cls))

    @classmethod
    def to_name_list(cls):
        return list(map(lambda item: item.name, cls))

    @classmethod
    def to_value_list(cls):
        return list(map(lambda item: item.value, cls))




class StockMarket(BaseEnum):
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
