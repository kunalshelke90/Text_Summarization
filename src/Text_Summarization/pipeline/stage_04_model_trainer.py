from src.Text_Summarization.config.configuration import ConfigurationManager
from src.Text_Summarization.components.model_trainer import ModelTrainer
from src.Text_Summarization.logging import *


class DataModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()