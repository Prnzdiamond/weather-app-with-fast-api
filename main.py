from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fetch import get_weather


app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/weather")
async def weather(request: Request, city: str = Form(...)):
    data = get_weather(city)
    if "error" in data:
        return templates.TemplateResponse("index.html", {"request": request, "error": data['error']['message']})
    if "location" in data:
        print(data)
        return templates.TemplateResponse("index.html", {"request": request,   "location": data["location"],
                                                         "current": data["current"]})
    # return {"data": data}
