"""Create SQLAlchemy engine and session objects."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create database engine
engine = create_engine('sqlite:///example.db', echo=False)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()