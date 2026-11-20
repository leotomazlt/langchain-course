from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

llm = ChatOllama(model="qwen3:1.7b")
tools = [TavilySearch(max_results=3)]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage("What is the weather in Tokyo?")})
    print(result)

if __name__ == "__main__":
    main()