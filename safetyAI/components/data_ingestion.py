import os
import sys
from roboflow import Roboflow
from safetyAI.logger import logging
from safetyAI.exception import AppException
from safetyAI.entity.config_entity import DataIngestionConfig
from safetyAI.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    """
    This class handles the data ingestion process, including downloading the dataset 
    from a specified URL, extracting the downloaded zip file, and preparing it for 
    further processing.
    """
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        """
        Constructor for the DataIngestion class.
        
        :param data_ingestion_config: Configuration for data ingestion including 
                                      download URL and directory paths.
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
           raise AppException(e, sys)
       
    
    def download_roboflow_dataset(self) -> str:
        """
        Downloads the Roboflow dataset from the specified URL and extracts it into
        the feature store directory.

        :return: Path to the extracted feature store directory.
        """
        try:
            dataset_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(dataset_download_dir, exist_ok=True)
        
            rf = Roboflow()
            roboflow_workspace = self.data_ingestion_config.roboflow_workspace
            roboflow_project = self.data_ingestion_config.roboflow_project

            project = rf.workspace(roboflow_workspace).project(roboflow_project)
            version = project.version(8)
            dataset = version.download("yolo26", location=dataset_download_dir)
            
            logging.info(f"Downloaded data from {roboflow_workspace}/{roboflow_project} to {dataset_download_dir}")
            
            dataset_path = os.path.join(dataset_download_dir, dataset.name)
            
            return dataset_path
        
        except Exception as e:
            raise AppException(e, sys)
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Orchestrates the data ingestion process by downloading and extracting the dataset.
        
        :return: DataIngestionArtifact containing paths to the zip file and extracted data directory.
        :raises AppException: If an error occurs during the data ingestion process.
        """
        logging.info("Entered initiate_data_ingestion method from DataIngestion class")
        try:
            dataset_path = self.download_roboflow_dataset()
            data_ingestion_artifact = DataIngestionArtifact(dataset_path=dataset_path)
            logging.info("Exited initiate_data_ingestion method")
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)