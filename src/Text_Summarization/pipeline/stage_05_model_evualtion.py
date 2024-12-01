from src.Text_Summarization.config.configuration import ConfigurationManager
from src.Text_Summarization.components.model_evualation import ModelEvaluation
from src.Text_Summarization.logging import *


class DataModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()