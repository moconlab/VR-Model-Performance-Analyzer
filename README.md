# VR-Model-Performance-Analyzer [WIP]
A data analysis tool that evaluates whether 3D models will perform well in a generic VR headset application

The tool inspects geometry, materials, textures, and scene structure to estimate VR framerate, identify performance risks, and provide actionable optimization recommendations before runtime.

> **Purpose:** Help teams validate and optimize large BIM and coordination models for VR experiences across multiple headsets.

---

## Features

  * Extracts geometry and metadata using Autodesk APIs
  * VR performance estimation

  * Predicts framerate and highlights CPU/GPU bottlenecks
  * Comprehensive scene analysis

  * Triangle and mesh counts
  * Object count and draw-call estimation
  * Material complexity and transparency detection
  * Texture resolution and GPU memory usage
  * LOD detection and quality assessment
  * Scene tiling and spatial partitioning checks
  * Clear performance scoring

  * Category-level scores
  * Overall VR readiness score
  * Pass / Warning / Fail indicators
  * Optimization recommendations

  * Concrete, model-specific improvement guidance
  * Web-based dashboard

  * Upload models and view interactive reports
  * Export results as PDF or JSON

---

## How It Works

1. **Model Ingestion**
   RVT and NWD files are parsed using Autodesk Revit and Navisworks APIs.

2. **Scene Normalization**
   Geometry, materials, textures, and hierarchy data are converted into a unified internal scene representation.

3. **Performance Analysis**
   Modular analyzers inspect geometry complexity, draw calls, transparency, LOD usage, textures, and spatial organization.

4. **VR Performance Estimation**
   A heuristic-based performance model estimates expected VR framerate and identifies likely bottlenecks.

5. **Scoring & Recommendations**
   Results are summarized into performance scores, warnings, and optimization actions suitable for VR applications.

---

## Metrics Analyzed

* Total triangle and mesh counts
* Object count and hierarchy depth
* Estimated draw calls
* Opaque vs transparent materials
* Overdraw risk
* Texture resolution and estimated GPU memory usage
* LOD presence and triangle reduction ratios
* Scene tiling, culling friendliness, and spatial coherence

---

## Scoring Model

Each model receives:

* **Category Scores (0–100)**

  * Geometry
  * Materials
  * Objects & Draw Calls
  * LOD Strategy
  * Textures
  * Overall VR Readiness Score
  * Estimated FPS Range
  * **Pass / Warning / Fail** status

Scores are calibrated against common VR performance budgets (72–120 FPS depending on headset class).

---

## Tech Stack

* **Backend:** Python, FastAPI
* **Frontend:** React, TypeScript
* **3D APIs:** Autodesk Revit API, Navisworks .NET API
* **Analysis Engine:** Modular rule-based evaluators
* **Visualization:** Interactive charts and dashboards

---

## Project Structure

```
/backend
  /parsers        # RVT and NWD extraction
  /analysis       # Geometry, materials, LOD, texture analyzers
  /scoring        # VR performance and scoring logic
  /api            # FastAPI routes

/frontend
  /components     # UI components
  /pages          # Dashboard views
  /charts         # Performance visualizations

/docs
  architecture.md
  metrics.md
```

---

## Disclaimer

This tool provides **performance estimates and optimization guidance** for VR headset applications.
Actual runtime performance may vary based on headset, GPU/CPU, rendering pipeline, and engine configuration.

