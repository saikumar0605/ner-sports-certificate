import os
from datetime import datetime


TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
LOGS_DIR = 'logs'
LOGS_FILE_NAME = 'ner.log'


DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
DATA_DIRECTORY = "data"
DATA_FILE_NAME = "data.xlsx"
TRAIN_ANNOTATION_FILE_NAME = "train_annotations.json"
TEST_ANNOTATION_FILE_NAME = "test_annotations.json"
SPACY_TRAIN_DATA_FORMAT_NAME = "train_data.spacy"
SPACY_TEST_DATA_FORMAT_NAME = "test_data.spacy"

MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"