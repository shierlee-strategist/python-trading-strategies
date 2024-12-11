import numpy as np

def calculate_metrics(returns):
    """
    Calculate key performance metrics
    """
    sharpe = returns.mean() / returns.std() * np.sqrt(252)
    max_drawdown = (returns.cumsum() - returns.cumsum().cummax()).min()
    return {
        'sharpe_ratio': sharpe,
        'max_drawdown': max_drawdown,
        'annual_return': returns.mean() * 252
    }
