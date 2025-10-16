from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .db import connect_to_mongo, close_mongo_connection, check_mongo_connection
from .auth.routes import router as auth_router
from .dashboard.routes import router as dashboard_router
from .payments.routes import router as payments_router
from .ai.routes import router as ai_router
from .reminders.routes import router as reminders_router

app = FastAPI(title="Finance AI Assistant", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
app.include_router(payments_router, prefix="/payments", tags=["payments"])
app.include_router(ai_router, prefix="/ai", tags=["ai"])
app.include_router(reminders_router, prefix="/reminders", tags=["reminders"])

@app.get("/")
async def root():
    return {"status": "ok", "service": app.title, "version": app.version}

@app.get("/health")
async def health_check():
    """Health check endpoint that verifies database connectivity."""
    db_healthy = await check_mongo_connection()

    if db_healthy:
        return {
            "status": "healthy",
            "database": "connected",
            "database_name": settings.DATABASE_NAME,
            "service": app.title,
            "version": app.version
        }
    else:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "service": app.title,
            "version": app.version
        }
