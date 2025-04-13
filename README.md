# Financial Assistant Agent

A Google ADK agent that provides financial calculations, currency conversions, and additional utilities.

## Features

- **Mortgage Calculator**: Calculate monthly payments based on loan amount, interest rate, and term
- **Currency Converter**: Convert between major currencies (USD, EUR, GBP, JPY)
- **Weather Information**: Get weather information for supported cities
- **Time Lookup**: Get current time for supported cities

## Setup

1. Set up a Python environment (3.10 or higher)
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Google ADK API key in the `.env` file
4. Run the example: `python main.py`

## Example Usage

```python
from multi_tool_agent.agent import root_agent

# Calculate mortgage
response = root_agent.generate(
    messages=[
        {"role": "user", "content": "Calculate monthly payment for a $300,000 loan with 4.5% interest over 30 years"}
    ]
)
print(response.text)

# Convert currency
response = root_agent.generate(
    messages=[
        {"role": "user", "content": "Convert 100 USD to EUR"}
    ]
)
print(response.text)
```

## Customization

You can customize this agent by:
1. Adding new tool functions in `multi_tool_agent/agent.py`
2. Modifying the agent configuration and description
3. Adding the new tool to the agent's tool list

## Requirements

- Python 3.10+
- Google ADK library
