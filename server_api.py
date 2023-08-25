from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from starlette.responses import JSONResponse,FileResponse,Response
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawling.crawling import get_articles,get_one_article,get_home_articles
from crawling.image import gen_image
from crawling.sport_exception import get_sport_articles

app = FastAPI()


class ImageRequestBody(BaseModel):
    context:str
    id:int

class ImageResponseBody(BaseModel):
    path:str
    id:int


class ResponseBody(BaseModel):
    title:str
    context:str
    author:str
    url:str
    date:str
    category:str
    userId:str
    keywords:list = []
    image:ImageResponseBody


class RequestBody(BaseModel):
    userId:str
    category:str




@app.post("/article/save", response_model=ResponseBody)
async def post_articles(requestBody: RequestBody):
    if requestBody.category == "스포츠":
        article = get_sport_articles(requestBody.userId)
    else:
        article = get_articles(requestBody.category, requestBody.userId)
    return JSONResponse(article)

@app.post("/article/home", response_model=ResponseBody)
async def post_articles(requestBody: RequestBody):
    article = get_home_articles(requestBody.category, requestBody.userId)
    return JSONResponse(article)

@app.post("/article/image",response_model=ImageResponseBody)
async def post_image(requestBody: ImageRequestBody):
    image = gen_image(requestBody.id, requestBody.context)

    return JSONResponse(image)
