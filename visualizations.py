import matplotlib.pyplot as plt

def plot_performance(returns, positions):
    """
    Generate performance visualizations
    """
    plt.figure(figsize=(12,8))
    plt.plot(returns.cumsum())
    plt.title('Cumulative Strategy Returns')
    plt.show()
