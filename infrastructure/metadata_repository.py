from abc import abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class OracleDbConnection:
    def __init__(self, args:dict):
        print(args)
        self.username=args["usrName"]
        self.password=args["pwd"]
        self.host=args["host"]
        self.service_name=args["database"]
        self.database=args["database"]
       

    def get_db_session(self):
        DATABASE_URL = f"oracle+cx_oracle://{self.username}:{self.password}@(DESCRIPTION = (LOAD_BALANCE=on) (FAILOVER=ON) (ADDRESS = (PROTOCOL = TCP)(HOST = {self.host})(PORT = {self.port})) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = {self.service_name})))"    
        engine = create_engine(DATABASE_URL)
        # Create session factory
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # Create base class for models
        Base = declarative_base()
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()


class MetadataRepository:
    def get_file_metadata(self, file_src_cd: str) -> dict:
        """
        Retrieves metadata for the file to decide on the adapter and processing.
        :param file_id: Unique file identifier
        :return: Metadata dictionary
        """
        pass

class ValidationRulesRepository:
    
    def get_validation_rules(self) -> list:
        """
        Fetches validation rules from the database.
        :return: List of validation rules
        """
        pass

class ReplicationCriteriaRepository:
    
    def get_replication_criteria(self) -> dict:
        """
        Fetches row replication criteria from the database.
        :return: Replication criteria
        """
        pass

class RawDataRepository:
    
    def store_raw_data(self, raw_data: list):
        """
        Stores raw data in the database.
        :param raw_data: List of raw data
        """
        pass

class ProcessedDataRepository:
    
    def store_processed_data(self, processed_data: list):
        """
        Stores processed data in the database.
        :param processed_data: List of processed data
        """
        pass

class SummaryReportRepository:
    
    def store_report(self, report: dict):
        """
        Stores the summary report in the database.
        :param report: Report data
        """
        pass
