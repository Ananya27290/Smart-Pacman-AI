🟡 Smart Pacman AI

An AI-powered Pacman game developed using **Python** and **Pygame**, featuring intelligent ghost behaviors, **A*** pathfinding, and rule-based decision making. The project demonstrates core Artificial Intelligence concepts through an interactive Pacman game.



🎯 Project Overview

Smart Pacman AI is an intelligent version of the classic Pacman game where ghosts exhibit different behaviors based on AI algorithms and predefined rules. Unlike a traditional Pacman game with random ghost movement, this project uses Artificial Intelligence techniques such as **A*** Search Algorithm, **Finite State Machine (FSM)**, and **Rule-Based Decision Making** to create more realistic and challenging gameplay.

The project was developed to demonstrate how search algorithms and intelligent agents can be applied in game development.
markdown


✨ Features

🎮 Interactive Pacman gameplay developed using Python and Pygame.
🤖 Intelligent ghost movement powered by the A* Search Algorithm.
🧠 Rule-based decision making for adaptive ghost behavior.
🔄 Finite State Machine (FSM) to control ghost modes such as Chase, Scatter, and Frightened.
🍒 Food pellets and power pellets with score tracking.
👻 Multiple ghost behaviors to provide varied gameplay.
🏆 Win and Game Over conditions.
⚡ Smooth real-time game rendering and keyboard controls.
📈 Modular project architecture for easy maintenance and future enhancements.

markdown


🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python 3 |
| Game Development | Pygame |
| Artificial Intelligence | A* Search Algorithm |
| AI Techniques | Rule-Based System, Finite State Machine (FSM) |
| Development Environment | Visual Studio Code |
| Version Control | Git & GitHub |

markdown

## 📁 Project Structure



Smart-Pacman-AI
│
├── agents/                 # Pacman and ghost agent implementations
├── algorithms/             # A* search algorithm
├── behaviors/              # Ghost behavior and Finite State Machine
├── docs/                   # Architecture, workflow, report and diagrams
├── environment/            # Maze and game environment
├── images/                 # Screenshots of the project
├── rendering/              # Game rendering and drawing functions
├── utils/                  # Constants and helper utilities
│
├── .gitignore
├── requirements.txt
├── README.md
└── main.py                 # Entry point of the application

markdown


# 🧠 Artificial Intelligence Concepts Used

This project demonstrates the practical application of Artificial Intelligence concepts in game development. Instead of using random ghost movement, intelligent decision-making techniques are implemented to create a challenging and realistic Pacman game.

### A* Search Algorithm
The A* Search Algorithm is used for pathfinding, enabling ghosts to calculate the shortest path towards Pacman while efficiently navigating around maze walls and obstacles. This allows ghosts to pursue Pacman intelligently rather than moving randomly.

### Rule-Based Decision Making
Ghost behavior is controlled using predefined IF-THEN rules. These rules determine how each ghost reacts based on the current game state, such as Pacman's position, ghost mode, and power pellet status. Rule-based reasoning enables consistent and predictable intelligent behavior.

### Finite State Machine (FSM)
A Finite State Machine manages ghost behavior by switching between different states such as Scatter, Chase, and Frightened. Each state defines a specific objective and movement strategy, making ghost behavior dynamic throughout the game.

### Intelligent Agent Design
Each ghost acts as an autonomous intelligent agent. Agents continuously perceive the game environment, evaluate the current situation, apply decision-making rules, and perform actions independently to achieve their objectives.
```
```markdown
---

# ⚙️ How the AI Works

The game is built around autonomous agents that continuously observe the game environment, make decisions, and execute actions in real time.

### Pacman Agent
- Controlled by the player through keyboard input.
- Collects pellets to increase the score.
- Avoids ghosts while navigating through the maze.
- Can temporarily gain an advantage by consuming power pellets.

### Ghost Agents
Each ghost acts as an independent intelligent agent with its own decision-making process.

The ghosts continuously:
1. Observe Pacman's current position.
2. Evaluate the current game state.
3. Determine their current behavior mode.
4. Calculate the next movement.
5. Move toward their target location.

### Decision-Making Process

The ghost decision process follows these steps:

```

Observe Environment
↓
Determine Current State
↓
Apply Rule-Based Logic
↓
Calculate Path using A*
↓
Move to Next Position
↓
Repeat

```

### Behavior Modes

Ghosts switch between different modes during gameplay:

- **Scatter Mode** – Move toward predefined corners of the maze.
- **Chase Mode** – Pursue Pacman using intelligent pathfinding.
- **Frightened Mode** – Move away from Pacman after a power pellet is consumed.

The transition between these modes is managed using a **Finite State Machine (FSM)**, making the gameplay dynamic and challenging.
```
---

# 🚀 Installation

## Prerequisites

- Python 3.10 or later
- Pygame

## Clone the Repository

```bash
git clone https://github.com/Ananya27290/Smart-Pacman-AI.git
cd Smart-Pacman-AI
## Install Dependencies
pip install -r requirements.txt
## Run the Project
python main.py

---

# 🏗️ Project Architecture

The Smart Pacman AI project follows a modular architecture where each component is responsible for a specific task. This design improves code readability, maintainability, and scalability.

The architecture consists of the following modules:

- **agents/** – Implements Pacman and Ghost agents.
- **algorithms/** – Contains the A* Search Algorithm used for intelligent pathfinding.
- **behaviors/** – Implements the Finite State Machine (FSM) and rule-based ghost behaviors.
- **environment/** – Defines the maze layout and game environment.
- **rendering/** – Handles rendering of the game interface using Pygame.
- **utils/** – Stores constants and reusable helper functions.
- **main.py** – Controls the game loop, event handling, and integration of all modules.

📄 The complete architecture diagram is available in the **docs/** folder.

---

# 📈 Future Improvements

- Add multiple difficulty levels.
- Implement additional intelligent ghost behaviors.
- Improve game graphics and animations.
- Add sound effects and background music.
- Implement score saving and leaderboard support.