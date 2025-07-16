from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
import os

class NoPathFoundException(Exception):
    pass
class AITrainer:
    def __init__(self,env,savepath="best_model"):
        self.env = env
        self.savepath = savepath

        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)

        self.model = DQN("MlpPolicy", env,verbose=1,learning_rate=1e-4, buffer_size=10000,learning_starts=1000, batch_size=64, gamma=0.99,train_freq=10,target_update_interval=500)
        
        self.eval_callback = EvalCallback(env,best_model_save_path=self.savepath,log_path=self.savepath,eval_freq=5000,deterministic=True,render=False,callback_on_new_best=StopTrainingOnRewardThreshold(reward_threshold=1100.0,verbose=1))

    def train(self,total_timesteps=100000):
        self.model.learn(total_timesteps=total_timesteps,callback=self.eval_callback)

    def load_bestmodel(self):
    
        model_path = os.path.join(self.savepath, "best_model.zip")
        if os.path.exists(model_path):
            self.model = DQN.load(model_path, env=self.env)
            print(f"Modelo carregado de {model_path}")
        else:
            print(f"Nenhum modelo encontrado em {model_path}.")


        
                
