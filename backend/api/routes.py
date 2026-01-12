from fastapi import APIRouter, UploadFile, File
from services.parser_stub import parse_model
from analysis.geometry import analyze_geometry
from analysis.materials import analyze_materials
from analysis.lods import analyze_lods
from analysis.scoring import estimate_fps, overall_score

router = APIRouter()


@router.post("/analyze")
async def analyze_model(file: UploadFile = File(...)):
    scene = parse_model(file.filename)

    geometry = analyze_geometry(scene)
    materials = analyze_materials(scene)
    lods = analyze_lods(scene)

    fps = estimate_fps(
        geometry["geometry_score"],
        materials["material_score"]
    )

    score = overall_score({
        **geometry,
        **materials,
        **lods
    })

    status = "PASS"
    if fps < 72:
        status = "WARNING"
    if fps < 60:
        status = "FAIL"

    return {
        "file": file.filename,
        "fps_estimate": fps,
        "overall_score": score,
        "status": status,
        "details": {
            **geometry,
            **materials,
            **lods
        }
    }
