from models.scene import Scene, Mesh, Material
import random


def parse_model(file_name: str) -> Scene:
    # Simulated extraction
    meshes = [
        Mesh(name=f"Mesh_{i}", triangle_count=random.randint(500, 50000))
        for i in range(random.randint(50, 300))
    ]

    materials = [
        Material(
            name=f"Material_{i}",
            transparent=random.random() < 0.25,
            texture_resolution=random.choice([512, 1024, 2048, 4096])
        )
        for i in range(random.randint(10, 80))
    ]

    return Scene(
        meshes=meshes,
        materials=materials,
        object_count=len(meshes),
        lod_count=random.randint(0, 5)
    )
