# =============== simple chatbot by using LLM
# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# # Load environment variables
# load_dotenv()

# # Initialize LLM
# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7
# )

# print("Chatbot Started (type 'exit' to quit)\n")

# while True:
#     user_input = input("You: ").strip()
#     if user_input.lower() == "exit":
#         print("Bot: Goodbye!")
#         break
#     response = llm.invoke(user_input)
#     print(f"Bot: {response.content}\n")


# ===================== chat by using llm and also it stores data so its now the continuevity 

# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7
# )

# messages = []

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break
#     messages.append(("human", user_input))
#     response = llm.invoke(messages)
#     print("Bot:", response.content)

#     messages.append(("ai", response.content))


# ================================ NEW CHATBOT USING LLM 
