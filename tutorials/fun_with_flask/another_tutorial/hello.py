from flask import Flask, render_template, jsonify


app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Job 1',
        'Location': 'Location 1',
        'salary': '10000 USD',
    },
    {
        'id': 2,
        'title': 'Job 2',
        'Location': 'Location 2',
        'salary': '20000 USD',
    },
    {
        'id': 3,
        'title': 'Job 3',
        'Location': 'Location 3',
        'salary': '30000 USD',
    },
    {
        'id': 4,
        'title': 'Job 4',
        'Location': 'Location 4',
        'salary': '40000 USD',
    },
]


@app.route("/")
def hello_there():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/tarapaty")
def tarapaty():
    return "<p> Tarapaty </p>"



def main() -> None:
    print(f'Hello main from : {__file__}')
    app.run(debug=True)

if __name__ == '__main__':
    main()