import os
import json

from pprint import pprint
from textwrap import shorten, dedent


from sqlalchemy import create_engine, text
from dotenv import load_dotenv, dotenv_values


config = dotenv_values()
connection_str = f"mysql+pymysql://{config['USERNAME']}:{config['PASSWORD']}@{config['HOST']}/{config['DATABASE']}?charset=utf8mb4"
connect_args = {
    "ssl": {
        "ca": "/etc/ssl/cert.pem",
    }
}

engine = create_engine(connection_str, connect_args=connect_args)


def get_jobs_data():
    with engine.connect() as conn:
        data: list = []
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()

        for row in result_all:
            data.append(row._asdict())

        return data


def get_job_data(id: int):
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from jobs j where j.id = {id}"))
        rows = result.all()

        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        # query = text(
        #     dedent(
        #         f"""INSERT INTO applications (job_id, full_name, email, linkedin_url, education) VALUES
        #     ({job_id}, {data['full_name']}, {data['email']}, {data['linkedin_url']}, {data['education']})
        # """
        #     )
        # )
        stmt = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education) VALUES"
            "(:job_id, :full_name, :email, :linkedin_url, :education)"
        )

        stmt = stmt.bindparams(
            job_id=job_id,
            full_name=data["full_name"],
            email=data["email"],
            linkedin_url=data["linkedin_url"],
            education=data["education"],
        )
        print(stmt)
        # pprint(dir(stmt))
        pprint(stmt.text)
        pprint(stmt.compile(engine).string)
        pprint(str(stmt.compile(engine, compile_kwargs={"literal_binds": True})))

        conn.execute(stmt)
