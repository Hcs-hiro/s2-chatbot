from fastapi import APIRouter
import requests
from pydantic import BaseModel
router = APIRouter()  

import file_utils

class Item(BaseModel):
  message: str

@router.post("/log_output/", tags=["log_output"], summary="メッセージ記録 API")
async def record():
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
    log = file_utils.file_readlines(file_path=file_path)

    return {"result": log}
