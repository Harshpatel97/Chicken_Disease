from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.utils import create_directories, read_yaml



class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zipfile()
        except Exception as e:
            raise e