from database import SessionLocal, engine
from models import Base, Campaign

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if data already exists
if db.query(Campaign).count() == 0:
    campaigns = [
        Campaign(id=1, name="Summer Sale", status="Active", clicks=150, cost=45.99, impressions=1000),
        Campaign(id=2, name="Black Friday", status="Paused", clicks=320, cost=89.50, impressions=2500),
        Campaign(id=3, name="Winter Deals", status="Active", clicks=200, cost=50.00, impressions=1500),
        Campaign(id=4, name="Flash Offer", status="Paused", clicks=90, cost=22.30, impressions=800),
        Campaign(id=5, name="New Launch", status="Active", clicks=400, cost=120.99, impressions=3000),
        Campaign(id=6, name="Holiday Promo", status="Paused", clicks=180, cost=60.00, impressions=1800),
        Campaign(id=7, name="Year End", status="Active", clicks=350, cost=100.50, impressions=2700),
        Campaign(id=8, name="Monsoon Mania", status="Paused", clicks=140, cost=39.75, impressions=950),
        Campaign(id=9, name="Valentine Special", status="Active", clicks=280, cost=75.20, impressions=2100),
        Campaign(id=10, name="Republic Day", status="Paused", clicks=160, cost=48.50, impressions=1200),
    ]
    db.add_all(campaigns)
    db.commit()
    print("Seeded data.")
else:
    print("Data already exists — no changes made.")

db.close()
