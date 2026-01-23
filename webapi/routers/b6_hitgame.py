from fastapi import APIRouter

router = APIRouter()


@router.get("/hitgame/", tags=["hitgame"])
async def hitgame(answer: int, guess: int):
    """
    answer: 当たりの数値
    guess : ユーザ入力値
    """

    if guess == answer:
        result = "hit"
    elif abs(guess - answer) <= 2:
        result = "near"
    elif guess < answer:
        result = "low"
    else:
        result = "high"

    return {"result": result, "answer": answer}
