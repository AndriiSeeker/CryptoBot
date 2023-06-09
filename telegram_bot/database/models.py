from sqlalchemy import Column, String, Boolean, BigInteger, Float, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Crypto(Base):
    __tablename__ = "cryptocurrency_crypto"
    id = Column(Integer, primary_key=True)
    coin_id = Column(BigInteger())
    name = Column(String())
    symbol = Column(String())
    price = Column(Float())
    percent_change_1h = Column(Float())
    percent_change_24h = Column(Float())
    percent_change_7d = Column(Float())
    circulating_supply = Column(BigInteger())


class News(Base):
    __tablename__ = "cryptocurrency_news"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    text = Column(String())
    date = Column(String())
    source = Column(String())
    link = Column(String())
