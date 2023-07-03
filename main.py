from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles

app = FastAPI()

answer = 'TRAIN'

@app.get("/answer")
def get_answer():
    return {'answer' : answer}

app.mount("/", StaticFiles(directory="static", html=True), name="static")



class Item(BaseModel):
    id:int
    content:str


items = ['맥북', '애플워치', '아이폰', '에어팟']


@app.get("/items")
def read_items():
    return items
  
@app.get("/items/{id}")
def read_id_item(id):
    return items[int(id)]
  
@app.get("/items")
def read_id_item(skip:int=0, limit:int=10):
    return items[skip:skip+limit]
  
  
@app.get("/hello")
def sayHello():
    return {"message": "안녕하세요"}

@app.get("/")
def sayWelcome():
    return {"message": "환영합니다"}
  
  
@app.post("/")
def post_item(item:Item):
  items.append(item.content)
  return "성공했습니다."

