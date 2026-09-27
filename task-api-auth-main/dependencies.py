from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import supabase

security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    print("TOKEN RECEIVED:", token)

    try:
        user = supabase.auth.get_user(token)
        return user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )