from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.core.database import init_db
from app.api.routes import router as auth_router
from app.core.database import Base, engine, init_db
from app.core.settings import settings


app = FastAPI(root_path="/users")

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    same_site="lax",
    session_cookie="session_id",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix=settings.PREFIX)

@app.on_event("startup")
def startup():
    init_db()