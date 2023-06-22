from flask import Flask, render_template
from sqlalchemy.orm import Session

from bachata_create_db import create_bachata_db_engine, Customer

app = Flask(__name__)


@app.route("/")
def index():
    engine = create_bachata_db_engine()
    with Session(engine) as session:
        customers = session.query(Customer).all()
    engine.dispose()
    return render_template('site.html', customers=customers)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)