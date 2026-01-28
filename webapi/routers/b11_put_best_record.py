from fastapi import APIRouter
from pydantic import BaseModel
import file_utils

router = APIRouter()


class Item(BaseModel):
    best_record: int



@router.put("/put_best_record/", tags=["put_best_record"], summary="数あて最高記録更新 API")
async def put_best_record(item: Item):
  """
  送られてきた最高記録でファイルの値を更新する API エンドポイント。
  Parameters:
  - item (Item): 更新する最高記録を含むデータクラス。
  Returns:
  dict: 更新が成功した旨の結果を含む辞書。{"result": "保存しました"}
  Example:
  リクエストボディ:
  {"best_record": 5}
  レスポンス:{"result": "保存しました"}
  """

  file_utils.file_write("./data/hitgame.txt", item.best_record)

  return {"result": "保存しました"}
  
  
