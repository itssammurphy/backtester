import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

NUM_TRADING_DAYS = 252


class StrategyBacktest:
    def __init__(self, data: pd.DataFrame, strategy, **strategyParams):
        """
        Initialise the backtesting tool for a given strategy

        Arguments:
            data (pd.DataFrame): historical data with 'close' prices
            strategy (function): signal generator function
            strategyParams (dict): parameters for the signal generator
        """
        self.data = data.copy()
        self.strategy = strategy
        self.strategyParams = strategyParams

        # Position: 1 = long, -1 = short, 0 = neutral
        self.data['position'] = 0

        # log returns and returns from strategy
        self.data['returns'] = 0
        self.data['stratReturns'] = 0

    def applyStrategy(self):
        """
        Generate the trading signals for a given strategy and log them
        """
        self.data['position'] = self.strategy(self.data, **self.strategyParams)

    def calcReturns(self):
        """
        Calculate returns for a portfolio with the given strategy
        """
        self.data['returns'] = np.log(
            self.data['close'] / self.data['close'].shift(1))
        self.data['stratReturns'] = self.data['position'].shift(
            1) * self.data['returns']

    def run(self):
        """
        Run the backtest itself
        """
        self.applyStrategy()
        self.calcReturns()

    def perfSummary(self):
        """
        Produce a performance summary for the strategy
        """
        totalReturn = self.data['stratReturns'].sum()
        annualReturn = totalReturn / len(self.data) * NUM_TRADING_DAYS

        # Sharpe Ratio describes risk-adjusted return; the value in holding
        # a more volatile asset in potential returns (in this case annualised)
        sharpeRatio = self.data['stratReturns'].mean(
        ) / self.data['stratReturns'].std() * np.sqrt(NUM_TRADING_DAYS)

        print(f"Total Returns: {totalReturn:.2%}")
        # print(f"Annualised Returns: {annualReturn:.2%}")
        print(f"Sharpe: {sharpeRatio:.2f}")

    def plot(self):
        """
        Plot equity curve for this strategy
        """

        # Build new columns in dataframe for strategy and market returns
        self.data['cumReturns'] = self.data['stratReturns'].cumsum().apply(
            np.exp)
        self.data['cumMarket'] = self.data['returns'].cumsum().apply(np.exp)

        # Build the Pyplot figure
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['cumReturns'], label="Strategy")
        plt.plot(self.data['cumMarket'], label="Market", linestyle="dotted")
        plt.title("Equity Curve on Backtest")
        plt.legend()
        plt.show()
