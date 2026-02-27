"""Market Simulation Engine entry point.

Loads historical trade data, computes performance analytics,
and optionally generates AI-powered strategy diagnostics.
"""

from dotenv import load_dotenv

load_dotenv()

from src.data.loader import load_trade_data
from src.analytics.performance import generate_performance_summary
from src.diagnostics.llm_diagnostics import generate_strategy_diagnostics


def main():
    """Run the simulation engine."""
    file_path = "TradeDatabase.xlsx"
    initial_capital = 10000

    print("Market Simulation Engine Initialized\n")

    df = load_trade_data(file_path)
    print(f"Loaded {len(df)} trades from {file_path}\n")

    summary = generate_performance_summary(df, initial_capital)

    print("=== Performance Summary ===")
    print(f"  Total Trades:          {summary['total_trades']}")
    print(f"  Win Rate:              {summary['win_rate']:.2%}")
    print(f"  Expectancy (R):        {summary['expectancy_r']:.2f}")
    print(f"  Average R:             {summary['average_r']:.2f}")
    print(f"  Avg Win R:             {summary['avg_win_r']:.2f}")
    print(f"  Avg Loss R:            {summary['avg_loss_r']:.2f}")
    print(f"  Profit Factor:         {summary['profit_factor']:.2f}")
    print(f"  Largest Win R:         {summary['largest_win_r']:.2f}")
    print(f"  Largest Loss R:        {summary['largest_loss_r']:.2f}")
    print(f"  Std Dev R:             {summary['std_r']:.2f}")
    print(f"  Max Consec. Losses:    {summary['max_consecutive_losses']}")
    print(f"  Max Drawdown:          {summary['max_drawdown']:.2%}")

    print("\n=== LLM Strategy Diagnostics ===")
    print(generate_strategy_diagnostics(summary))


if __name__ == "__main__":
    main()
  
