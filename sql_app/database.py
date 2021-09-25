from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

time.sleep(30)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:###@db:3306/studyApp"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:###@db:3306/studyApp"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:###############@localhost:3306/studyApp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
