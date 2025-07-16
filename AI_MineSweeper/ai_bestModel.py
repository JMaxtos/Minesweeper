from stable_baselines3 import DQN
from ai_game import AIGame
from game import *
from constants import TILESIZE,COLUMNS,ROWS


class BestModel:
    def __init__(self,model_path="Best_model/best_model.zip"):
        self.env = AIGame()
        self.model = DQN.load(model_path,env=self.env)
        self.game= Game()
        self.game.new()
    
    def run(self):
        done = False
        while not done:
            currentGameState = self.env.board.getGameState()
            action,_ = self.model.predict(currentGameState,deterministic=True)
            x = action // ROWS
            y = action % COLUMNS

            done = not self.game.board.dig(x,y)
            self.game.draw()

            pygame.time.delay(200)

            if self.game.checkWin():
                print("AI Wins!!")
                done = True
            
            pygame.time.delay(2000)
            self.game.leaveGame()


        