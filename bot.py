# Trading botu v1.0
import anthropic
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

print("KEY:", os.environ.get("ANTHROPIC_API_KEY"))  # test satırı


def calculate_rsi(prices: list, period: int = 14):
    if len(prices) < period + 1:
        return None

    gains = []
    losses = []
    for i in range(1, period + 1):
        change = prices[i] - prices[i - 1]
        if change >= 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# hook test
# hook test 2