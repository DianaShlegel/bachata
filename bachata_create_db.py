import datetime as dt

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column


def create_bachata_db_engine():
    return create_engine("sqlite:///Bachata.db")


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customer"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name = mapped_column("name", String(30), nullable=False)
    age = mapped_column("age", Integer, nullable=True)
    sex = mapped_column("sex", String(30), nullable=True)

    city_id = mapped_column(ForeignKey("city.id"))

    email = mapped_column("email", String(30), nullable=False, index=True, unique=True)
    password = mapped_column("password", String)
    created_date = mapped_column("created_date", DateTime, default=dt.datetime.now)

    city: Mapped["City"] = relationship(lazy='subquery')
    abonnements: Mapped[list["Abonnement"]] = relationship(lazy='subquery')

    def get_styles(self):
        return ", ".join([abonnement.style.name for abonnement in self.abonnements]) or "-"


class City(Base):
    __tablename__ = "city"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name = mapped_column("name", String(30), nullable=False)


class Abonnement(Base):
    __tablename__ = "abonnement"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    customer_id = mapped_column(ForeignKey("customer.id"))
    dance_style_id = mapped_column(ForeignKey("dance_style.id"))

    start_date = mapped_column("start_date", DateTime, default=dt.datetime.now)
    remaining_days = mapped_column("remaining_days", Integer, nullable=False)

    style: Mapped["DanceStyle"] = relationship(lazy='subquery')


class DanceStyle(Base):
    __tablename__ = "dance_style"
    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    name = mapped_column("name", String(30), nullable=False)


if __name__ == "__main__":
    engine = create_bachata_db_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.dispose()
