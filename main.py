from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api.classes.router import class_item_router
from api.items.router import item_router
from fastapi.staticfiles import StaticFiles
from handeling import JinjaExeption

# from class_db import *





# Create an appt

app = FastAPI()
app.include_router(class_item_router, prefix='/api')
app.include_router(item_router)
app.mount("/media", StaticFiles(directory="media"), name="ch")

@app.exception_handler(JinjaExeption)
def Login_Failied_expetion_handler(request: Request, exc: JinjaExeption):
    return JSONResponse(status_code=exc.status_code,
                        content={"message": f"{exc.detail}"}
                        )

origins = [
    "https://www.google.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000, reload=True)
