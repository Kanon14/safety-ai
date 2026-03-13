import os
from pathlib import Path
from dotenv import load_dotenv
from safetyAI.pipeline.training_pipeline import TrainPipeline

env_path = Path("safetyAI/.env")
load_dotenv(dotenv_path=env_path)

# Setup environment variables
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
os.environ["ROBOFLOW_API_KEY"] = ROBOFLOW_API_KEY


# Instantiate the TrainPipeline class
train_pipeline = TrainPipeline()

# Test 1: Run test on data ingestion -> data validation
train_pipeline.run_pipeline()