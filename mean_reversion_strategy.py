import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class MeanReversionStrategy:
    def __init__(self):
        # Strategy parameters
        self.RETURNS_LOOKBACK_DAYS = 5
        self.MAX_GROSS_EXPOSURE = 1.0
        self.MAX_POSITION_SIZE = 0.001
        self.PERCENTILE_THRESHOLD = 10  # Top/bottom 10%

    def calculate_returns(self, prices):
        """
        Calculate rolling returns for given price data
        """
        return prices.pct_change(self.RETURNS_LOOKBACK_DAYS)

    def calculate_zscore(self, returns):
        """
        Convert returns to z-scores for normalization
        """
        return (returns - returns.mean()) / returns.std()

    def select_securities(self, zscore_returns):
        """
        Select securities in top/bottom percentiles
        """
        lower_percentile = np.percentile(zscore_returns, self.PERCENTILE_THRESHOLD)
        upper_percentile = np.percentile(zscore_returns, 100 - self.PERCENTILE_THRESHOLD)
        
        long_signals = zscore_returns <= lower_percentile
        short_signals = zscore_returns >= upper_percentile
        
        return long_signals, short_signals

    def calculate_positions(self, long_signals, short_signals, prices):
        """
        Calculate position sizes with risk management
        """
        # Initialize position sizes
        position_sizes = pd.Series(0.0, index=prices.index)
        
        # Set long positions
        num_longs = long_signals.sum()
        if num_longs > 0:
            position_sizes[long_signals] = self.MAX_GROSS_EXPOSURE / (2 * num_longs)
            
        # Set short positions
        num_shorts = short_signals.sum()
        if num_shorts > 0:
            position_sizes[short_signals] = -self.MAX_GROSS_EXPOSURE / (2 * num_shorts)
            
        # Apply position size limits
        position_sizes = position_sizes.clip(
            lower=-self.MAX_POSITION_SIZE,
            upper=self.MAX_POSITION_SIZE
        )
        
        return position_sizes

    def run_strategy(self, prices):
        """
        Execute the mean reversion strategy
        """
        # Calculate returns and z-scores
        returns = self.calculate_returns(prices)
        zscore_returns = self.calculate_zscore(returns)
        
        # Generate trading signals
        long_signals, short_signals = self.select_securities(zscore_returns)
        
        # Calculate position sizes
        positions = self.calculate_positions(long_signals, short_signals, prices)
        
        return positions

    def calculate_portfolio_stats(self, positions, prices):
        """
        Calculate strategy performance metrics
        """
        returns = prices.pct_change()
        strategy_returns = (positions.shift() * returns).sum(axis=1)
        
        stats = {
            'sharpe_ratio': np.sqrt(252) * strategy_returns.mean() / strategy_returns.std(),
            'annual_return': 252 * strategy_returns.mean(),
            'max_drawdown': (strategy_returns.cumsum() - strategy_returns.cumsum().cummax()).min()
        }
        
        return stats

if __name__ == "__main__":
    # Example usage
    strategy = MeanReversionStrategy()
    # Add your data loading and strategy execution code here
