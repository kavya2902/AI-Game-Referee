# main.py
from agent import GameAgent
from state import game_state

def main():
    game = GameAgent()
    print(game.explain_rules())

    while not game_state["game_over"]:
        user_input = input(f"\nRound {game_state['round']} - Enter your move: ")
        response = game.handle_turn(user_input)
        print(response)

    print("\nGAME OVER")
    if game_state["user_score"] > game_state["bot_score"]:
        print("Final Result: USER WINS")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Final Result: BOT WINS")
    else:
        print("Final Result: DRAW")

if __name__ == "__main__":
    main()
