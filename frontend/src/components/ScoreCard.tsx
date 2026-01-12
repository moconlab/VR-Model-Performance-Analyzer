import React from "react";

interface ScoreCardProps {
  fps: number;
  overallScore: number;
  status: string;
}

const ScoreCard: React.FC<ScoreCardProps> = ({ fps, overallScore, status }) => {
  return (
    <div style={{ border: "1px solid #ccc", padding: 20, margin: 10 }}>
      <h3>Overall Score</h3>
      <p>FPS Estimate: {fps}</p>
      <p>Score: {overallScore}</p>
      <p>Status: {status}</p>
    </div>
  );
};

export default ScoreCard;
