from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model="llama3",
    base_url="http://localhost:11434")

general_agent = Agent(role = "Software Engineer",
                      goal = """I'm a software engineer and i work with typescript, python, javascript, react native, angular and PostgreSQL.""",
                      backstory = """As a smart software engineer i want your help to discuss, improve or teach each other about how to write better algorithms for frontend and mobile applications and backend services.""",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm)
task = Task (description="""Create a snake game in python.""",
             agent = general_agent,
             expected_output="the entire code of the snake game.")

crew = Crew(
    agents=[general_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()

f = open("../out/snake_game.txt", "a")
f.write(result)
f.close()
