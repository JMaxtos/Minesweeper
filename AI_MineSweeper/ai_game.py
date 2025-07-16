import numpy as np 
import gymnasium
from gymnasium import spaces
from ai_board import AIBoard
from constants import ROWS,COLUMNS

class AIGame(gymnasium.Env):
    def __init__(self):
        super().__init__()
        self.board = AIBoard()
        #Observation: Game Matrix Rows*Columns with integers from -2 to 9
        #np.int8 -> 8 bits to represent all the data 
        self.observation_space = spaces.Box(low=-2,high=9,shape=(ROWS,COLUMNS),dtype=np.int8)
        self.score = 0
        #Actions: (x,y) -> 400 possible actions
        self.action_space = spaces.Discrete(ROWS*COLUMNS)
        
    def reset(self,*,seed = None,options=None):
        print("RESET called")
        self.board = AIBoard()
        currentGameState = np.array(self.board.getGameState(),dtype=np.int8)
        return currentGameState,{}
    
    def step(self, action):
        gameScore = self.score
       
        print(f"STEP called with action {action}, score: {gameScore}")
        x = action // ROWS
        y = action % COLUMNS

        if not (0 <= x < ROWS and 0 <= y < COLUMNS):
            currentGameState = np.array(self.board.getGameState(),dtype=np.int8)
            return currentGameState, -100.0, True,False, {}
               
        result = self.board.dig(x,y)
        if self.board.boardList[x][y].revealed:
            gameScore += -10.0
        elif not result:
            gameScore += -100.0
        else:
            gameScore += 10.0
        gameComplete = False
        
        if gameScore <=-100:
            gameComplete = True
        elif self.board.checkWin():
            gameScore += 1000.0
            gameComplete = True
        elif not result:
            gameComplete = True
        
        currentGameState = np.array(self.board.getGameState(),dtype=np.int8)

        return currentGameState,gameScore,gameComplete,False,{}
        
    def render(self):
        for row in self.board.getGameState():
            print(" ".join(f"{val:2}"for val in row))
        print()