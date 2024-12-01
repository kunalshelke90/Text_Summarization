from src.Text_Summarization.config.configuration import ConfigurationManager
from src.Text_Summarization.components.data_validatioin import DataValiadtion
from src.Text_Summarization.logging import *

class DataValidationTrainingPipeline:
    def ___init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
