import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SqlAlchemy_url = os.environ.get('SQLALCHEMY_DB')
engine = create_engine(SqlAlchemy_url)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = DBSession()
