from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://aihsiumy_username:aihsiumy_username@localhost:3306/aihsiumy_question"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456789@localhost:3306/questionApp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()