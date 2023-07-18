import psycopg2
from sqlalchemy import create_engine, text

from job import Job

db_url = 'postgresql://postgres:example@127.0.0.1:5431/postgres'
engine = create_engine(db_url)


def get_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs_dict = [row._asdict() for row in result]
        jobs = [Job(**row) for row in jobs_dict]
    return jobs

def get_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            val = id)
        rows = result.all()        
        if len(rows) == 0:
            return None
        else:
            job = Job(**dict(rows[0]))
            resp = get_resp_from_db(id)
            job.responsibilities = resp
            return job
        
def get_resp_from_db(job_id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT task FROM responsibilities WHERE fk_id = :val"),
            val = job_id)
        rows = result.all()
        tasks = [row[0] for row in rows]
        return tasks




    