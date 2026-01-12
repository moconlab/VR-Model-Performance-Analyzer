import React from "react";

interface DeviceSelectorProps {
  selected: string;
  onChange: (device: string) => void;
}

const devices = ["standalone_vr", "pc_vr"];

const DeviceSelector: React.FC<DeviceSelectorProps> = ({ selected, onChange }) => {
  return (
    <select value={selected} onChange={(e) => onChange(e.target.value)}>
      {devices.map((d) => (
        <option key={d} value={d}>
          {d}
        </option>
      ))}
    </select>
  );
};

export default DeviceSelector;
