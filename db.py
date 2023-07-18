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




    