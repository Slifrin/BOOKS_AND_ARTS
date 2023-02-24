
from flask import Flask, render_template, jsonify, request

from database import get_jobs_data, get_job_data, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    return render_template("home.html", jobs=get_jobs_data(), company_name="Jovian")

@app.route("/job/<id>")
def show_job(id):
    job = get_job_data(id)
    # return jsonify(job)
    if job is None:
      return "Not Found", 404
    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.args
    print(data)
    data = request.form
    print(data)
    add_application_to_db(id, data)
    return jsonify(data)


@app.route("/api/jobs2")
def list_jobs2():
    return get_jobs_data()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=True)
