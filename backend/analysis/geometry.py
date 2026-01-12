def analyze_geometry(scene):
    total_triangles = sum(m.triangle_count for m in scene.meshes)

    score = 100
    if total_triangles > 10_000_000:
        score -= 50
    elif total_triangles > 5_000_000:
        score -= 30
    elif total_triangles > 2_000_000:
        score -= 15

    return {
        "total_triangles": total_triangles,
        "geometry_score": max(score, 0)
    }
