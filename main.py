from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import GameTasks
from agents import GameAgents

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
game_name = input("What is the name of the game you would like to build?\n")
game_instructions = input("What will be the mechanics?\n")
game = f"{game_name}: {game_instructions}"

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

game_code = crew.kickoff()

# Generate file name from the game name
file_name = game_name.lower().replace(' ', '_') + '.py'

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")

# Save the code to a file with the dynamic name
with open(file_name, 'w') as f:
    f.write(game_code)
