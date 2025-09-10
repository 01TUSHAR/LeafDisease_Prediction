from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# MongoDB connection string from .env
MONGO_URL = os.getenv("MONGO_URL")

# Initialize Mongo client
client = AsyncIOMotorClient(MONGO_URL)
db = client["SugarcaneDisease"]   # Database
disease_collection = db["disease_info"]  # Collection



# Pydantic model for request/response
class DiseaseInfo(BaseModel):
    disease_name: str
    description: str | None = None
    cause: str | None = None
    symptoms: str | None = None
    pre_management: str | None = None
    mid_management: str | None = None
    future_management: str | None = None
    precautions: str | None = None


# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Database connection settings
# # SQLALCHEMY_DATABASE_URL = "mysql+mysqlclient://root:user1@localhost:3306/sugarcanediseases"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:user1@localhost:3306/sugarcanediseases"


# # Create engine and session
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # DiseaseInfo Model
# class DiseaseInfo(Base):
#     __tablename__ = "disease_info"
#     id = Column(Integer, primary_key=True, index=True)
#     disease_name = Column(String, index=True)
#     description = Column(String)
#     cause = Column(String)
#     symptoms = Column(String)
#     pre_management = Column(String)
#     mid_management = Column(String)
#     future_management = Column(String)
#     precautions = Column(String)

# # Create all tables
# Base.metadata.create_all(bind=engine)