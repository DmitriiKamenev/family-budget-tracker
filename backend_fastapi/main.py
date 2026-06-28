from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.health import health_router

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",
                host="127.0.0.1",
                ort=8000,
                reload=True)