from sqlalchemy import create_engine, text
import os 


DB_CONN_STR = os.environ['DB_CONNECTION_STRING']

engine = create_engine(DB_CONN_STR)


def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      return result.all()


      

