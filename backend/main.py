from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Debt Consolidation Call Center API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Lead(BaseModel):
    id: str
    title: str
    status: str
    score: int
    timestamp: str
    jornaya_token: Optional[str] = None
    trusted_form_cert: Optional[str] = None
    lead_source_url: Optional[str] = None

# In-memory seed data
db = [
    Lead(id="1", title="Lead A", status="pending", score=85, timestamp=datetime.now().isoformat()),
    Lead(id="2", title="Lead B", status="approved", score=92, timestamp=datetime.now().isoformat())
]

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/analytics")
def get_analytics():
    return {"total_leads": len(db), "avg_score": sum(l.score for l in db) / len(db) if db else 0}

@app.post("/api/reviews")
def submit_review(lead: Lead):
    db.append(lead)
    return {"message": "Data submitted successfully", "id": lead.id}

@app.post("/api/v1/bid/approve/6df220f1")
def approve_bid():
    return {"status": "success", "message": "Bid 6df220f1 approved successfully"}
