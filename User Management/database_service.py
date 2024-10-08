from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create an engine for SQLite database
db = create_engine('sqlite:///patient_management.db', echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=db)

# Create a Session instance
session = Session()

# Define Base for the ORM models
Base = declarative_base()

# Check tables in the database using MetaData
metadata = MetaData()
metadata.reflect(bind=db)
