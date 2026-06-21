#this file contains all the database connections and session creations
#load the environmental variables
from dotenv import load_dotenv
#to create connection to database
from sqlalchemy import create_engine
#to create sessions and creating base class for all tables
from sqlalchemy.orm import sessionmaker,declarative_base
import os
#---LOAD ENVIRONEMNETAL VARIBALES----
load_dotenv()
#fetch the DB_URL
DATABASE_URL=os.getenv('DATABASE_URL')
#create engine
engine=create_engine(DATABASE_URL,pool_pre_ping=True)
#create a base class 
Base=declarative_base()
#create a session 
SessionLocal=sessionmaker(bind=engine)