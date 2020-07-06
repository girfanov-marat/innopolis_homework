"""Описание моделей бд."""
from typing import Any

from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # type: Any
engine = create_engine("sqlite:///onyx_taxi.db")
Session = sessionmaker(bind=engine)


class Client(Base):
    """Модель под табличку с клиентами."""

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, comment="Идентификатор клиента")
    name = Column(String, nullable=False, comment="Имя клиента")
    is_vip = Column(Boolean, nullable=False, comment="статус клиента")


class Drivers(Base):
    """Create model for table."""

    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    car = Column(String, nullable=False)


class Orders(Base):
    """Модель таблицы Orders."""

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    address_from = Column(String, nullable=False)
    address_to = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    date_created = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)


Base.metadata.create_all(engine)
