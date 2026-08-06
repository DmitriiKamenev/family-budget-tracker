from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.session import init_db
from routers.health import health_router
from routers.user import user_router
from routers.auth import auth_router
from routers.room import room_router
from routers.category import category_router
from routers.transaction import transaction_router

app = FastAPI(
    title="Family Budget Tracker API",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(room_router)
app.include_router(category_router)
app.include_router(transaction_router)

init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
                host="127.0.0.1",
                ort=8000,
                reload=True)

