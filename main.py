from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent  # noqa: E402
from langchain_core.messages import HumanMessage  # noqa: E402
from langchain_google_genai import ChatGoogleGenerativeAI  # noqa: E402
from langchain_tavily import TavilySearch  # noqa: E402

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)
# llm_with_grounding = llm.bind(tools=[{"google_search": {}}])
# agent = create_agent(model=llm_with_grounding)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
