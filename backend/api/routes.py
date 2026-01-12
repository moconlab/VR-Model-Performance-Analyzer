from fastapi import APIRouter, UploadFile, File
from analysis.geometry import analyze_geometry
from analysis.materials import analyze_materials
from analysis.draw_calls import estimate_draw_calls
from analysis.textures import analyze_textures
from analysis.tiling import analyze_scene_tiling
from analysis.engine_warnings import engine_warnings
from analysis.devices import DEVICE_PROFILES

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
        }
    }
