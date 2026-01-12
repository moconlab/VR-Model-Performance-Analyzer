def analyze_scene_tiling(scene):
    large_scene = scene.object_count > 5000

    score = 100
    if large_scene:
        score -= 30

    return {
        "tiling_recommended": large_scene,
        "tiling_score": max(score, 0)
    }
