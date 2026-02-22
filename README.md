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
### Structural Strengths
- High reward-to-risk ratio (Avg Win 4.00R vs Avg Loss -0.92R)
- Profit factor of 1.45 confirms aggregate profitability

### Structural Weaknesses
- Low win rate (25.06%) requires psychological resilience
- Max drawdown of 36.88% indicates significant equity retracement periods

### Risk Profile
- High-risk profile driven by large drawdowns and low win rate
- Profitability depends on outsized winners relative to frequent small losses

### Long-term Sustainability
- Sustainable if capital reserves can absorb drawdowns
- Requires strict discipline and consistent trade execution

### Trade Distribution Asymmetry
- Highly asymmetric: largest win (25.76R) far exceeds largest loss (-4.24R)

### Volatility of Returns
- Std Dev of 3.11R indicates significant variability in outcomes

### Tail Risk Exposure
- Positive tail risk from large winners is beneficial
- 18 consecutive losses highlights negative tail risk

### Psychological Difficulty
- Low win rate and long losing streaks make this system mentally demanding

### Capital Efficiency
- Requires significant capital buffer to withstand drawdowns

### Areas for Improvement
- Refine entry criteria to improve win rate
- Implement tighter risk controls to reduce max drawdown
- Consider dynamic position sizing to manage volatility
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

