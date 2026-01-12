def engine_warnings(scene):
    warnings = []

    if scene.object_count > 5000:
        warnings.append("High object count may cause poor batching in Unity.")

    if any(m.transparent for m in scene.materials):
        warnings.append("Transparent materials can cause overdraw in Unreal.")

    if scene.lod_count == 0:
        warnings.append("No LODs detected. Required for VR engines.")

    return warnings
