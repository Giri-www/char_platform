from fastapi import APIRouter
from services.proxy_service import forward_request
from config import USER_SERVICE

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: int):

    url = f"{USER_SERVICE}/users/{user_id}"

    response = await forward_request("GET", url)

    return response