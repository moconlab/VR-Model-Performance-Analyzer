import React, { useState } from "react";
import FileUploader from "../components/FileUploader";
import DeviceSelector from "../components/DeviceSelector";
import ScoreCard from "../components/ScoreCard";
import TriangleChart from "../charts/TriangleChart";
import TextureChart from "../charts/TextureChart";
import FPSChart from "../charts/FPSChart";
import { analyzeModel } from "../api/api";

const Dashboard: React.FC = () => {
  const [device, setDevice] = useState("standalone_vr");
  const [result, setResult] = useState<any>(null);

  const handleUpload = async (file: File) => {
    const res = await analyzeModel(file, device);
    setResult(res);
  };

  return (
    <div>
      <DeviceSelector selected={device} onChange={setDevice} />
      <FileUploader onUpload={handleUpload} />
      {result && (
        <>
          <ScoreCard
            fps={result.fps_estimate}
            overallScore={result.overall_score}
            status={result.status}
          />
          <h3>Triangles by Mesh</h3>
          <TriangleChart data={result.details.meshes.map((m: any) => ({ mesh: m.name, triangles: m.triangle_count }))} />
          <h3>Texture Resolutions</h3>
          <TextureChart materials={result.details.materials} />
        </>
      )}
    </div>
  );
};

export default Dashboard;
