"""
Main chatbot script
"""

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from db import store_conversation
from api import get_stock_price
from utils import format_response, extract_symbol

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        try:
            print("user_input---------------------:" + str(user_input))
            if "stock price" in user_input.lower():
                # symbol = user_input.split()[-1]
                symbol = extract_symbol(user_input)
                if not symbol:
                    result = "I couldn't find a valid stock symbol in your query."
                price = get_stock_price(symbol)
                print("price is---------------------:" + str(price))
                result = f"The current price of {symbol} is {price}."
            else:
                result = chain.invoke({"context": context, "question": user_input})

            print("Bot: ", result)
            formatted_response = format_response(user_input, result)
            store_conversation(user_input, result)
            context += f"\nUser: {user_input}\nAI: {result}"

        except Exception as e:
            print(f"Sorry, something went wrong: {e}")

if __name__ == "__main__":
    handle_conversation()