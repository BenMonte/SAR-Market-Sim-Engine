# Market-Sim-Engine

A modular Python tool for analyzing historical trade data. It calculates performance metrics from a trade journal and optionally generates AI-powered diagnostic commentary on strategy strengths and weaknesses.

This is **not** a live trading system or a prediction engine. It reads completed trade records and produces a structured performance report.

## Features

- **Trade data ingestion** — Loads and cleans trade records from an Excel file
- **Deterministic performance analytics** — Calculates win rate, expectancy, profit factor, drawdown, R-multiple statistics, and more
- **AI-powered strategy diagnostics** — Sends performance metrics to an LLM (OpenAI) to get a written analysis covering risk profile, sustainability, and areas for improvement
- **Modular design** — Each component (data loading, analytics, diagnostics) is isolated and independently testable

## Architecture

```
src/
├── data/
│   └── loader.py           # Trade data ingestion and preprocessing
├── analytics/
│   └── performance.py      # Performance metric calculations
├── diagnostics/
│   └── llm_diagnostics.py  # LLM-based strategy analysis

main.py                     # Entry point
TradeDatabase.xlsx           # Trade journal (Excel)
```

## Example Output

```
Market Simulation Engine Initialized

Loaded 830 trades from TradeDatabase.xlsx

=== Performance Summary ===
  Total Trades:          830
  Win Rate:              25.06%
  Expectancy (R):        0.31
  Average R:             0.31
  Avg Win R:             4.00
  Avg Loss R:            -0.92
  Profit Factor:         1.45
  Largest Win R:         25.76
  Largest Loss R:        -4.24
  Std Dev R:             3.11
  Max Consec. Losses:    18
  Max Drawdown:          36.88%

=== LLM Strategy Diagnostics ===
1. Structural Strengths
   - High average win at 4.00R, capturing substantial gains when successful
   - Positive expectancy of 0.31R confirms long-run profitability
   - Profit factor of 1.45 indicates profitability after accounting for losses

2. Structural Weaknesses
   - Low win rate of 25.06%, relying heavily on a few large wins
   - Max drawdown of 36.88% indicates significant capital reduction periods

3. Risk Profile
   - High-risk strategy due to low win rate and large drawdowns
   - May not suit all investors

4. Long-term Sustainability
   - High drawdown and psychological stress from consecutive losses
     may challenge sustainability for many investors

5. Trade Distribution Asymmetry
   - Large asymmetry between gains and losses
   - A few large wins offset many small losses

6. Volatility of Returns
   - Std Dev of 3.11R reflects significant volatility and unpredictable swings

7. Tail Risk Exposure
   - Largest loss at -4.24R and max drawdown of 36.88% suggest moderate-high tail risk

8. Psychological Difficulty
   - Very high: up to 18 consecutive losses can be psychologically taxing

9. Capital Efficiency
   - High drawdown and low win rate reduce capital efficiency
   - Requires substantial capital buffers to maintain positions

10. Areas for Improvement
   - Increase win rate to stabilize returns and reduce psychological stress
   - Implement risk management techniques to mitigate large drawdowns
   - Refine entry and exit rules to dampen return volatility
   - Explore diversification or hedging to protect against extreme losses
```

## Quickstart

1. Install dependencies:
   ```bash
   pip install pandas openpyxl openai
   ```
2. Run the engine:
   ```bash
   python main.py
   ```
3. **(Optional)** To enable AI-powered strategy diagnostics, set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
   If not configured, AI diagnostics will be skipped and all deterministic analytics will still run normally.

