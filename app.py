from job import Job
from flask import Flask, render_template, jsonify

from db import get_jobs_from_db, get_job_from_db

app = Flask(__name__)
adress = "127.0.0.1"
port = 5000
jobs = []

@app.route("/")
def hellow():
    jobs = get_jobs_from_db()
    return render_template('home.html', \
        jobs=jobs)
    
@app.route("/api/jobs")
def ask_jobs():
    jobs = get_jobs_from_db()
    job_list = []
    for job in jobs:
        job_dict = {
            'id': job.id,
            'title': job.title,
            'location': job.location,
            'salary': job.salary
        }
        job_list.append(job_dict)
    
    return jsonify(job_list)

@app.route("/job/<int:job_id>")
def show_job(job_id):
    job = get_job_from_db(job_id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)

if __name__ == "__main__":
    app.run(host=adress, port=port, debug=True)