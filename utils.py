"""
Utility functions (e.g., response formatting)
"""
symbol_mapping = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "google": "GOOGL",
}

def format_response(user_input, bot_response):
    return f"You asked: {user_input}\nBot response: {bot_response}"

def extract_symbol(user_input):
    user_input_lower = user_input.lower()
    for name, symbol in symbol_mapping.items():
        if name in user_input_lower:
            return symbol
    return None