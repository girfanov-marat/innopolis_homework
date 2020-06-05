"""Файл для работы с базой данных."""
from typing import Any

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sa.create_engine("sqlite:///mybd.db")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()  # type: Any


class Goods(Base):
    """Таблица goods."""

    __tablename__ = "goods"

    id = sa.Column(sa.INTEGER,
                   nullable=False,
                   autoincrement=True,
                   primary_key=True,
                   comment='уникальный идентификатор товарa')
    name = sa.Column(sa.VARCHAR,
                     nullable=False,
                     comment='наименование товара')
    package_height = sa.Column(sa.FLOAT,
                               nullable=False,
                               comment='высота кпакованного товара')
    package_width = sa.Column(sa.FLOAT,
                              nullable=False,
                              comment='ширина кпакованного товара')


class ShopGoods(Base):
    """Таблица shop_goods."""

    __tablename__ = "shop_goods"

    id = sa.Column(sa.INTEGER,
                   nullable=False,
                   autoincrement=True,
                   primary_key=True,
                   comment='идентификатор записи')
    id_good = sa.Column(sa.INTEGER,
                        sa.ForeignKey('goods.id'),
                        nullable=False,
                        comment='идентификатор товара')
    location = sa.Column(sa.VARCHAR,
                         nullable=False,
                         comment='адрес магазина')
    amount = sa.Column(sa.INTEGER,
                       nullable=False,
                       comment='количество этого товара в этом магазине')


def create_tables() -> None:
    """Создание таблиц, если они не созданы."""
    if not engine.dialect.has_table(engine, "goods"):
        Goods.__table__.create(engine)
    if not engine.dialect.has_table(engine, "shop_goods"):
        ShopGoods.__table__.create(engine)


def goods_insert(values: dict) -> Any:
    """Создание объекта класса Goods с полученным параметрами."""
    to_insert = Goods(id=values["id"],
                      name=values["name"],
                      package_height=values["height"],
                      package_width=values["width"])
    return to_insert


def shop_goods_insert(values: dict) -> Any:
    """Создание объекта класса ShopGoods с полученным параметрами."""
    to_insert = ShopGoods(id_good=values["id_good"],
                          location=values["location"],
                          amount=values["amount"])
    return to_insert


def insert_or_update(all_dicts: list) -> None:
    """Функция для добавления или изменения значений входного JSON в бд."""
    for i in range(len(all_dicts)):
        if len(all_dicts[i]) == 4:
            data = goods_insert(all_dicts[i])
            if session.query(Goods).filter_by(id=all_dicts[i]["id"]).first():
                session.query(Goods).filter_by(id=all_dicts[i]["id"]). \
                    update({Goods.id: data.id,
                            Goods.name: data.name,
                            Goods.package_height: data.package_height,
                            Goods.package_width: data.package_width})
            else:
                session.add(data)
        if len(all_dicts[i]) == 3:
            data = shop_goods_insert(all_dicts[i])
            if session.query(ShopGoods).filter_by(id_good=all_dicts[i]["id_good"],
                                                  location=all_dicts[i]["location"]).first():
                session.query(ShopGoods).filter_by(id_good=all_dicts[i]["id_good"],
                                                   location=all_dicts[i]["location"]). \
                    update({ShopGoods.id_good: data.id_good,
                            ShopGoods.location: data.location,
                            ShopGoods.amount: data.amount})
            else:
                session.add(data)
    session.commit()
    session.close()
