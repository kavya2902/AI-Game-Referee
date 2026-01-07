# tools.py
from state import game_state

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]

def validate_move(move: str, player: str) -> dict:
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb":
        if player == "user" and game_state["user_bomb_used"]:
            return {"valid": False, "reason": "Bomb already used"}
        if player == "bot" and game_state["bot_bomb_used"]:
            return {"valid": False, "reason": "Bomb already used"}

    return {"valid": True}


def resolve_round(user_move: str, bot_move: str) -> dict:
    if user_move == bot_move:
        return {"winner": "draw"}

    if user_move == "bomb":
        return {"winner": "user"}
    if bot_move == "bomb":
        return {"winner": "bot"}

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if rules[user_move] == bot_move:
        return {"winner": "user"}

    return {"winner": "bot"}


def update_game_state(winner: str, user_move: str, bot_move: str) -> dict:
    if user_move == "bomb":
        game_state["user_bomb_used"] = True
    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True

    if winner == "user":
        game_state["user_score"] += 1
    elif winner == "bot":
        game_state["bot_score"] += 1

    game_state["round"] += 1
    if game_state["round"] > 3:
        game_state["game_over"] = True

    return game_state
