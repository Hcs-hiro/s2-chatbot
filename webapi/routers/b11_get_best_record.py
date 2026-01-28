from fastapi import APIRouter
import file_utils


router = APIRouter()


@router.get(
    "/get_best_record/", tags=["get_best_record"], summary="数あて最高記録取得 API"
)
async def get_best_record():

    best_record = file_utils.file_read("./data/hitgame.txt")

    return {"result": best_record}
