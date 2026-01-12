def estimate_draw_calls(scene):
    unique_meshes = [m for m in scene.meshes if not m.instanced]
    instanced_meshes = [m for m in scene.meshes if m.instanced]

    draw_calls = len(unique_meshes) + max(1, len(instanced_meshes) // 10)

    score = 100
    if draw_calls > 2000:
        score -= 40
    elif draw_calls > 1000:
        score -= 20

    return {
        "estimated_draw_calls": draw_calls,
        "draw_call_score": max(score, 0)
    }
