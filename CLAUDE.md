# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an early-stage AI-powered trading bot that uses the Anthropic Claude API as its intelligence layer. Currently in initial setup phase.

## Running the Bot

```bash
python bot.py
```
## Trading Rules
- RSI < 30 → Alım sinyali
- RSI > 70 → Satım sinyali
- Her zaman stop-loss kullan

## Code Style
- Türkçe yorum satırları
- Type hints zorunlu

## Dependencies

Install dependencies with:
```bash
pip install anthropic python-dotenv
```

No `requirements.txt` exists yet — consider creating one with `pip freeze > requirements.txt` once dependencies stabilize.

## Configuration

Copy `.env` and populate with your credentials:
- `ANTHROPIC_API_KEY` — required for the Anthropic SDK client

## Architecture

- **bot.py** — single entry point; initializes the Anthropic client via `anthropic` SDK and loads env vars via `python-dotenv`
- **.env** — local credentials (never commit this file)

The bot is designed to use Claude as the decision-making engine for trading logic. Trading strategies, market data ingestion, and order execution are not yet implemented.
