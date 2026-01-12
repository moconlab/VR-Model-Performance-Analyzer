def analyze_lods(scene):
    score = 100

    if scene.lod_count == 0:
        score -= 40
    elif scene.lod_count < 3:
        score -= 15

    return {
        "lod_count": scene.lod_count,
        "lod_score": max(score, 0)
    }
