from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Docker python App is running"}

@app.get("/db")
def check_db():
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        return {"message": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}

