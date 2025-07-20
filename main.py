from fastapi import FastAPI
from typing import List
from userDataType import Manjeet

#Defining the app components

app = FastAPI()

usrList: List[Manjeet] = []

@app.get("/")
def get_root():
    return {"message": "Welcome to the FastAPI"}


@app.get("/userlist")
def get_all_userlist():
    return usrList


@app.post("/adduser")
def add_user(user: Manjeet):
    usrList.append(user)
    return user
