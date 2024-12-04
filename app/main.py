from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api.endpoints import admin, organization
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers
app.include_router(
    admin.router,
    prefix=f"{settings.API_V1_STR}/admin",
    tags=["admin"]
)
app.include_router(
    organization.router,
    prefix=f"{settings.API_V1_STR}/org",
    tags=["organization"]
)

@app.get("/")
def root():
    return {"message": "Welcome to Organization Management API"}