def analyze_textures(scene):
    total_memory_mb = 0

    for mat in scene.materials:
        size = mat.texture_resolution
        memory = (size * size * 4) / (1024 ** 2)  # RGBA
        total_memory_mb += memory

    score = 100
    if total_memory_mb > 2048:
        score -= 50
    elif total_memory_mb > 1024:
        score -= 30

    return {
        "texture_memory_mb": int(total_memory_mb),
        "texture_score": max(score, 0)
    }
