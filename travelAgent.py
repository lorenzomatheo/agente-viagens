from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType,create_react_agent,AgentExecutor
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain import hub




# Inicializa o modelo de linguagem
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Configura a API do Wikipedia
wiki_api_wrapper = WikipediaAPIWrapper()

query = """
Vou viajar para França em julho de 2025. Quero que faça um roteiro de viagens para mim com os eventos que irão ocorrer na data da viagem 
e com o preço de passagem de São Paulo pra Londres
"""

def researchAgent(query, llm):
    tools = [WikipediaQueryRun(api_wrapper=wiki_api_wrapper)]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm,tools, prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools,prompt=prompt,verbose=True)
    webContext = agent_executor.invoke({"input": query})
    return webContext['output']

print(researchAgent(query, llm))




