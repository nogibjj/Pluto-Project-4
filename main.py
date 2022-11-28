#~/book_service/app/main.py

from fastapi import FastAPI
import uvicorn
from logictest import wiki_search
from logictest import wiki as wikilogic

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Wikipedia API"}

@app.get("/search/{value}")
async def add(value:str):
   """ page to search in wiki"""

   results = wiki_search(value)
   return{"results":result}

@app.get("/wiki/{name}")
async def wiki(name:str):
    """retrieve page"""

    result = wikilogic(name)
    return{"result": result}



if __name__=='__main__':
    uvicorn.run(app,port = 8070, host = '0.0.0.0')
