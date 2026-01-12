import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { MaterialInfo } from "../types";

interface TextureChartProps {
  materials: MaterialInfo[];
}

const TextureChart: React.FC<TextureChartProps> = ({ materials }) => {
  const data = materials.map((m) => ({
    material: m.name,
    resolution: m.texture_resolution,
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey="material" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="resolution" fill="#82ca9d" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default TextureChart;
