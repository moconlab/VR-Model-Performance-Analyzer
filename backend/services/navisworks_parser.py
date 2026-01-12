# Navisworks Add-in context (IronPython / C#)
from Autodesk.Navisworks.Api import Application
from models.scene import Scene, Mesh, MaterialInfo


def parse_navisworks_model() -> Scene:
    doc = Application.ActiveDocument
    meshes = []
    materials = {}

    for item in doc.Models.RootItemDescendants:
        geo = item.Geometry
        if not geo:
            continue

        tri_count = sum(facet.TriangleCount for facet in geo.Facets)

        meshes.append(
            Mesh(
                name=item.DisplayName,
                triangle_count=tri_count,
                instanced=item.IsComposite
            )
        )

        mat = item.Appearance
        if mat and mat.Name not in materials:
            materials[mat.Name] = MaterialInfo(
                name=mat.Name,
                transparent=mat.Transparency > 0,
                texture_resolution=2048
            )

    return Scene(
        meshes=meshes,
        materials=list(materials.values()),
        object_count=len(meshes),
        lod_count=0
    )
