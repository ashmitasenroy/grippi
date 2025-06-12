from fastapi import FastAPI
from database import SessionLocal
from models import Campaign
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to fetch data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/campaigns")
def get_campaigns():
    db = SessionLocal()
    campaigns = db.query(Campaign).all()
    result = [c.__dict__ for c in campaigns]
    for item in result:
        item.pop("_sa_instance_state", None)
    return result

@app.get("/")
def root():
    return {"message": "Hello! Go to /campaigns or /docs"}
