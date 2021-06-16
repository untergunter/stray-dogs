import datetime
import shutil
from fastapi import FastAPI,Path,Request,Form,File,UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from Image import get_image_metadata

app = FastAPI()
templates = Jinja2Templates(directory='templates')

""" / stands for root """
@app.get("/")
def home():
    """ this should redirect to the streamlit dashboard  """
    return {'app_name':" helping us find stray dogs"}


@app.get("/missing_form")
async def form(request:Request):
    """ post new missing or seen dog  """
    return templates.TemplateResponse('missing_form.html',{"request":request})


@app.post("/new_missing")
async def form(lost_at_date:datetime.date = Form(...),
               lost_at_time:datetime.time = Form(...),
               dog_image: UploadFile= File(...),
               mail:str = Form(...),
               lost_location_image:UploadFile = File(...)):
    """ post new missing or seen dog  """


    print(type(lost_location_image))
    print(lost_location_image.filename)
    return {'filename':lost_location_image.filename}



if __name__ == '__main__':
    uvicorn.run(app)