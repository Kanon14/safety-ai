import os
import sys
import torch
from safetyAI.logger import logging
from safetyAI.exception import AppException
from safetyAI.entity.config_entity import ModelTrainerConfig
from safetyAI.entity.artifacts_entity import (DataIngestionArtifact,
                                              ModelTrainerArtifact)
from ultralytics import YOLO


class ModelTrainer:
    """
    This class handles the training of the YOLO model for object detection.
    It manages data preparation, model training, and cleanup processes.
    """
    
    def __init__(self, 
                 data_ingestion_artifact: DataIngestionArtifact,
                 model_trainer_config: ModelTrainerConfig):
        """
        Constructor for the ModelTrainer class.
        
        :param data_ingestion_artifact: Contains paths to the ingested data artifacts.
        :param model_trainer_config: Configuration object containing training parameters like
                                     weights, batch size, and number of epochs.
        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise AppException(e, sys)
        
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        """
        Orchestrates the entire model training process, including:
        - Reading data from data ingestion
        - Training the YOLO model
        - Saving the best-trained model
        
        :return: ModelTrainerArtifact containing the path to the best-trained model.
        :raises AppException: If any step of the process fails.
        """
        logging.info("Entered intiate_model_trainer method of ModelTrainer class")
        try:            
            # Path to the data.yaml which should be relative
            data_yaml_path = os.path.join(self.data_ingestion_artifact.dataset_path, "data.yaml")
            logging.info(f"Accessing the YAML file path: {data_yaml_path}")
            
            # Path to the model_trainer which training occurred
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            logging.info(f"Creating the model training directory: {self.model_trainer_config.model_trainer_dir}")
            
            # Start the YOLO model training
            model = YOLO(model=self.model_trainer_config.weight_name)
            model.train(
                project=os.path.abspath(self.model_trainer_config.model_trainer_dir),
                data=data_yaml_path,
                epochs=self.model_trainer_config.no_epochs,
                imgsz=640,
                device="cuda" if torch.cuda.is_available() else "cpu"
            )
                    
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=os.path.join(self.model_trainer_config.model_trainer_dir, 
                                                     "train", "weights", "best.pt")
            )
            
            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            
            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(e, sys)
    
    
