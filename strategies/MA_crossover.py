import numpy as np
import pandas as pd


def movingAverageCrossover(
    data: pd.DataFrame,
    shortWindow=50,
    longWindow=200
) -> pd.Series:
    """
    Moving Average Crossover strategy signal generator

    Arguments:
        data (pd.DataFrame): historical data with 'close' prices
        shortWindow (int): short-term moving average window
        longWindow (int): long-term moving average window
    Returns:
        pd.Series: position signals (1 = long, -1 = short, 0 = neutral)
    """

    # Calculate short- and long-term moving averages
    data['shortMA'] = data['close'].rolling(window=shortWindow).mean()
    data['longMA'] = data['close'].rolling(window=longWindow).mean()

    # Create signals
    signals = np.where(data['shortMA'] > data['longMA'], 1, -1)

    return pd.Series(signals, index=data.index)
