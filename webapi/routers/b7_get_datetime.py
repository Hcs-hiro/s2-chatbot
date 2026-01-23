from fastapi import APIRouter
import datetime

router = APIRouter()

@router.get("/get_datetime/", tags=["get_datetime"], summary="現在日時取得 API")
async def get_datetime():
  """
  現在の日時を返す API エンドポイント。
  Returns:
  dict: 現在の日時を含む辞書。{"result": "MM/DD HH:MM:SS"}
  Example:
  リクエスト:
  レスポンス:{"result": "01/01 12:34:56"}
  """
  now = datetime.datetime.now()
  formated_now = now.strftime("%m/%d %H:%M:%S")

  return {
              "result": formated_now,     "image_idx": 7} 


