import pandas as pd
import numpy as np


def meanReversion(data: pd.DataFrame, lookback=10, numStd=2) -> pd.Series:
    """
    Mean reversion strategy

    Arguments:
        data (pd.DataFrame): historical data with 'close' price
        lookback (int): lookback period for Boll. Bands
        numStd (int): number of standard deviations for threshold
    Returns:
        pd.Series: position signals (1 = long, -1 = short, 0 = neutral)
    """

    data['mean'] = data['close'].rolling(window=lookback).mean()
    data['std'] = data['close'].rolling(window=lookback).std()

    # Bollinger Bands
    lower = data['mean'] - numStd * data['std']
    upper = data['mean'] + numStd * data['std']

    # Create signals
    signals = np.where(data['close'] < lower, 1,
                       np.where(data['close'] > upper, -1, 0))

    return pd.Series(signals, index=data.index)
