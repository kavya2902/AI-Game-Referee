# agent.py
import random
from google.adk.agents import Agent
from tools import validate_move, resolve_round, update_game_state
from state import game_state

class GameAgent:
    def __init__(self):
        self.agent = Agent(
            name="rps_referee_agent",
            tools=[
                validate_move,
                resolve_round,
                update_game_state
            ]
        )

    def explain_rules(self):
        return (
            "Rock–Paper–Scissors–Plus\n"
            "• Best of 3 rounds\n"
            "• rock, paper, scissors, bomb\n"
            "• bomb beats all (once per game)\n"
            "• Invalid input wastes the round"
        )

    def bot_move(self):
        moves = ["rock", "paper", "scissors"]
        if not game_state["bot_bomb_used"]:
            moves.append("bomb")
        return random.choice(moves)

    def handle_turn(self, user_move: str):
        round_no = game_state["round"]

        validation = validate_move(user_move, "user")
        bot_move = self.bot_move()

        if not validation["valid"]:
            update_game_state("draw", "", "")
            return f"Round {round_no}\nInvalid input. Round wasted."

        result = resolve_round(user_move, bot_move)
        update_game_state(result["winner"], user_move, bot_move)

        return (
            f"Round {round_no}\n"
            f"You played: {user_move}\n"
            f"Bot played: {bot_move}\n"
            f"Result: {result['winner']}\n"
            f"Score → You: {game_state['user_score']} | Bot: {game_state['bot_score']}"
        )
