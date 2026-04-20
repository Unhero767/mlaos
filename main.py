from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, TableA, init_db

# Initialize the Lithic Substrate on startup
init_db()

app = FastAPI(title="MLAOS Persistent Substrate")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/start_transaction")
async def start_transaction(db: Session = Depends(get_db)):
    # Create a baseline record for id=3 if it doesn't exist
    record = db.query(TableA).filter(TableA.id == 3).first()
    if not record:
        record = TableA(id=3, value="baseline_value", integrity_score=100)
        db.add(record)
        db.commit()
    return {"status": "success", "state": "◦A_INIT", "id": 3}

@app.post("/simulate_failure")
async def simulate_failure(db: Session = Depends(get_db)):
    # This endpoint purposefully does NOT commit to simulate a crash/failure
    try:
        db.execute("UPDATE table_a SET value='corrupted' WHERE id=3")
        # We 'forget' to commit or explicitly raise an error
        raise Exception("Metalogical Burn: Forcing failure.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health(db: Session = Depends(get_db)):
    record = db.query(TableA).filter(TableA.id == 3).first()
    return {
        "status": "STABLE",
        "current_value": record.value if record else "NULL",
        "integrity": record.integrity_score if record else 0
    }
