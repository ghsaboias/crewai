# Game Development Workspace

This workspace is dedicated to the development of a game using Python. It leverages a unique approach by integrating agents and tasks to streamline the game development process.

## Structure

The workspace contains the following key components:

- `agents.py`: Defines various agent roles such as Senior Software Engineer, Software Quality Control Engineer, and Chief Software Quality Control Engineer. Each agent has specific roles and responsibilities in the game development process.
- `game.py`: The main game file where the game logic and rendering happen. This is the output of the development process.
- `main.py`: The entry point of the workspace. It orchestrates the creation of agents, assignment of tasks, and the overall game development process.
- `tasks.py`: Defines tasks that agents need to perform. These tasks include coding the game, reviewing the code, and evaluating the completeness of the game.
- `trained_agents_data.pkl`: A serialized file containing data related to the agents' performance and learning.

## Setup

To set up the workspace, follow these steps:

1. Ensure Python 3.6 or higher is installed on your system.

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   On Unix or MacOS:

   ```bash
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Workspace

To run the game development process:

1. Activate the virtual environment as described in the setup section.
2. Run the main.py script:
   ```bash
   python main.py
   ```

## Contributing

Contributions to the game development workspace are welcome. Please ensure to follow the coding standards and submit pull requests for review.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
