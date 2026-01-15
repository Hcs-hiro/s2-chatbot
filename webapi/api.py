from fastapi import FastAPI
from routers import b1_replay
from routers import b2_add

app = FastAPI()
# TODO 規定課題の機能追加
app.include_router(b1_replay.router)
app.include_router(b2_add.router)

# TODO 追加課題の機能追加
