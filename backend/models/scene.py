from pydantic import BaseModel
from typing import List


class Mesh(BaseModel):
    name: str
    triangle_count: int
    instanced: bool


class MaterialInfo(BaseModel):
    name: str
    transparent: bool
    texture_resolution: int


class Scene(BaseModel):
    meshes: List[Mesh]
    materials: List[MaterialInfo]
    object_count: int
    lod_count: int
