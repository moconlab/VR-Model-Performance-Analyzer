from sqlalchemy.orm import Session
from models.db import AnalysisResult


def save_result(db: Session, data: dict):
    record = AnalysisResult(**data)
    db.add(record)
    db.commit()
