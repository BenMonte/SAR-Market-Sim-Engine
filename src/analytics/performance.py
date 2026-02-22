"""Performance analytics module for a trading backtesting engine.

Provides modular, independently testable functions for calculating
trade-level performance metrics from a pandas DataFrame.
"""

import pandas as pd


def calculate_win_rate(df: pd.DataFrame) -> float:
    """Calculate the percentage of winning trades.

    Args:
        df: DataFrame with at minimum a 'Trade P&L ($)' column.

    Returns:
        Win rate as a float between 0.0 and 1.0.
    """
    if "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: Trade P&L ($)")
    total = len(df)
    if total == 0:
        return 0.0
    wins = (df["Trade P&L ($)"] > 0).sum()
    return float(wins / total)


def calculate_expectancy(df: pd.DataFrame) -> float:
    """Calculate expectancy in R-multiples.

    Expectancy = (win_rate × avg winning R) − (loss_rate × |avg losing R|)

    Args:
        df: DataFrame with at minimum 'Trade P&L ($)' and 'R-Multiple' columns.

    Returns:
        Expectancy as a float (in R).
    """
    if "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: Trade P&L ($)")
    if "R-Multiple" not in df.columns:
        raise ValueError("Missing required column: R-Multiple")
    if df.empty:
        return 0.0

    total = len(df)
    winners = df.loc[df["Trade P&L ($)"] > 0, "R-Multiple"]
    losers = df.loc[df["Trade P&L ($)"] <= 0, "R-Multiple"]

    win_rate = len(winners) / total
    loss_rate = len(losers) / total

    avg_win_r = float(winners.mean()) if not winners.empty else 0.0
    avg_loss_r = float(losers.abs().mean()) if not losers.empty else 0.0

    return float(win_rate * avg_win_r - loss_rate * avg_loss_r)


def calculate_average_r(df: pd.DataFrame) -> float:
    """Calculate the average R-multiple across all trades.

    Args:
        df: DataFrame with at minimum an 'R-Multiple' column.

    Returns:
        Average R-multiple as a float.
    """
    if "R-Multiple" not in df.columns:
        raise ValueError("Missing required column: R-Multiple")
    if df.empty:
        return 0.0
    return float(df["R-Multiple"].mean())


def calculate_equity_curve(
    df: pd.DataFrame, initial_capital: float
) -> pd.Series:
    """Build a cumulative equity curve from trade P&L.

    Args:
        df: DataFrame with at minimum a 'Trade P&L ($)' column.
        initial_capital: Starting capital in dollars.

    Returns:
        A pandas Series representing equity value after each trade,
        starting from initial_capital at index 0.
    """
    if "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: Trade P&L ($)")
    cumulative_pnl = df["Trade P&L ($)"].cumsum()
    equity_curve = initial_capital + cumulative_pnl
    equity_curve = pd.concat(
        [pd.Series([initial_capital]), equity_curve]
    ).reset_index(drop=True)
    return equity_curve


def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    """Calculate the maximum drawdown from an equity curve.

    Max drawdown is the largest peak-to-trough decline expressed as a
    positive fraction (0.0 – 1.0).

    Args:
        equity_curve: A pandas Series of equity values over time.

    Returns:
        Maximum drawdown as a positive float between 0.0 and 1.0.
    """
    if equity_curve.empty:
        return 0.0
    running_max = equity_curve.cummax()
    drawdowns = (equity_curve - running_max) / running_max
    return float(drawdowns.min() * -1)


def calculate_average_win_r(df: pd.DataFrame) -> float:
    """Calculate the average R-multiple of winning trades."""
    if "R-Multiple" not in df.columns or "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: R-Multiple or Trade P&L ($)")
    winners = df.loc[df["Trade P&L ($)"] > 0, "R-Multiple"]
    return float(winners.mean()) if not winners.empty else 0.0


def calculate_average_loss_r(df: pd.DataFrame) -> float:
    """Calculate the average R-multiple of losing trades (returned as negative)."""
    if "R-Multiple" not in df.columns or "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: R-Multiple or Trade P&L ($)")
    losers = df.loc[df["Trade P&L ($)"] <= 0, "R-Multiple"]
    return float(losers.mean()) if not losers.empty else 0.0


def calculate_profit_factor(df: pd.DataFrame) -> float:
    """Calculate profit factor (gross wins / gross losses in R)."""
    if "R-Multiple" not in df.columns or "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: R-Multiple or Trade P&L ($)")
    gross_win = df.loc[df["Trade P&L ($)"] > 0, "R-Multiple"].sum()
    gross_loss = df.loc[df["Trade P&L ($)"] <= 0, "R-Multiple"].abs().sum()
    if gross_loss == 0:
        return float("inf") if gross_win > 0 else 0.0
    return float(gross_win / gross_loss)


def calculate_largest_win_r(df: pd.DataFrame) -> float:
    """Return the largest winning R-multiple."""
    if "R-Multiple" not in df.columns:
        raise ValueError("Missing required column: R-Multiple")
    if df.empty:
        return 0.0
    return float(df["R-Multiple"].max())


def calculate_largest_loss_r(df: pd.DataFrame) -> float:
    """Return the largest losing R-multiple (most negative)."""
    if "R-Multiple" not in df.columns:
        raise ValueError("Missing required column: R-Multiple")
    if df.empty:
        return 0.0
    return float(df["R-Multiple"].min())


def calculate_std_r(df: pd.DataFrame) -> float:
    """Calculate the standard deviation of R-multiples."""
    if "R-Multiple" not in df.columns:
        raise ValueError("Missing required column: R-Multiple")
    if df.empty:
        return 0.0
    return float(df["R-Multiple"].std())


def calculate_max_consecutive_losses(df: pd.DataFrame) -> int:
    """Calculate the longest streak of consecutive losing trades."""
    if "Trade P&L ($)" not in df.columns:
        raise ValueError("Missing required column: Trade P&L ($)")
    if df.empty:
        return 0
    is_loss = (df["Trade P&L ($)"] <= 0).astype(int)
    streaks = is_loss.groupby((is_loss != is_loss.shift()).cumsum()).sum()
    return int(streaks.max()) if not streaks.empty else 0


def generate_performance_summary(
    df: pd.DataFrame, initial_capital: float
) -> dict:
    """Generate a structured performance summary for a set of trades.

    Args:
        df: DataFrame with columns 'Trade P&L ($)', 'Trade Return (%)',
            and 'R-Multiple'.
        initial_capital: Starting capital in dollars.

    Returns:
        Dictionary with keys: total_trades, win_rate, expectancy_r,
        average_r, max_drawdown, avg_win_r, avg_loss_r, profit_factor,
        largest_win_r, largest_loss_r, std_r, max_consecutive_losses.
    """
    equity_curve = calculate_equity_curve(df, initial_capital)

    return {
        "total_trades": len(df),
        "win_rate": calculate_win_rate(df),
        "expectancy_r": calculate_expectancy(df),
        "average_r": calculate_average_r(df),
        "max_drawdown": calculate_max_drawdown(equity_curve),
        "avg_win_r": calculate_average_win_r(df),
        "avg_loss_r": calculate_average_loss_r(df),
        "profit_factor": calculate_profit_factor(df),
        "largest_win_r": calculate_largest_win_r(df),
        "largest_loss_r": calculate_largest_loss_r(df),
        "std_r": calculate_std_r(df),
        "max_consecutive_losses": calculate_max_consecutive_losses(df),
    }
