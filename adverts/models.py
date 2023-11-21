from atexit import register

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine, func
from sqlalchemy.orm import sessionmaker, declarative_base

PG_USER = 'netology'
PG_PASS = 'netology'
PG_DB = 'flask-advert'
PG_HOST = '192.168.85.4'
PG_PORT = '5431'

PG_DSN = f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_engine(PG_DSN)

register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base()


class Adverts(Base):
    __tablename__ = "api_adverts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True, index=True)
    description = Column(Text, nullable=False)
    owner = Column(String, nullable=False, unique=True, index=True)
    creation_date = Column(DateTime, server_default=func.now())


# Base.metadata.create_all(bind=engine)