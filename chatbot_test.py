"""
Main chatbot script
"""
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template =  """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# result = model.invoke(input="hello")

# result = chain.invoke({"context": "", "question": "how are you"})
# print(result)

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\n AI: {result}"

if __name__ == "__main__":
    handle_conversation()