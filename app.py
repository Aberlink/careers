from job import Job
from flask import Flask, render_template, jsonify

app = Flask(__name__)
adress = "127.0.0.1"
port = 5000

a = Job("123", "plumber", "Krakow", 3500)
b = Job("xaawd", "painter", "Wroclaw", 5400)
c = Job("css1eq", "carpenter", "katowice", 4200)

jobs = [a,b,c]

@app.route("/")
def hellow():
    return render_template('home.html', \
        jobs=jobs)
    
@app.route("/api/jobs")
def ask_jobs():
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

if __name__ == "__main__":
    app.run(host=adress, port=port, debug=True)