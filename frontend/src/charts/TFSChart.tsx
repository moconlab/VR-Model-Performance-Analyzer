import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

interface FPSChartProps {
  data: { frame: number; fps: number }[];
}

const FPSChart: React.FC<FPSChartProps> = ({ data }) => (
  <ResponsiveContainer width="100%" height={300}>
    <LineChart data={data}>
      <XAxis dataKey="frame" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="fps" stroke="#ff7300" />
    </LineChart>
  </ResponsiveContainer>
);

export default FPSChart;
