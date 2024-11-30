import numpy as np
import pandas as pd


def momentum(data: pd.DataFrame, lookback=20, threshold=0.05) -> pd.Series:
    """
    Momentum strategy

    Arguments:
        data (pd.DataFrame): historical data with 'close' price
        lookback (int): lookback period to calculate momentum
        threshold (float): momentum threshold for entries and exits
    Returns:
        pd.Series: position signals (1 = long, -1 = short, 0 = neutral)
    """

    # Calculate price momentum in new column
    data['momentum'] = data['close'].pct_change(periods=lookback)

    # Create signals
    signals = np.where(data['momentum'] > threshold, 1, -1)

    return pd.Series(signals, index=data.index)
