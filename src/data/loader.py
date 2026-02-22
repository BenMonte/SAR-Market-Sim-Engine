"""Trade data ingestion and preprocessing."""

import os

import pandas as pd


def load_trade_data(filepath: str) -> pd.DataFrame:
    """Load trade-level data from an Excel file.

    Reads the file, drops fully empty rows, converts numeric columns
    where possible, and sorts by 'Entry Date' if the column exists.

    Args:
        filepath: Path to the Excel (.xlsx) file.

    Returns:
        A cleaned pandas DataFrame of trade data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_excel(filepath, engine="openpyxl")

    # Drop rows where every value is NaN
    df = df.dropna(how="all")

    # Drop rows without a completed Trade P&L (open/pending trades)
    if "Trade P&L ($)" in df.columns:
        df = df.dropna(subset=["Trade P&L ($)"])

    # Strip trailing " R" suffix from R-Multiple column (e.g. "1.52 R" → 1.52)
    if "R-Multiple" in df.columns:
        df["R-Multiple"] = (
            df["R-Multiple"]
            .astype(str)
            .str.replace(r"\s*R$", "", regex=True)
        )

    # Convert columns to numeric where possible, leaving others untouched
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except (ValueError, TypeError):
            pass

    # Sort by entry date if the column exists
    if "Entry Date" in df.columns:
        df = df.sort_values(by="Entry Date").reset_index(drop=True)

    return df
