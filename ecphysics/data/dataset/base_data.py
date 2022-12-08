import FinanceDataReader as fdr
from collections import defaultdict
import pandas as pd

class BaseDataset():

    @classmethod
    def get_stock_listing_info(cls,
                               market:str='KOSPI'
                               )-> dict:


        rst = defaultdict(dict)
        stocks = fdr.StockListing(market)
        columns = stocks.columns
        stock_key = list(set(['Symbol', 'Code']).intersection(set(columns)))
        if len(stock_key)==0:
            raise ValueError('listing info is empty')
        stock_key = stock_key[0]
        name_key = list(set(['Name', 'name']).intersection(columns))
        name_key = name_key[0] if len(name_key) !=0 else None
        ind_key = list(set(['Industry', 'Sector']).intersection(columns))
        ind_key = ind_key[0] if len(ind_key) !=0 else None

        for i in range(len(stocks)):
            stock_info = dict()
            stock = stocks.iloc[i][stock_key]
            stock_info['name'] = stocks.iloc[i][name_key] if name_key is not None else None
            stock_info['industry'] = stocks.iloc[i][ind_key] if ind_key is not None else None
            rst[stock] = stock_info

        return rst

    @classmethod
    def get_stock_price_data(cls,
                  code:str,
                  start_date:str = None,
                  end_date:str = None,
                  exchange:str = None,
                  price_type:list = ['Close'] 
                  )->pd.DataFrame:
        
        try:
            stock_prices = fdr.DataReader(code, start_date, end_date, exchange=exchange)
        except:
            raise ValueError('check code and exchange')

        return stock_prices[price_type]
    

        
