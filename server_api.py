from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from starlette.responses import JSONResponse,FileResponse
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from crawling.crawling import get_articles
from crawling.image import gen_image

app = FastAPI()

class ResponseBody(BaseModel):
    title:str
    context:str
    author:str
    url:str
    date:str
    category:str
    userId:str


class RequestBody(BaseModel):
    userId:str
    category:str

class ImageRequestBody(BaseModel):
    context:str
    id:int

class ImageResponseBody(BaseModel):
    image:UploadFile
    id:int


@app.post("/article/save", response_model=ResponseBody)
async def post_articles(requestBody: RequestBody):
    article = get_articles(requestBody.category)
    return JSONResponse(article)


@app.post("/article/image")
async def post_image(requestBody: ImageRequestBody):
    image = gen_image(requestBody.id, requestBody.context)
    #return FileResponse(f'{requestBody.id}.png')
    
    #여기서 파이썬 컨트롤러 호출
    return FileResponse(image)