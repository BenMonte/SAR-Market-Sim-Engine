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

## Future Improvements

- Add time-based analytics (monthly/quarterly breakdowns)
- Visualize the equity curve and drawdown periods
- Support filtering by ticker, sector, or date range
- Export reports to PDF or HTML
