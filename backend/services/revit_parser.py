# pyRevit context
from Autodesk.Revit.DB import FilteredElementCollector, Material
from models.scene import Scene, Mesh, MaterialInfo


def parse_revit_model(doc) -> Scene:
    meshes = []
    materials = {}

    elements = FilteredElementCollector(doc).WhereElementIsNotElementType()

    for el in elements:
        geom = el.get_Geometry(None)
        if not geom:
            continue

        tri_count = 0
        for g in geom:
            if hasattr(g, "Triangles"):
                tri_count += g.Triangles.Count

        meshes.append(
            Mesh(
                name=str(el.Id),
                triangle_count=tri_count,
                instanced=el.CanBeHidden(doc.ActiveView)
            )
        )

        mat_id = el.GetMaterialIds(False)
        for mid in mat_id:
            mat = doc.GetElement(mid)
            if mat and mat.Id not in materials:
                materials[mat.Id] = MaterialInfo(
                    name=mat.Name,
                    transparent=mat.Transparency > 0,
                    texture_resolution=2048  # Revit does not expose directly
                )

    return Scene(
        meshes=meshes,
        materials=list(materials.values()),
        object_count=len(meshes),
        lod_count=0
    )
