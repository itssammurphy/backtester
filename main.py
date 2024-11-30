import pandas as pd
import numpy as np
from tester import StrategyBacktest
from strategies.MA_crossover import movingAverageCrossover
from strategies.M_reversion import meanReversion
from strategies.momentum import momentum

DATA_SRC = './data/XJO_bigger_minute.csv'


if __name__ == "__main__":
    data = pd.read_csv(DATA_SRC, parse_dates=['date'], index_col='date')

    test_MAC = StrategyBacktest(
        data, movingAverageCrossover, shortWindow=5, longWindow=46)
    test_MAC.run()
    test_MAC.perfSummary()
    test_MAC.plot()
