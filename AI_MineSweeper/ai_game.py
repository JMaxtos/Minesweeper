import numpy as np 
import gymnasium
from gymnasium import spaces
from ai_board import AIBoard
from Board.constants import ROWS,COLUMNS

class AIGame(gymnasium.Env):
    def __init__(self):
        super().__init__()
        self.board = AIBoard()
        #Observation: Game Matrix Rows*Columns with integers from -2 to 9
        #np.int8 -> 8 bits to represent all the data 
        self.observation_space = spaces.Box(low=-2,high=9,shape=(ROWS,COLUMNS),dtype=np.int8)

        #Actions: (x,y) -> 400 possible actions
        self.action_space = spaces.Discrete(ROWS*COLUMNS)
        
    def reset(self,):
        self.board = AIBoard()
        currentGameState = np.array(self.board.getGameState(),dtype=np.int8)
        return currentGameState
    
    def step(self, action):
        x = action // ROWS
        y = action % COLUMNS

        result = self.board.dig(x,y)
        gameComplete = not result or self.board.checkWin()
        #Reward of Penalize depending of any mine as exploded
        gameScore = 10.0 if result else -100.0 
        if self.board.checkWin():
            gameScore +=1000.0

        currentGameState = np.array(self.board.getGameState(),dtype=np.int8)
        return currentGameState,gameScore,gameComplete
        
    def render(self):
        for row in self.board.getGameState():
            print(" ".join(f"{val:2}"for val in row))
        print()