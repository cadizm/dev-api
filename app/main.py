from app import api, config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=config.origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api.wordle.router)
app.include_router(api.words.router)
app.include_router(api.spelling_bee.router)


@app.get("/syn")
def syn_ack():
  return {'message': 'ack'}


# uvicorn --debug --port 9001 --env-file .env/local.py --reload  app.main:app
