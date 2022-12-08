import numpy as np
import pandas as pd
import FinanceDataReader as fdr
from ecphysics.data.dataset.base_data import BaseDataset


class TimeSeriesDataset(BaseDataset):

    @classmethod
    def get_price_return_series(cls,
                                codes:list,
                                start_date:str,
                                end_date:str,
                                price_type:str = 'Close',
                                exchange:str = None,
                                log_return:bool = False
                                ):
        
        prices = pd.DataFrame()
        stock_list = list()
        for code in codes:
            try:
                price = cls.get_stock_price_data(code, start_date, end_date, exchange, [price_type])
                prices = pd.concat([prices, price], axis = 1)
                stock_list.append(code)
            except:
                continue
        prices.columns = stock_list
        prices = prices.dropna(axis = 0)
        if log_return:
            price_rtns = np.log(prices)-np.log(prices).shift(1)
        else:
            price_rtns = prices.pct_change(1)
        price_rtns = price_rtns.dropna(axis = 0)
        return price_rtns



