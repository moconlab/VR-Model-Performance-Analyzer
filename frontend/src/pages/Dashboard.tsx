import React, { useState } from "react";
import FileUploader from "../components/FileUploader";
import DeviceSelector from "../components/DeviceSelector";
import ScoreCard from "../components/ScoreCard";
import TriangleChart from "../charts/TriangleChart";
import TextureChart from "../charts/TextureChart";
import FPSChart from "../charts/FPSChart";
import { analyzeModel } from "../api/api";
import jsPDF from "jspdf";

const Dashboard: React.FC = () => {
  const [device, setDevice] = useState("standalone_vr");
  const [result, setResult] = useState<any>(null);

  // Upload and analyze model
  const handleUpload = async (file: File) => {
    const res = await analyzeModel(file, device);
    setResult({ ...res, file: file.name });
  };

  // Export JSON
  const handleExportJSON = () => {
    if (!result) return;
    const blob = new Blob([JSON.stringify(result, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `${result.file || "model_report"}.json`;
    link.click();
  };

  // Export PDF
  const handleExportPDF = () => {
    if (!result) return;
    const doc = new jsPDF();
    doc.setFontSize(16);
    doc.text("VR Model Performance Report", 10, 10);
    doc.setFontSize(12);
    doc.text(`File: ${result.file}`, 10, 20);
    doc.text(`Overall Score: ${result.overall_score.toFixed(1)}`, 10, 30);
    doc.text(`FPS Estimate: ${result.fps_estimate.toFixed(1)}`, 10, 40);
    doc.text(`Status: ${result.status}`, 10, 50);

    if (result.bottlenecks && result.bottlenecks.length > 0) {
      doc.text("Bottlenecks / Warnings:", 10, 60);
      result.bottlenecks.forEach((b: string, i: number) => {
        doc.text(`- ${b}`, 15, 70 + i * 10);
      });
    }

    doc.save(`${result.file || "model_report"}.pdf`);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>VR Model Performance Dashboard</h1>

      {/* Device Selection */}
      <div style={{ marginBottom: 20 }}>
        <label>Select Device: </label>
        <DeviceSelector selected={device} onChange={setDevice} />
      </div>

      {/* File Upload */}
      <div style={{ marginBottom: 20 }}>
        <FileUploader onUpload={handleUpload} />
      </div>

      {/* Analysis Results */}
      {result && (
        <div>
          {/* Score Card */}
          <ScoreCard
            fps={result.fps_estimate}
            overallScore={result.overall_score}
            status={result.status}
          />

          {/* Charts */}
          <div style={{ marginTop: 20 }}>
            <h3>Triangles per Mesh</h3>
            <TriangleChart
              data={result.meshes.map((m: any) => ({
                mesh: m.name,
                triangles: m.triangle_count,
              }))}
            />
          </div>

          <div style={{ marginTop: 20 }}>
            <h3>Texture Memory per Material (MB)</h3>
            <TextureChart materials={result.materials} />
          </div>

          {result.fps_history && result.fps_history.length > 0 && (
            <div style={{ marginTop: 20 }}>
              <h3>FPS over time</h3>
              <FPSChart data={result.fps_history} />
            </div>
          )}

          {/* Bottlenecks and Recommendations */}
          <div style={{ marginTop: 20 }}>
            <h3>Optimization Recommendations</h3>
            {result.bottlenecks && result.bottlenecks.length > 0 ? (
              <ul>
                {result.bottlenecks.map((b: string, idx: number) => (
                  <li key={idx}>{b}</li>
                ))}
              </ul>
            ) : (
              <p>No bottlenecks detected. Model is optimized for VR.</p>
            )}
          </div>

          {/* LOD and Tiling */}
          <div style={{ marginTop: 20 }}>
            <h3>Scene Analysis</h3>
            <p>LOD Count per Mesh:</p>
            <ul>
              {result.lods.map((l: any, idx: number) => (
                <li key={idx}>
                  {l.mesh}: {l.lods.length} LODs
                </li>
              ))}
            </ul>
            <p>
              Scene Tiling Recommended: {result.tiling_needed ? "Yes" : "No"}
            </p>
          </div>

          {/* Export Buttons */}
          <div style={{ marginTop: 20 }}>
            <button onClick={handleExportJSON} style={{ marginRight: 10 }}>
              Export JSON
            </button>
            <button onClick={handleExportPDF}>Export PDF</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
