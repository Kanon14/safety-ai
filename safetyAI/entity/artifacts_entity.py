from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Artifact representing the outputs of the Data Ingestion process.

    Attributes:
    - data_zipfile_path: Path to the downloaded dataset zip file.
    - feature_store_path: Path to the directory where extracted and processed data is stored.
    """
    data_zipfile_path: str
    feature_store_path: str
    

@dataclass
class DataValidationArtifact:
    """
    Artifact representing the results of the Data Validation process.

    Attributes:
    - validation_status: Boolean indicating whether the validation passed (True) or failed (False).
    """
    validation_status: bool
    

@dataclass
class ModelTrainerArtifact:
    """
    Artifact representing the results of the Data Validation process.

    Attributes:
    - validation_status: Boolean indicating whether the validation passed (True) or failed (False).
    """
    trained_model_file_path: str