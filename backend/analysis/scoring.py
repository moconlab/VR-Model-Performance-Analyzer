def estimate_fps(geometry_score, material_score):
    fps = 90
    fps -= (100 - geometry_score) * 0.4
    fps -= (100 - material_score) * 0.3
    return max(int(fps), 30)


def overall_score(scores: dict):
    weighted = (
        scores["geometry_score"] * 0.4 +
        scores["material_score"] * 0.35 +
        scores["lod_score"] * 0.25
    )
    return int(weighted)
