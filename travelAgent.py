from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType,create_react_agent,AgentExecutor
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain import hub

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Configura a API do Wikipedia
wiki_api_wrapper = WikipediaAPIWrapper()

# Define a ferramenta com o wrapper configurado
tools = [WikipediaQueryRun(api_wrapper=wiki_api_wrapper)]

# Carrega o prompt "react" do repositório hwchase17 utilizando o hub
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm,tools, prompt)

agent_executor = AgentExecutor(agent=agent,tools=tools,prompt=prompt,verbose=True)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Exemplo de uso do agente
query = """
Vou viajar para França em julho de 2025. Quero que faça um roteiro de viagens para mim com os eventos que irão ocorrer na data da viagem 
e com o preço de passagem de São Paulo pra Londres
"""

agent_executor.invoke({"input": query})
