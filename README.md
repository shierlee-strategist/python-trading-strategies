# Mean Reversion Trading Strategy

## Overview
A sophisticated algorithmic trading system implementing statistical arbitrage principles in Python, designed for modern markets.

## Core Features
- **Mean Reversion Implementation**: Z-score based statistical arbitrage
- **Risk Management**: Position limits (0.1% max per position), dollar-neutral exposure
- **Performance Metrics**: 
  - Target Sharpe Ratio: ~0.8
  - Market Neutral Design (Beta < 0.1)
  - Controlled Maximum Drawdown

## Technical Stack
- Python 3.8+
- NumPy/Pandas for data processing
- Matplotlib for visualization
- SciPy for statistical analysis

## Quick Start
```bash
pip install -r requirements.txt
python mean_reversion_strategy.py

Project Structure
mean_reversion_strategy.py: Core strategy implementation
performance_analysis.py: Performance metrics calculation
visualizations.py: Trading results visualization
crypto_adaptation.md: Crypto market implementation notes
