# VR Model Performance Analyzer - Architecture

## Overview
- Backend: FastAPI Python, parses RVT/NWD, analyzes geometry, materials, draw calls, textures, LODs
- Frontend: React + TypeScript, file upload, dashboard, charts
- Database: SQLite/Postgres for persistence
- Optional: ML FPS prediction and automated LOD generation

## Workflow
1. Upload model via frontend
2. Backend parses and analyzes model
3. ML FPS prediction
4. Optional runtime GPU profiling
5. Results persisted in DB
6. Frontend dashboard displays scores and charts
