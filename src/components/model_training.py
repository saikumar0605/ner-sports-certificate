import os
import sys
import logging
from src.exception import NerException
from src.entity.config_entity import ModelTrainingConfig
from src.entity.artifacts_entity import ModelTrainerArtifacts


# initiatlizing logger
logger = logging.getLogger(__name__)


class ModelTraining:
    def __init__(self, model_trainer_config: ModelTrainingConfig) -> None:
        self.model_trainer_config = model_trainer_config


    def initiate_model_training(self) -> ModelTrainerArtifacts:
        try:
            pass

        except Exception as e:
            raise NerException(e, sys) from e
