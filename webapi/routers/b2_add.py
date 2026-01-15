from fastapi import APIRouter

router = APIRouter()

# 足し算API
@router.get("/add/", tags=["add"], summary="足し算API")
async def add(x: int=0, y: int=0):
    """
    指定された数値 x と y を加算して結果を返すAPIエンドポイント。
    
    Parameters:
    - x (int): 足し合わせる数値の一つ。
    - y (int): 足し合わせるもう一つの数値。

    Returns:
    dict: 加算結果を含む辞書。{"result": x + y}

    Example:
    クエリパラメータ x=5, y=3 に対してのリクエスト：
    レスポンス：{"result": 8}
    """
    return {
        "result": x + y
    }