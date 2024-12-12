# Reference: https://microsoft.github.io/autogen/0.2/blog/2024/06/24/AltModels-Classes#function-calls

from typing import Literal

import autogen
from typing_extensions import Annotated

config_list = [
    {
        "model": "llama3.1",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
]

llm_config = {
    "config_list": config_list,
    "timeout": 120
}

currency_bot = autogen.AssistantAgent(
    name="currency_bot",
    system_message="For currency exchange tasks, only use the functions you have been provided with. Reply TERMINATE when the task in done",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="User proxy",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    code_execution_config= {
        "work_dir": "example/03-function-calling/coding",
        "use_docker": False
    }
)

CurrencySymbol = Literal["USD", 'EUR']

def exchange_rate(base_currency: CurrencySymbol, quote_currency: CurrencySymbol) -> float:
    if base_currency == quote_currency:
        return 1.0
    
    elif base_currency == "USD" and quote_currency == "EUR":
        return 1/1.09

    elif base_currency == "EUR" and quote_currency == "USD":
        return 1/1.1
    else:
        raise ValueError(f"Unsupported currency pair: {base_currency}-{quote_currency}")


@user_proxy.register_for_execution()
@currency_bot.register_for_llm(description="Currency exchange calculator")    
def currency_calculator( # Annotated: 'add context specific metadata for a type'
    base_amount: Annotated[float, "Amount of currency in base_currency"],
    base_currency: Annotated[CurrencySymbol, "Base currency"] = "USD",
    quote_currency: Annotated[CurrencySymbol, "Quote currency"] = "EUR"
    ) -> str:
    
    quote_amount = exchange_rate(base_currency, quote_currency) * base_amount
    return f"{quote_amount} - {quote_currency}"

user_proxy.initiate_chat(
    currency_bot,
    message="How much EUR can 1000 USD be exchanged to?"
)    