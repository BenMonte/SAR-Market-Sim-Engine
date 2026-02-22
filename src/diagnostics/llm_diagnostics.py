"""LLM-based strategy diagnostics module.

Interprets structured performance metrics and generates
strategy-level critiques and insights via the OpenAI API.
"""

import os

from openai import OpenAI


def build_diagnostics_prompt(metrics: dict) -> list[dict]:
    """Build structured chat messages for the diagnostics prompt.

    Args:
        metrics: Performance summary dictionary.

    Returns:
        A list of message dicts with 'role' and 'content' keys.
    """
    system_message = (
        "You are a quantitative trading strategy analyst. "
        "You interpret structured performance metrics and deliver "
        "concise, data-driven diagnostic assessments."
    )

    user_message = (
        "The following performance metrics come from a momentum / trend-following "
        "equity strategy:\n\n"
        f"  Total Trades:          {metrics['total_trades']}\n"
        f"  Win Rate:              {metrics['win_rate']:.2%}\n"
        f"  Expectancy (R):        {metrics['expectancy_r']:.2f}\n"
        f"  Avg Win R:             {metrics['avg_win_r']:.2f}\n"
        f"  Avg Loss R:            {metrics['avg_loss_r']:.2f}\n"
        f"  Profit Factor:         {metrics['profit_factor']:.2f}\n"
        f"  Largest Win R:         {metrics['largest_win_r']:.2f}\n"
        f"  Largest Loss R:        {metrics['largest_loss_r']:.2f}\n"
        f"  Std Dev R:             {metrics['std_r']:.2f}\n"
        f"  Max Consec. Losses:    {metrics['max_consecutive_losses']}\n"
        f"  Max Drawdown:          {metrics['max_drawdown']:.2%}\n\n"
        "Based on these metrics, provide a concise and structured analysis covering:\n"
        "1. Structural strengths of this strategy\n"
        "2. Structural weaknesses of this strategy\n"
        "3. Risk profile commentary\n"
        "4. Long-term sustainability assessment\n"
        "5. Trade distribution asymmetry\n"
        "6. Volatility of returns\n"
        "7. Tail risk exposure\n"
        "8. Psychological difficulty of the system\n"
        "9. Capital efficiency implications\n"
        "10. Specific areas for improvement\n\n"
        "Be direct, data-driven, and actionable."
    )

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]


def generate_strategy_diagnostics(metrics: dict) -> str:
    """Generate an LLM-powered diagnostic analysis of a trading strategy.

    Args:
        metrics: A dictionary containing:
            - total_trades (int)
            - win_rate (float)
            - expectancy_r (float)
            - max_drawdown (float)
            - avg_win_r (float)
            - avg_loss_r (float)
            - profit_factor (float)
            - largest_win_r (float)
            - largest_loss_r (float)
            - std_r (float)
            - max_consecutive_losses (int)

    Returns:
        The LLM-generated analysis string.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "LLM diagnostics unavailable — OPENAI_API_KEY not configured."

    client = OpenAI(api_key=api_key)
    messages = build_diagnostics_prompt(metrics)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM diagnostics failed — {e}"