import numpy as np
import pandas as pd
import FinanceDataReader as fdr
from ecphysics.data.dataset.base import BaseDataset


class TimeSeriesDataset(BaseDataset):

    @classmethod
    def get_price_return_series(cls):
        return None