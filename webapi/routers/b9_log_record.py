from fastapi import APIRouter
import requests
from pydantic import BaseModel
router = APIRouter()  

import file_utils

class Item(BaseModel):
  message: str

@router.post("/log_record/", tags=["log_record"], summary="メッセージ記録 API")
async def record(item: Item):
    """
    送られてきたメッセージをファイルに保存する API エンドポイント。
    Parameters:
    - item (Item): 保存するメッセージを含むデータクラス。
    Returns:
    dict: 保存が成功した旨の結果を含む辞書。{"result": "保存しました"}
    Example:
    デ
    """

    file_path = "./data/record.txt"
    file_utils.file_append(file_path=file_path, value=item.message)

    return {"result":"保存しました。"}
