AI-Game-Referee

This project implements a minimal AI Game Referee chatbot for a 3-round game of Rock–Paper–Scissors–Plus.
The chatbot enforces rules, tracks game state across turns, and ends the game automatically after three rounds.
The solution is built in Python using Google ADK, with explicit use of agents, tools, and structured outputs.

Game Rules: Best of 3 rounds

1.Valid moves: rock, paper, scissors, bomb

2.bomb beats all other moves

3.Each player can use bomb only once per game

4.bomb vs bomb → draw

5.Invalid input wastes the round

6.Game ends automatically after 3 rounds

State Model:
Game state is maintained outside prompts in a persistent Python dictionary:

{
  "round": int,
  "user_score": int,
  "bot_score": int,
  "user_bomb_used": bool,
  "bot_bomb_used": bool,
  "game_over": bool
}
State is updated only via tools to ensure consistency and correctness.

Architecture:
Google ADK Agent: A single Google ADK Agent orchestrates the game:

Explains rules:
-->Handles user input
-->Calls tools
-->Generates user-facing responses
-->ADK Tools
-->Core game logic is implemented as explicit tools and registered with the agent:
-->validate_move – validates moves and enforces bomb usage rules
-->resolve_round – determines the winner of a round
-->update_game_state – mutates scores, round count, and game status
-->All tools return structured outputs (JSON-like dictionaries).

Separation of Concerns:
1.Conversation & flow control → Agent
2.Game logic & validation → Tools
3.State persistence → Python state object (not prompt-based)

Tradeoffs:
-->Bot move selection is random
-->CLI-based interface (no UI)
-->Possible Improvements
-->Strategic bot behavior
-->Replay or reset option
-->Schema validation for tool outputs
-->Enhanced intent parsing

How to Run: 
python main.py

Tech Stack:
1.Python
2.Google ADK
