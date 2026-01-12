from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    device = Column(String)
    fps = Column(Integer)
    score = Column(Integer)
    details = Column(JSON)
