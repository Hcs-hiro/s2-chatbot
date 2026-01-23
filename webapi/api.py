from fastapi import FastAPI
from routers import b1_replay
from routers import b2_add
from routers import b3_payroll
from routers import b4_good_words
from routers import b5_omikuji
from routers import b6_hitgame
from routers import b7_get_datetime
from routers import b8_zipcode

app = FastAPI()
# TODO 規定課題の機能追加
app.include_router(b1_replay.router)
app.include_router(b2_add.router)
app.include_router(b3_payroll.router)
app.include_router(b4_good_words.router)
app.include_router(b5_omikuji.router)
app.include_router(b6_hitgame.router)
app.include_router(b7_get_datetime.router)
app.include_router(b8_zipcode.router)

# TODO 追加課題の機能追加
