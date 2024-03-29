from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.users.auth import get_password_hash, create_access_token, autheticate_user
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Пользователь уже существует')
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await autheticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("what_study_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("what_study_access_token")

@router.get("/me")
async def read_own_user(current_user: Users = Depends(get_current_user)):
    return current_user
