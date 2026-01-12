from pydantic import BaseModel
from typing import List


class Mesh(BaseModel):
    name: str
    triangle_count: int
    instanced: bool = False


class Material(BaseModel):
    name: str
    transparent: bool
    texture_resolution: int  # max dimension (e.g. 2048)


class Scene(BaseModel):
    meshes: List[Mesh]
    materials: List[Material]
    object_count: int
    lod_count: int
