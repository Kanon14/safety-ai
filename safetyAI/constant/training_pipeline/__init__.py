ARTIFACTS_DIR: str = "artifacts" 

"""
Data Ingestion related constant
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

ROBOFLOW_WORKSPACE = "roboflow-universe-projects"

ROBOFLOW_PROJECT = "personal-protective-equipment-combined-model"  

"""
Data Validation related constant
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "valid", "data.yaml"]


"""
Model Trainer related constant
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolo26s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 100