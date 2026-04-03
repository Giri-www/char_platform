""" Auth Routes """
from fastapi import APIRouter, Request
from app.service.service_proxy import forward_request
from app.config import AUTH_SERVICE

router = APIRouter()

@router.post("/login")
async def login(request: Request):

    body = await request.json()

    url = f"{AUTH_SERVICE}/login"

    response = await forward_request("POST", url, body)

    return response


@router.post("/register")
async def register(request: Request):

    body = await request.json()

    url = f"{AUTH_SERVICE}/register"

    response = await forward_request("POST", url, body)

    return response

