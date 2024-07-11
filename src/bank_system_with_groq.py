#gen_bank_system_with_qroq
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY"))

general_sm_agent = Agent(role="Software Manager",
                         goal="""My goal is to manage and discuss the given project with the team.""",
                         backstory="""As a smart manager I'm very capable to talk with my team and do the best choice to achieve the best solution""",
                         allow_delegation=False,
                         verbose=True,
                         llm=llm)

general_db_agent = Agent(role="Database Engineer",
                         goal="""My goal is to devlop the best database for the given project.""",
                         backstory="""As a smart database engineer I'm very capable to develop SQLs of databases.""",
                         allow_delegation=False,
                         verbose=True,
                         llm=llm)

general_sf_agent = Agent(role="Software Engineer",
                         goal="""My goal is to devlop the best software with the given technology.""",
                         backstory="""I'm a software engineer and i work with typescript, python, javascript, react native, angular and PostgreSQL. As a smart software engineer i want your help to discuss, improve or teach each other about how to write better algorithms for frontend and mobile applications and backend services.""",
                         allow_delegation=False,
                         verbose=True,
                         llm=llm)


task = Task(description="""Lead the team to the best solution with the given tasks.""",
            agent=general_sm_agent,
            expected_output="the team complete the given tasks.")

task = Task(description="""Create a database for a bank system, with withdraw, client, transaction using postgreSQL.""",
            agent=general_db_agent,
            expected_output="the entire SQL of each table.")

task = Task(description="""Create a software for a bank system, with withdraw, client, transaction using python.""",
            agent=general_db_agent,
            expected_output="the entire code for the bank system.")

crew = Crew(
    agents=[general_sm_agent, general_db_agent, general_sf_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()

f = open("../out/bank_system_with_groq.md", "a")
f.write(result)
f.close()
