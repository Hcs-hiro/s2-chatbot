from fastapi import APIRouter
import random
router = APIRouter()


@router.get("/good_words/", tags=["good_words"], summary="名言取得 API")
async def good_words():
    """
    名言をランダムに選んで返す API エンドポイント。
    Returns:
    dict: ランダムに選ばれた名言を含む辞書。{"result": "選ばれた名言"}
    Example:
    レスポンス:{"result":
    """

    quotes = [
        "死ぬこと以外はかすり傷。",
        "愛車はラパン。",
        "おれの車ハイジェットは「白い閃光」と呼ばれている。",
        "チー牛は男の頂点",
        "あっせんされなきゃ、何も始まらない。",
    ]
    image_idx = random.randint(1,5)


    quote = random.choice(quotes)
    return {
        "result": quote,
        "image_idx": image_idx
    }
