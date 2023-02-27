
from flask import render_template
import connexion

import config
from models import Person

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)