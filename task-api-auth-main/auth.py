from fastapi import APIRouter
from pydantic import BaseModel
from config import supabase
from fastapi import Depends
from dependencies import verify_token

router = APIRouter()


class UserSignup(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/signup",status_code=201)
def signup(user: UserSignup):
    response = supabase.auth.sign_up(
        {
            "email": user.email,
            "password": user.password,
        }
    )

    return {
        "message": "User registered successfully",
        "data": response
    }


@router.post("/login")
def login(user: UserLogin):
    response = supabase.auth.sign_in_with_password(
        {
            "email": user.email,
            "password": user.password,
        }
    )

    return {
        "message": "Login successful",
        "data": response
    }

@router.post("/logout", status_code=204)
def logout(user=Depends(verify_token)):
    supabase.auth.sign_out()
    return