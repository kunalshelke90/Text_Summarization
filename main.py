# import sys
# sys.path.append(r"C:\Users\shelk\OneDrive\Desktop\Text_Summarize")

# from Text_Summarization.logging import *
# from Text_Summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Text_Summarization.logging import logger
from src.Text_Summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
