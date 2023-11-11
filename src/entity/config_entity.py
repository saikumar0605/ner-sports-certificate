import os
from dataclasses import dataclass
from src.constant import *



@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.data_transformation_artifacts_dir: str = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)

        self.data_file_path: str = os.path.join(DATA_DIRECTORY, DATA_FILE_NAME)

        self.train_annotation_path: str = os.path.join(DATA_DIRECTORY, TRAIN_ANNOTATION_FILE_NAME)

        self.test_annotation_path: str = os.path.join(DATA_DIRECTORY, TEST_ANNOTATION_FILE_NAME)


@dataclass
class ModelTrainingConfig:
    def __init__(self):
        self.data_transformation_artifacts_dir: str = os.path.join(ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR)