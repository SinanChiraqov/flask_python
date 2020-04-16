import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# DATABASE_URL = "postgresql://postgres:123@127.0.0.1:5432/myProject"

engine = create_engine(os.getenv("DATABASE_URL"))
# app.config['DATABASE_URL'] = "path_to_db"
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
     flights = db,execute("SELECT origin, destination, duration FROM flights")
     for flight in flights:
         print(f"{flight.origin} to {flight.destination} {flight.duration} minutes")
