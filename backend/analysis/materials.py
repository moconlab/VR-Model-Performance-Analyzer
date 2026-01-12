def analyze_materials(scene):
    transparent_count = sum(1 for m in scene.materials if m.transparent)
    total = len(scene.materials)

    transparency_ratio = transparent_count / max(total, 1)

    score = 100
    if transparency_ratio > 0.4:
        score -= 40
    elif transparency_ratio > 0.25:
        score -= 20

    return {
        "materials_total": total,
        "transparent_materials": transparent_count,
        "material_score": max(score, 0)
    }
