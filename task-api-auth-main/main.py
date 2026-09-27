from fastapi import FastAPI, Depends
from auth import router as auth_router
from dependencies import verify_token

app = FastAPI(
    title="Task API Authentication"
)

app.include_router(
    auth_router,
    prefix="",
    tags=["Authentication"]
)


@app.get("/")
def home():
    return {
        "message": "Task API Authentication Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/test-supabase")
def test_supabase():
    return {
        "message": "Supabase connected"
    }


@app.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }


@app.get("/protected/profile")
def profile(user=Depends(verify_token)):
    return {
        "id": user.user.id,
        "email": user.user.email
    }