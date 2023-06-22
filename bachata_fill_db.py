from sqlalchemy.orm import Session

from bachata_create_db import City, Customer, DanceStyle, Abonnement, create_bachata_db_engine


def insert_rows(session, rows):
    session.add_all(rows)
    session.commit()
    for row in rows:
        session.refresh(row)


if __name__ == '__main__':
    engine = create_bachata_db_engine()

    with Session(engine) as session:
        session.query(Customer).delete()
        session.query(City).delete()
        session.query(DanceStyle).delete()
        session.query(Abonnement).delete()

        pair_dance = DanceStyle(name="Парная бачата")
        salsa = DanceStyle(name="Сальса")
        lady_style = DanceStyle(name="Lady Style")
        man_style = DanceStyle(name="Man Style")
        insert_rows(session, [pair_dance, salsa, lady_style, man_style])

        kld = City(name="Калининград")
        msk = City(name="Москва")
        spb = City(name="Санкт-Питербург")
        kzn = City(name="Казань")
        aer = City(name="Сочи")
        insert_rows(session, [kld, msk, spb, kzn, aer])

        andrey = Customer(
            name="Андрей",
            age=25,
            sex="м",
            city_id=kld.id,
            email="andrey@mail.ru",
            password="1234"
        )
        masha = Customer(
            name="Маша",
            age=30,
            sex="ж",
            city_id=msk.id,
            email="masha@mail.ru",
            password="1234"
        )
        sergey = Customer(
            name="Сергей",
            age=35,
            sex="м",
            city_id=spb.id,
            email="sergey@mail.ru",
            password="1234"
        )
        valeria = Customer(
            name="Валерия",
            age=35,
            sex="ж",
            city_id=kld.id,
            email="valeria@mail.ru",
            password="1234"
        )
        oleg = Customer(
            name="Олег",
            age=36,
            sex="м",
            city_id=kzn.id,
            email="oleg@mail.ru",
            password="1234"
        )
        insert_rows(session, [andrey, masha, sergey, valeria, oleg])

        a1 = Abonnement(
            customer_id=andrey.id,
            dance_style_id=pair_dance.id,
            remaining_days=24,
        )
        a2 = Abonnement(
            customer_id=masha.id,
            dance_style_id=lady_style.id,
            remaining_days=10,
        )
        a3 = Abonnement(
            customer_id=sergey.id,
            dance_style_id=man_style.id,
            remaining_days=14,
        )
        a4 = Abonnement(
            customer_id=valeria.id,
            dance_style_id=pair_dance.id,
            remaining_days=15,
        )
        a5 = Abonnement(
            customer_id=oleg.id,
            dance_style_id=salsa.id,
            remaining_days=16,
        )
        insert_rows(session, [a1, a2, a3, a4, a5])

    engine.dispose()
