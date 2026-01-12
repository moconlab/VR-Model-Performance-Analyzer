import React from "react";
import TriangleChart from "../charts/TriangleChart";
import { SceneDetails } from "../types";

interface ModelDetailsProps {
  details: SceneDetails;
}

const ModelDetails: React.FC<ModelDetailsProps> = ({ details }) => {
  const triangleData = details.meshes.map((m) => ({
    mesh: m.name,
    triangles: m.triangle_count,
  }));

  return (
    <div>
      <h2>Model Details</h2>
      <TriangleChart data={triangleData} />
      <p>Total Objects: {details.object_count}</p>
      <p>LOD Count: {details.lod_count}</p>
      <p>Warnings:</p>
      <ul>
        {details.warnings?.map((w, idx) => (
          <li key={idx}>{w}</li>
        ))}
      </ul>
    </div>
  );
};

export default ModelDetails;
