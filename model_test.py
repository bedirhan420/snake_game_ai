import torch
from test_game import SnakeGameAI
from agent import Agent

def test():
    agent = Agent()
    game = SnakeGameAI()

    # Eğitim sonrası modeli yükle
    agent.model.load()

    while True:
        state = agent.get_state(game)
        action = agent.get_action(state)

        reward, done, score = game.play_step(action)
        state_new = agent.get_state(game)

        if done:
            game.reset()
            print('Game over! Score:', score)
            break

if __name__ == '__main__':
    test()
