from ai_game import AIGame
from ai_trainer import AITrainer
from stable_baselines3.common.monitor import Monitor
def main():
    env = AIGame()
    trainer = AITrainer(Monitor(env),savepath="Best_model")
    trainer.train(total_timesteps=100000)

if __name__ == "__main__":
    main()