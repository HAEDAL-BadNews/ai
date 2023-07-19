from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawling.crawling import get_articles

app = FastAPI()

class ResponseBody(BaseModel):
    title:str
    context:str
    author:str
    url:str
    date:str
    category:str
    userId:str
    #keyword:str[3]
    

class RequestBody(BaseModel):
    userId:str
    category:str
    sort:str


@app.post("/article/save", response_model=ResponseBody)
async def post_articles(requestBody: RequestBody):
    article = get_articles()
    return JSONResponse(article)

