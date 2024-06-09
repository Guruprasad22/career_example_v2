from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
import json


app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': "data analyst",
    'location': 'bengaluru',
    'salary': 'Rs 10,00,000'
  },
  {
    'id': 2,
    'title': "data scientist",
    'location': 'bengaluru',
    'salary': 'Rs 15,00,000'
  },
  {
    'id': 3,
    'title': "director",
    'location': 'bengaluru',
    'salary': 'Rs 25,00,000'
  }
]


@app.route("/")
def index():
  job_list = load_jobs_from_db()
  return render_template('home.html', jobs=job_list)


@app.route("/api/jobs")
def get_jobs():
  job_list = load_jobs_from_db()
  return jsonify(json.dumps(job_list, default=str))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
