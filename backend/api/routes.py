from fastapi import APIRouter, UploadFile, File
from analysis.geometry import analyze_geometry
from analysis.materials import analyze_materials
from analysis.draw_calls import estimate_draw_calls
from analysis.textures import analyze_textures
from analysis.tiling import analyze_scene_tiling
from analysis.engine_warnings import engine_warnings
from analysis.devices import DEVICE_PROFILES
from services.parser_stub import parse_model
from analysis.geometry import analyze_geometry
from analysis.materials import analyze_materials
from analysis.lods import analyze_lods
from analysis.scoring import estimate_fps, overall_score

router = APIRouter()


@router.post("/analyze/{device}")
async def analyze_model(device: str, file: UploadFile = File(...)):
    profile = DEVICE_PROFILES[device]

    # Scene is injected from Revit/Navisworks runtime
    scene = get_scene_from_host_application()

    geometry = analyze_geometry(scene)
    materials = analyze_materials(scene)
    draw_calls = estimate_draw_calls(scene)
    textures = analyze_textures(scene)
    tiling = analyze_scene_tiling(scene)
    warnings = engine_warnings(scene)

    fps = min(profile["target_fps"], 90 - (100 - geometry["geometry_score"]))

    return {
        "device": device,
        "fps_estimate": fps,
        "warnings": warnings,
        "details": {
            **geometry,
            **materials,
            **draw_calls,
            **textures,
            **tiling
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
