# Market-Sim-Engine

A modular Python research engine for simulating and evaluating systematic trading strategies. 

The system combines deterministic backtesting and performance analytics with an LLM-driven strategy diagnostics layer that analyzes trade distributions, drawdowns, and structural performance characteristics to identify weaknesses and risk dynamics.

## Core Components

- Trade data ingestion and cleaning
- Backtesting and simulation engine
- Performance & risk analytics (expectancy, drawdown, equity modeling)
- LLM-powered strategy diagnostics layer

## Architecture

src/
├── data/        # Trade data ingestion and preprocessing  
├── analytics/   # Performance, risk, and distribution analysis  
├── strategies/  # Strategy logic abstraction  
├── diagnostics/ # LLM-based evaluation layer  

main.py          # Execution entry point  
