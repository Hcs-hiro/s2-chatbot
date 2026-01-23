from fastapi import APIRouter

import random

router = APIRouter()

@router.get("/omikuji/", tags=["omikuji"], summary="おみくじ API")
async def omikuji():
    """
    おみくじの結果をランダムに返す API エンドポイント。
    Returns:
    dict: おみくじの結果と結びつく画像のインデックスを含む辞書。
    {"result": "おみくじの結果", "image_idx": 画像のインデックス}
    Example:
    レスポンス:{"result": "大吉", "image_idx": 1}
    """

    fortune = random.randint(1, 100)

    

    if 91 <= fortune <= 100:
        return {
            "result": "大吉",      "image_idx": 6}
    elif 71 <= fortune <= 90:
        return {"result": "中吉",     "image_idx": 5}
    elif 41 <= fortune <= 70:
        return {"result": "吉", "image_idx": 2}

    elif 11 <= fortune <= 40:
        return {"result": "末吉", "image_idx": 3}

    else:
        return {"result": "凶", "image_idx": 4}
