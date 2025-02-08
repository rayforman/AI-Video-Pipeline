from fastapi import FastAPI
from .database import engine
from .models import models
from .api import topics, videos  # Add videos import

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Video Pipeline")

# Include routers
app.include_router(topics.router)
app.include_router(videos.router)  # Add this line