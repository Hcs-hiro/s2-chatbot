from fastapi import APIRouter
import requests

router = APIRouter()  # ← () が必須！


@router.get("/zipcode/", tags=["zipcode"], summary="郵便番号検索 API")
async def get_address(code: str = "0030806"):
    """
    指定された郵便番号に対応する住所を返す API エンドポイント。
    Parameters:
    - code (str): 検索対象の郵便番号。デフォルトは '0030806'。
    Returns:
    dict: 郵便番号に対応する住所を含む辞書。{"result": "検索結果の住所"}
    Example:
    クエリパラメータ code='1000001' に対してのリクエスト:
    レスポンス:{"result": "東京都千代田区千代田"}
    """
    url = "https://zipcloud.ibsnet.co.jp/api/search"
    params = {"zipcode": code}

    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()

    if data["results"] is None:
        return {"result": "住所が見つかりません"}

    result = data["results"][0]
    address = result["address1"] + result["address2"] + result["address3"]

    return {"result": address}


# from fastapi import APIRouter, HTTPException
# import datetime
# import requests
# router = APIRouter

# @router.get("/zipcode/", tags=["zipcode"], summary="郵便番号検索 API")
# async def get_address(code:str='0030806'):
#     """
#   指定された郵便番号に対応する住所を返す API エンドポイント。
#   Parameters:
#   - code (str): 検索対象の郵便番号。デフォルトは '0030806'。
#   Returns:
#   dict: 郵便番号に対応する住所を含む辞書。{"result": "検索結果の住所"}
#   Example:
#   クエリパラメータ code='1000001' に対してのリクエスト:
#   レスポンス:{"result": "東京都千代田区千代田"}
#   """

#     url = "https://zipcloud.ibsnet.co.jp/api/search"
#     params = {"zipcode": code}

#     res = requests.get(url, params=params)
#     res.raise_for_status()

#     data = res.json()

#     if data["results"] is None:
#             raise HTTPException(status_code=404, detail="住所が見つかりません")
#     result = data["results"][0]
#     address = (
#     result["address1"]+
#     result["address2"]+
#     result["address3"]
#   )
#     return {
#         "result": address
#     }
