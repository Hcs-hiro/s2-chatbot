from fastapi import APIRouter

router = APIRouter()

@router.get("/replay/", tags=["replay"])
async def replay(message: str):
    """
    与えられたメッセージに対する適切な返信を生成して返すAPIエンドポイント。

    Parameters:
    - message (str): ユーザーからの質問や挨拶などのメッセージ。

    Returns:
    dict: 生成された返信を含む辞書。{"result": "生成された返信のメッセージ", "image_idx": 画像のインデックス}

    Example:
    クエリパラメータ message="おはよう" に対してのリクエスト：
    レスポンス：{"result": "おはよう！！",image_idx": 1}

    """

    result = ""
    image_idx = 0

    if message == "おはよう":
        result = "おはよう！！"
        image_idx = 2
    elif message == "チー牛":
        result = "はぁ？！！\nチー牛じゃねえわ！\nトライアル屯田店にうめんぞこらぁ！！"
        image_idx = 3
    else:
        result = "え？すみません。\nよくわかりません。"
        image_idx = 1

    return {
        "result": result, 
        "image_idx": image_idx
        }
